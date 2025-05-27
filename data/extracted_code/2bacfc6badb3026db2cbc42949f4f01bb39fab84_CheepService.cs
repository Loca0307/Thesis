        {
            Name = authors[0].Name,
            Email = authors[0].Email
        };
    }

    public void CreateAuthor(string name, string email)
    {
        _repository.CreateAuthor(name, email);
       