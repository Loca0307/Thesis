    public async Task SetDarkMode(string name, bool isDarkMode)
    {
        var author = await _authorDb.Authors.FirstOrDefaultAsync(a => a.Name == name);
        if (author == null)
        {
            throw new ArgumentException($"Author {name} does not exist");
        }
        author.IsDarkMode = isDarkMode;
        await _authorDb.SaveChangesAsync();
    }
    
    public async Task<bool> IsDarkMode(string name)
    {
        var author = await _authorDb.Authors.FirstOrDefaultAsync(a => a.Name == name);
        if (author == null)
        {
            throw new ArgumentException($"Author {name} does not exist");
        }
        return author.IsDarkMode;
    }
    
    public async Task SetFontSizeScale(string name, int fontSizeScale)
    {
        var author = await _authorDb.Authors.FirstOrDefaultAsync(a => a.Name == name);
        if (author == null)
        {
            throw new ArgumentException($"Author {name} does not exist");
        }
        author.FontSizeScale = fontSizeScale;
        await _authorDb.SaveChangesAsync();
    }
    
    public async Task<int> GetFontSizeScale(string name)
    {
        var author = await _authorDb.Authors.FirstOrDefaultAsync(a => a.Name == name);
        if (author == null)
        {
            throw new ArgumentException($"Author {name} does not exist");
        }
        return author.FontSizeScale;
    }
    