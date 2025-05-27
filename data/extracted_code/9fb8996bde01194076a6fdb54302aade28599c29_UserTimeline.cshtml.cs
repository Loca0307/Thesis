    public async Task<ActionResult> OnPostLike(string authorDto, string text, string timeStamp, int? likes)
    {
        // Find the author that's logged in
        var authorName = User.FindFirst("Name")?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException("Author name cannot be null or empty.");
        }

        var author = await AuthorRepository.FindAuthorWithName(authorName);
        var cheep = await CheepRepository.FindCheep(text,timeStamp, authorDto);
        
        // Adds the cheep to the author's list of liked cheeps
        await CheepRepository.LikeCheep(cheep, author);
        
        likedCheeps = await AuthorRepository.getLikedCheeps(author.AuthorId);
        
        return RedirectToPage();
    }

    
    public async Task<ActionResult> OnPostUnLike(string authorDto, string text, string timeStamp, int? likes)
    {
        // Find the author that's logged in
        var authorName = User.FindFirst("Name")?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException("Author name cannot be null or empty.");
        }

        var author = await AuthorRepository.FindAuthorWithName(authorName);
        var cheep = await CheepRepository.FindCheep(text,timeStamp,authorDto);
        
        await CheepRepository.UnLikeCheep(cheep, author);
        
        likedCheeps = await AuthorRepository.getLikedCheeps(author.AuthorId);
        
        return RedirectToPage();
    }

    public async Task<bool> DoesUserLikeCheep(string authorDto, string text, string timeStamp)
    {
        var authorName = User.FindFirst("Name")?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException("Author name cannot be null or empty.");
        }
        
        var author = await AuthorRepository.FindAuthorWithLikes(authorName);
        var cheep = await CheepRepository.FindCheep(text,timeStamp,authorDto);
        
        return await  CheepRepository.DoesUserLikeCheep(cheep, author);
    }
    