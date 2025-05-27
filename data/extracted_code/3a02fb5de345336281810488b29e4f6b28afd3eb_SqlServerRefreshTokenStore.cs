        EnsureRefreshTokenTableCreated();

        var tokens = new List<KeyValuePair<string, RefreshToken>>();

        await using var command = _connection.CreateCommand();
        command.CommandText = "SELECT Id, UserIdentifier, TokenString, ExpireAt FROM RefreshTokens WHERE ExpireAt < @ExpireAt";
        command.AddParameter("@ExpireAt", DbType.DateTime, time);
        await command.ExecuteNonQueryAsync();

        await using var reader = await command.ExecuteReaderAsync();
        while (await reader.ReadAsync())
        {
            tokens.Add(new KeyValuePair<string, RefreshToken>(
                reader.GetString(0),
                new RefreshToken
                {
                    UserIdentifier = reader.GetString(1),
                    TokenString = reader.GetString(2),
                    ExpireAt = reader.GetDateTime(3)
                }));
        }

        return tokens;