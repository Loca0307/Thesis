func (s *DriverTestSuite) TestOnUnsafeL2PayloadWithInvalidPayload() {
	s.ForkIntoPacaya(s.p, s.d.ChainSyncer().BlobSyncer())
	// Propose some valid L2 blocks
	s.ProposeAndInsertEmptyBlocks(s.p, s.d.ChainSyncer().BlobSyncer())

	l2Head1, err := s.d.rpc.L2.HeaderByNumber(context.Background(), nil)
	s.Nil(err)

	b, err := utils.Compress(testutils.RandomBytes(32))
	s.Nil(err)

	baseFee, overflow := uint256.FromBig(common.Big256)
	s.False(overflow)

	payload := &eth.ExecutionPayload{
		ParentHash:    l2Head1.Hash(),
		FeeRecipient:  s.TestAddr,
		PrevRandao:    eth.Bytes32(testutils.RandomHash()),
		BlockNumber:   eth.Uint64Quantity(l2Head1.Number.Uint64() + 1),
		GasLimit:      eth.Uint64Quantity(l2Head1.GasLimit),
		Timestamp:     eth.Uint64Quantity(time.Now().Unix()),
		ExtraData:     l2Head1.Extra,
		BaseFeePerGas: eth.Uint256Quantity(*baseFee),
		Transactions:  []eth.Data{b},
		Withdrawals:   &types.Withdrawals{},
	}

	s.Nil(s.d.preconfBlockServer.OnUnsafeL2Payload(
		context.Background(),
		peer.ID(testutils.RandomBytes(32)),
		&eth.ExecutionPayloadEnvelope{ExecutionPayload: payload},
	))

	l2Head2, err := s.d.rpc.L2.BlockByNumber(context.Background(), nil)
	s.Nil(err)
	s.Equal(l2Head1.Number.Uint64(), l2Head2.Number().Uint64())
	s.Equal(l2Head1.Hash(), l2Head2.Hash())
}

