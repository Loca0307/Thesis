
    public List<CheepDTO> GetCheepsNotBlocked(string userEmail)
    {
        var query = (from Author in _context.Authors
            join Cheeps in _context.Cheeps on Author.AuthorId equals Cheeps.AuthorId
            where !_context.Blocked.Any(b => b.User.Email == userEmail && b.BlockedUser.Email == Author.Email)
            orderby Cheeps.TimeStamp descending
            select new CheepDTO
            {
                Author = Author.Name,
                Email = Author.Email,
                Message = Cheeps.Text,
                TimeStamp = ((DateTimeOffset)Cheeps.TimeStamp).ToUnixTimeSeconds(),
                CheepId = Cheeps.CheepId
            });

        return query.ToList();
    }

    public List<CheepDTO> GetLiked(string email)
    {
        var query = (from Cheep in _context.Cheeps
            join Likes in _context.Likes on Cheep.CheepId equals Likes.cheep.CheepId
            orderby Cheep.TimeStamp descending
            where Likes.User.Email == email
            select new CheepDTO
            {
                CheepId = Cheep.CheepId,
                TimeStamp = ((DateTimeOffset)Cheep.TimeStamp).ToUnixTimeSeconds(),
                Author = Cheep.Author.Name,
                Message = Cheep.Text
            });

        return query.ToList();
    }

    public List<Cheep> GetCheep(string userEmail, int cheepId)
    {
        var query = (from Cheep in _context.Cheeps
            where Cheep.Author.Email == userEmail && Cheep.CheepId == cheepId
            select Cheep);

        return query.ToList();
    }

    public List<Cheep> GetCheepFromId(int cheepId)
    {
        var query = (from Cheep in _context.Cheeps
            where Cheep.CheepId == cheepId
            select Cheep);

        return query.ToList();
    }

    // Methods for adding and removing cheeps