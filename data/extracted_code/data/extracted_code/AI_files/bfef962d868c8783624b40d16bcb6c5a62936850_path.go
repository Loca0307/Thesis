		// checking the found parameterStartChar is a cluster
		i := nextParamPosition + 1
		for i < len(pattern) {
			if findNextNonEscapedCharsetPosition(pattern[i:i+1], parameterStartChars) != 0 {
				// It was a single parameter start char or end of cluster