func (s *DriverTestSuite) TestOnUnsafeL2PayloadWithMissingAncients() {
	s.ForkIntoPacaya(s.p, s.d.ChainSyncer().BlobSyncer())
	// Propose some valid L2 blocks
	s.ProposeAndInsertEmptyBlocks(s.p, s.d.ChainSyncer().BlobSyncer())

	l2Head1, err := s.d.rpc.L2.HeaderByNumber(context.Background(), nil)
	s.Nil(err)

	headL1Origin, err := s.RPCClient.L2.HeadL1Origin(context.Background())
	s.Nil(err)
	s.Equal(l2Head1.Number.Uint64(), headL1Origin.BlockID.Uint64())

	snapshotID := s.SetL1Snapshot()

	for i := 0; i < rand.Intn(6)+5; i++ {
		s.ProposeAndInsertEmptyBlocks(s.p, s.d.ChainSyncer().BlobSyncer())
	}

	l2Head2, err := s.d.rpc.L2.HeaderByNumber(context.Background(), nil)
	s.Nil(err)
	s.Greater(l2Head2.Number.Uint64(), l2Head1.Number.Uint64())

	blocks := []*types.Block{}
	for i := l2Head1.Number.Uint64() + 1; i <= l2Head2.Number.Uint64(); i++ {
		block, err := s.RPCClient.L2.BlockByNumber(context.Background(), new(big.Int).SetUint64(i))
		s.Nil(err)
		blocks = append(blocks, block)
	}
	s.Equal(l2Head2.Number.Uint64()-l2Head1.Number.Uint64(), uint64(len(blocks)))

	s.RevertL1Snapshot(snapshotID)
	s.Nil(rpc.SetHead(context.Background(), s.RPCClient.L2, l2Head1.Number))
	_, err = s.RPCClient.L2Engine.SetHeadL1Origin(context.Background(), headL1Origin.BlockID)
	s.Nil(err)

	headL1Origin, err = s.RPCClient.L2.HeadL1Origin(context.Background())
	s.Nil(err)
	s.Equal(l2Head1.Number.Uint64(), headL1Origin.BlockID.Uint64())

	l2Head3, err := s.d.rpc.L2.HeaderByNumber(context.Background(), nil)
	s.Nil(err)
	s.Equal(l2Head1.Number.Uint64(), l2Head3.Number.Uint64())

	// Randomly gossip preconfirmation messages with missing ancients
	blockNums := rand.Perm(len(blocks))
	for i := range blockNums {
		blockNums[i] += int(l2Head1.Number.Uint64() + 1)
	}

	getBlock := func(blockNum uint64) *types.Block {
		for _, b := range blocks {
			if b.Number().Uint64() == blockNum {
				return b
			}
		}
		return nil
	}

	insertPayloadFromBlock := func(block *types.Block, gossipRandom bool) {
		baseFee, overflow := uint256.FromBig(block.BaseFee())
		s.False(overflow)

		b, err := utils.EncodeAndCompressTxList(block.Transactions())
		s.Nil(err)
		s.GreaterOrEqual(len(block.Transactions()), 1)

		s.Nil(s.d.preconfBlockServer.OnUnsafeL2Payload(
			context.Background(),
			peer.ID(testutils.RandomBytes(32)),
			&eth.ExecutionPayloadEnvelope{ExecutionPayload: &eth.ExecutionPayload{
				BlockHash:     block.Hash(),
				ParentHash:    block.ParentHash(),
				FeeRecipient:  block.Coinbase(),
				PrevRandao:    eth.Bytes32(block.MixDigest()),
				BlockNumber:   eth.Uint64Quantity(block.Number().Uint64()),
				GasLimit:      eth.Uint64Quantity(block.GasLimit()),
				Timestamp:     eth.Uint64Quantity(block.Time()),
				ExtraData:     block.Extra(),
				BaseFeePerGas: eth.Uint256Quantity(*baseFee),
				Transactions:  []eth.Data{b},
				Withdrawals:   &types.Withdrawals{},
			}},
		))

		if gossipRandom {
			// Also gossip some random blocks
			s.Nil(s.d.preconfBlockServer.OnUnsafeL2Payload(
				context.Background(),
				peer.ID(testutils.RandomBytes(32)),
				&eth.ExecutionPayloadEnvelope{ExecutionPayload: &eth.ExecutionPayload{
					BlockHash:     common.BytesToHash(testutils.RandomBytes(32)),
					ParentHash:    common.BytesToHash(testutils.RandomBytes(32)),
					FeeRecipient:  block.Coinbase(),
					PrevRandao:    eth.Bytes32(common.BytesToHash(testutils.RandomBytes(32))),
					BlockNumber:   eth.Uint64Quantity(block.Number().Uint64()),
					GasLimit:      eth.Uint64Quantity(block.GasLimit()),
					Timestamp:     eth.Uint64Quantity(block.Time()),
					ExtraData:     block.Extra(),
					BaseFeePerGas: eth.Uint256Quantity(*baseFee),
					Transactions:  []eth.Data{b},
					Withdrawals:   &types.Withdrawals{},
				}},
			))

			s.Nil(s.d.preconfBlockServer.OnUnsafeL2Payload(
				context.Background(),
				peer.ID(testutils.RandomBytes(32)),
				&eth.ExecutionPayloadEnvelope{ExecutionPayload: &eth.ExecutionPayload{
					BlockHash:     common.BytesToHash(testutils.RandomBytes(32)),
					ParentHash:    block.ParentHash(),
					FeeRecipient:  block.Coinbase(),
					PrevRandao:    eth.Bytes32(common.BytesToHash(testutils.RandomBytes(32))),
					BlockNumber:   eth.Uint64Quantity(block.Number().Uint64()),
					GasLimit:      eth.Uint64Quantity(block.GasLimit()),
					Timestamp:     eth.Uint64Quantity(block.Time()),
					ExtraData:     block.Extra(),
					BaseFeePerGas: eth.Uint256Quantity(*baseFee),
					Transactions:  []eth.Data{b},
					Withdrawals:   &types.Withdrawals{},
				}},
			))
		}
	}

	// Insert all blocks except the first one
	for _, blockNum := range blockNums {
		if blockNum == int(l2Head1.Number.Uint64()+1) {
			continue
		}

		block := getBlock(uint64(blockNum))
		s.NotNil(block)

		insertPayloadFromBlock(block, true)
	}

	l2Head4, err := s.d.rpc.L2.BlockByNumber(context.Background(), nil)
	s.Nil(err)
	s.Equal(l2Head1.Number.Uint64(), l2Head4.Number().Uint64())

	// Insert the only missing ancient block
	block := getBlock(l2Head1.Number.Uint64() + 1)
	s.NotNil(block)
	insertPayloadFromBlock(block, false)

	l2Head5, err := s.d.rpc.L2.BlockByNumber(context.Background(), nil)
	s.Nil(err)
	s.Equal(l2Head2.Number.Uint64(), l2Head5.Number().Uint64())
}
