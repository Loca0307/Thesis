    private static List<CheepViewModel> ConnectAndExecute(string query, string author)
    {
        var cheeps = new List<CheepViewModel>();
        using (var connection = new SqliteConnection($"Data Source={sqlDBFilePath}"))
        {
            connection.Open();

            var command = connection.CreateCommand();
            command.CommandText = query;
            command.Parameters.Add("@Author", SqliteType.Text);
            command.Parameters["@Author"].Value = author;

            using var reader = command.ExecuteReader();
            while (reader.Read())
            {
                var message_id = reader.GetString(0);
                var author_id = reader.GetInt32(1);
                var message = reader.GetString(2);
                var date = reader.GetInt32(3);
                
                cheeps.Add(new CheepViewModel(GetAuthorFromID(author_id), message, UnixTimeStampToDateTimeString(date)));
            }
        }
        return cheeps;
    }
    