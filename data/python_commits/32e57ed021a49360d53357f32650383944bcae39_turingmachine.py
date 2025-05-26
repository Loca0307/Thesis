for i in range(0,len(tape)):
	try:
		tape[i] = int(tape[i])
	except ValueError:
		try:
			assert tape[i] in symbols
		except AssertionError:
			tape[i] = "A"
	else:
		try:
			assert tape[i] in symbols
		except AssertionError:
			tape[i] = 0