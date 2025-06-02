      // Add current earners to LUT
      for (const pid of [PROGRAM_ID, EXT_PROGRAM_ID]) {
        const auth = await EarnAuthority.load(connection, evmClient, new Graph(''), pid);
        const earners = await auth.getAllEarners();

        for (const earner of earners) {
          addressesForTable.push(earner.pubkey, earner.data.userTokenAccount);

          // Check if there is an earn manager
          if (
            earner.data.earnManager &&
            !addressesForTable.find((a) => a.equals(earner.data.earnManager))
          ) {
            addressesForTable.push(earner.data.earnManager);
          }
        }
      }
