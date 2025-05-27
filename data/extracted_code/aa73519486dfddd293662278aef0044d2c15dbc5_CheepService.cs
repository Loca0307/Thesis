
    public async Task<(byte[] FileData, string ContentType, string FileName)> DownloadAuthorInfo(Author author)
    {
        var name = author.UserName;
        var email = author.Email;
        
        // var followingList = await GetFollowingAuthorsAsync(name);
        // var userCheeps = await cheepRepository.ReadCheeps(-1, 0, );
        
        // Create the textfile
        var content = new StringBuilder();
        content.AppendLine($"{name}'s information:");
        content.AppendLine($"-----------------------");
        content.AppendLine($"Name: {name}");
        content.AppendLine($"Email: {email}");
        
        content.AppendLine("Following:");
        if (author.FollowingList != null && author.FollowingList.Count != 0)
        {
            foreach (var following in author.FollowingList)
            {
                content.AppendLine($"- {following.UserName}");
            }
        }
        else content.AppendLine("- No following");
        
        content.AppendLine("Cheeps:");
        if (author.Cheeps != null && author.Cheeps.Count != 0)
        {
            foreach (var cheep in author.Cheeps)
            {
                content.AppendLine($"- \"{cheep.Text}\" ({cheep.TimeStamp})");
            }
        }
        else content.AppendLine("- No Cheeps posted yet");

        // Convert content into bytes and return file
        var fileBytes = Encoding.UTF8.GetBytes(content.ToString());
        const string contentType = "text/plain";
        var fileName = $"{name}_Chirp_data.txt";
        return (fileBytes, contentType, fileName);
    }