    public async Task<List<Cheep>> GetAllCheepsFromFollowed(string author) //Made with the help of ChatGPT
    {
        var query = from cheep in _context.Cheeps
            where (from follow in _context.Follows
                    where follow.FollowsAuthorName == author
                    select follow.FollowsAuthorName)
                .Contains(cheep.Author.Name)
            select cheep;
        var result = await query.ToListAsync();
        return result;
    }
    