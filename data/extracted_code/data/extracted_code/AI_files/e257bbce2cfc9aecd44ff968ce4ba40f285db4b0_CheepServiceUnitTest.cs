    public static async Task<AuthorDTO[]> SetUpTestAuthorDB(IAuthorRepository authorRepository, SqliteConnection connection)
    {
        using (var command = new SqliteCommand("DELETE FROM authors;", connection))
        {
            command.ExecuteNonQuery();
        }

        AuthorDTO[] authors = new AuthorDTO[4];
        for (int i = 0; i < authors.Length; i++)
        {
            authors[i] = new AuthorDTO
            {
                Id = i+1,
                Name = $"Test{i+1}",
                Email = $"Test{i+1}@Tester.com"
            };
            authors[i].Id = await authorRepository.AddAuthorAsync(authors[i]);
        }

        return authors;

    }
    public static async Task<CheepDTO[]> SetUpTestCheepDB(ICheepRepository cheepRepository, SqliteConnection connection, AuthorDTO[] authors)
    {
        using (var command = new SqliteCommand("DELETE FROM cheeps;", connection))
        {
            command.ExecuteNonQuery();
        }

        DateTime timeStamp = DateTime.Now;
        long timeStampLong = timeStamp.Ticks;
        CheepDTO[] cheeps = new CheepDTO[160];
        for (int i = 0; i < cheeps.Length; i++)
        {
            timeStampLong += 10000000;
            timeStamp = new DateTime(timeStampLong);
            cheeps[i] = new CheepDTO
            {
                Id = i + 1,
                Name = authors[i % authors.Length].Name,
                Message = $"Text{i + 1}",
                TimeStamp = timeStamp.ToString("yyyy\\-MM\\-dd HH\\:mm\\:ss"),
                AuthorId = authors[i % authors.Length].Id
            };
            cheeps[i].Id = await cheepRepository.AddCheepAsync(cheeps[i]);
        }

        Array.Reverse(cheeps);
        return cheeps;

    }


    public static void AssertCheep(CheepDTO expected, CheepDTO actual)
    {
        Assert.Equal(expected.Id, actual.Id);
        Assert.Equal(expected.Name, actual.Name);
        Assert.Equal(expected.TimeStamp, actual.TimeStamp);
        Assert.Equal(expected.AuthorId, actual.AuthorId);
        Assert.Equal(expected.Message, actual.Message);