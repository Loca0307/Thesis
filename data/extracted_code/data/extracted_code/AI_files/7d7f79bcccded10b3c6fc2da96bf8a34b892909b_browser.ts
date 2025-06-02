      const headers = req.headers();
      const url = req.url();
      const method = req.method();
      const referer = headers['referer'] ?? '';

      try {
        const urlHostname = new URL(url).hostname;
        const refererHostname = referer ? new URL(referer).hostname : '';
        const shouldAddHeaders = req.isNavigationRequest() || urlHostname === refererHostname;
        this.log.debug('Comparing referer and URL hostnames', 'method', method, 'shouldAddHeaders', shouldAddHeaders, 'url', url, 'referer', referer);

        if (shouldAddHeaders) {
          headers['traceparent'] = optionsHeaders['traceparent'] ?? '';
          headers['tracestate'] = optionsHeaders['tracestate'] ?? '';
        }
      } catch (error) {
        this.log.debug('Failed to add tracing headers', 'url', url, 'referer', referer, 'error', error.message);