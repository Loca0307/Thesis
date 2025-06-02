        try:
            await message.add_reaction(emoji)
        except discord.NotFound:
            # Message was deleted, ignore and stop executing
            return