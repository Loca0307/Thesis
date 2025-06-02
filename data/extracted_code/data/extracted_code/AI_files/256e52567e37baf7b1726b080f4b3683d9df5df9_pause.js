      try {
        output.print(output.styles.debug(JSON.stringify(val, null, 2)))
      } catch (err) {
        output.print(output.styles.error(' ERROR '), 'Failed to stringify result:', err.message)
        output.print(output.styles.error(' RAW VALUE '), String(val))
      }