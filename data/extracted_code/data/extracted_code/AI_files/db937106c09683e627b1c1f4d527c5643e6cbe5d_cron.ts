		const chatUsers = await findUsersInChat.run({ chatId }, client)
		const userNames = chatUsers.map((user) => user.name).join(', ')

		const userMessage: ChatCompletionMessageParam = {
			role: 'user',
			content: `Good morning, ${userNames}! Today is a new opportunity to continue building positive habits. Whether it's ${habitStr} or any other personal goals, remember that each small step is a part of your journey towards success and well-being. Stay focused, stay motivated, and embrace the day with enthusiasm! You've got this!`,
		}

		let chatMessage: string
		try {
			chatMessage = await generateChatMessage([userMessage])
		} catch (error) {
			chatMessage = `Good morning, accountability champions! 🌞 Today is a brand new opportunity to find your inner peace and clarity through meditation. Take a deep breath, commit to your practice, and let's make today another successful day on our journey to mindfulness and well-being. 🧘‍♀️🧘‍♂️ #MeditationMasters`
			console.error('Failed to generate chat message', error)
		}

		await bot.telegram.sendMessage(chatId, chatMessage)