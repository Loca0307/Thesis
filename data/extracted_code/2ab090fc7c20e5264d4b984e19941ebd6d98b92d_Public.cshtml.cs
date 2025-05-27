
    public async Task<ActionResult> OnPostLike(CheepDTO cheepDto)
    {
        //Finds the author thats logged in
        var authorName = User.FindFirst(ClaimTypes.Name)?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException("Author name cannot be null or empty.");
        }
        
        var author = await _authorRepository.FindAuthorWithEmail(authorName);
        var cheep = await _cheepRepository.GetCheepFromCheepDto(cheepDto);
        
        //adds the cheep to the authors list of liked cheeps
        if (author.LikedCheeps != null)
        {
            author.LikedCheeps.Add(cheep);
        }
        
        cheepDto.Likes = cheepDto.Likes + 1;
        
        likedCheeps = await _authorRepository.getLikedCheeps(author.AuthorId);
        
        return RedirectToPage();
    }
    
    public async Task<ActionResult> OnPostUnLike(CheepDTO cheepDto)
    {
        //Finds the author thats logged in
        var authorName = User.FindFirst(ClaimTypes.Name)?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException("Author name cannot be null or empty.");
        }
        
        var author = await _authorRepository.FindAuthorWithEmail(authorName);
        var cheep = await _cheepRepository.GetCheepFromCheepDto(cheepDto);
        
        //removes the cheep from the user's unlikes from their list of liked cheeps
        if (author.LikedCheeps != null)
        {
            author.LikedCheeps.Remove(cheep);
        }

        cheepDto.Likes = cheepDto.Likes - 1;
        
        likedCheeps = await _authorRepository.getLikedCheeps(author.AuthorId);
        
        return RedirectToPage();
    }

    public async Task<bool> UserLikesCheep(CheepDTO cheepDto)
    {
        //Finds the author thats logged in
        var authorName = User.FindFirst(ClaimTypes.Name)?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException("Author name cannot be null or empty.");
        }
        
        var author = await _authorRepository.FindAuthorWithEmail(authorName);
        var cheep = await _cheepRepository.GetCheepFromCheepDto(cheepDto);
        
        return await  _cheepRepository.DoesUserLikeCheep(cheep, author);
    }