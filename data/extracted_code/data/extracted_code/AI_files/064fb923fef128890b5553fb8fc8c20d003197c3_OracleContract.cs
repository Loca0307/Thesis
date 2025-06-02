            var urlSize = url.GetStrictUtf8ByteCount();
            if (urlSize > MaxUrlLength)
                throw new ArgumentException($"The url bytes size({urlSize}) cannot be greater than {MaxUrlLength}.");

            var filterSize = filter.GetStrictUtf8ByteCount();
            if (filterSize > MaxFilterLength)
                throw new ArgumentException($"The filter bytes size({filterSize}) cannot be greater than {MaxFilterLength}.");

            var callbackSize = callback is null ? 0 : callback.GetStrictUtf8ByteCount();
            if (callbackSize > MaxCallbackLength)
                throw new ArgumentException($"The callback bytes size({callbackSize}) cannot be greater than {MaxCallbackLength}.");

            if (callback.StartsWith('_'))
                throw new ArgumentException($"The callback cannot start with '_'.");

            if (gasForResponse < 0_10000000)
                throw new ArgumentException($"The gasForResponse({gasForResponse}) must be greater than or equal to 0.1 datoshi.");