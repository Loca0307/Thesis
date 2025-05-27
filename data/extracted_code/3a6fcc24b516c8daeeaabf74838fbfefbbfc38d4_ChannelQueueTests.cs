		foreach (var item in items)
		{
			await channel.WriteAsync(item);
		}

		channel.Lock(); // Lock the channel to allow ListenAsync to complete.

		var readItems = new List<int>();
		await foreach (var item in channel.ListenAsync())
		{
			readItems.Add(item);
		}