
    public List<Cheep> GetCheepsFromAuthorNameForPage(string authorName, int pageNumber)
    {
        return GetCheepsFromAuthorNameWithAuthors(authorName)
            .Skip((pageNumber - 1) * 32)
            .Take(32)//Refactor
            .ToList();
    }