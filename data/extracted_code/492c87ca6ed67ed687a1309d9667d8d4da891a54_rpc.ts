    try {
      const { lastValidBlockHeight, blockhash } = await connection.getLatestBlockhash();

      await connection.confirmTransaction(
        {
          blockhash: blockhash,
          lastValidBlockHeight: lastValidBlockHeight,
          signature: sig,
        },
        'confirmed',
      );
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : JSON.stringify(error);
      throw new Error(`Failed to confirm transaction: ${sig}. Error details: ${errorMessage}`);
    }