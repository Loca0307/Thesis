            Transactions = DeserializeTransactions(ref reader, ushort.MaxValue, Header.MerkleRoot);
        }

        private static Transaction[] DeserializeTransactions(ref MemoryReader reader, int maxCount, UInt256 merkleRoot)
        {
            var count = (int)reader.ReadVarInt((ulong)maxCount);
            var hashes = new UInt256[count];
            var txs = new Transaction[count];

            if (count > 0)
            {
                var hashset = new HashSet<UInt256>();
                for (var i = 0; i < count; i++)
                {
                    var tx = reader.ReadSerializable<Transaction>();
                    if (!hashset.Add(tx.Hash))
                        throw new FormatException();
                    txs[i] = tx;
                    hashes[i] = tx.Hash;
                }
            }

            if (MerkleTree.ComputeRoot(hashes) != merkleRoot)
                throw new FormatException("The computed Merkle root does not match the expected value.");
            return txs;