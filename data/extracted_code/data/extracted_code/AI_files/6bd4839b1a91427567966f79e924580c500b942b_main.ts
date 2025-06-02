  program
    .command('update-earn-lut')
    .description('Create or update the LUT for common addresses')
    .option('-a, --address [pubkey]', 'Address of table to update', 'HtKQ9sHyMhun73asZsARkGCc1fDz2dQH7QhGfFJcQo7S')
    .action(async ({ address }) => {
      const [owner] = keysFromEnv(['OWNER_KEYPAIR']);
      const ixs = [ComputeBudgetProgram.setComputeUnitPrice({ microLamports: 250_000 })];

      // Get or create LUT
      let tableAddress: PublicKey;
      if (address) {
        tableAddress = new PublicKey(address);
      } else {
        const [lookupTableIx, lookupTableAddress] = AddressLookupTableProgram.createLookupTable({
          authority: owner.publicKey,
          payer: owner.publicKey,
          recentSlot: (await connection.getSlot({ commitment: 'finalized' })) - 10,
        });

        console.log(`Creating lookup table: ${lookupTableAddress.toBase58()}`);
        tableAddress = lookupTableAddress;
        ixs.push(lookupTableIx);
      }

      // Addresses to add to LUT
      const [mMint, wmMint, multisig] = keysFromEnv(['M_MINT_KEYPAIR', 'WM_MINT_KEYPAIR', 'M_MINT_MULTISIG_KEYPAIR']);
      const [portalTokenAuthPda] = PublicKey.findProgramAddressSync([Buffer.from('token_authority')], PROGRAMS.portal);
      const [earnTokenAuthPda] = PublicKey.findProgramAddressSync([Buffer.from('token_authority')], PROGRAMS.earn);
      const [mVaultPda] = PublicKey.findProgramAddressSync([Buffer.from('m_vault')], PROGRAMS.extEarn);
      const [mintAuthPda] = PublicKey.findProgramAddressSync([Buffer.from('mint_authority')], PROGRAMS.extEarn);
      const [global] = PublicKey.findProgramAddressSync([Buffer.from('global')], PROGRAM_ID);
      const [extGlobal] = PublicKey.findProgramAddressSync([Buffer.from('global')], EXT_PROGRAM_ID);

      const addressesForTable = [
        PROGRAMS.portal,
        PROGRAMS.earn,
        PROGRAMS.extEarn,
        mMint.publicKey,
        wmMint.publicKey,
        multisig.publicKey,
        portalTokenAuthPda,
        earnTokenAuthPda,
        mVaultPda,
        mintAuthPda,
        global,
        extGlobal,
      ];

      // Fetch current state of LUT
      let existingAddresses: PublicKey[] = [];
      if (address) {
        const state = (await connection.getAddressLookupTable(tableAddress)).value?.state.addresses;
        if (!state) {
          throw new Error(`Failed to fetch state for address lookup table ${tableAddress}`);
        }
        if (state.length === 256) {
          throw new Error('LUT is full');
        }

        existingAddresses = state;
      }

      // Dedupe missing addresses
      const toAdd = addressesForTable.filter((address) => !existingAddresses.find((a) => a.equals(address)));
      if (toAdd.length === 0) {
        console.log('No addresses to add');
        return;
      }

      ixs.push(
        AddressLookupTableProgram.extendLookupTable({
          payer: owner.publicKey,
          authority: owner.publicKey,
          lookupTable: tableAddress,
          addresses: toAdd,
        }),
      );

      // Send transaction
      const blockhash = await connection.getLatestBlockhash('finalized');

      const messageV0 = new TransactionMessage({
        payerKey: owner.publicKey,
        recentBlockhash: blockhash.blockhash,
        instructions: ixs,
      }).compileToV0Message();

      const transaction = new VersionedTransaction(messageV0);
      transaction.sign([owner]);
      const txid = await connection.sendTransaction(transaction);
      console.log('Transaction sent:', txid);

      // Confirm
      const confirmation = await connection.confirmTransaction(
        { signature: txid, blockhash: blockhash.blockhash, lastValidBlockHeight: blockhash.lastValidBlockHeight },
        'confirmed',
      );
      if (confirmation.value.err) {
        throw new Error(`Transaction not confirmed: ${confirmation.value.err}`);
      }
    });
