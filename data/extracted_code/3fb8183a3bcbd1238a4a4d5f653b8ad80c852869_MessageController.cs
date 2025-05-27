

    [IgnoreAntiforgeryToken]
    [HttpGet("msgs/{username}")]
    public async Task<IActionResult> GetFilteredMessages(string username)
    {
        int pageSize = 100;
        await latestService.UpdateLatest(1);
        
        var user = await db.Users.FirstOrDefaultAsync(u => u.Username == username);
        if (user == null)
        {
            return new JsonResult(new { status = 404, error_msg = "User does not exist!" })
            {
                StatusCode = 404
            };
        }
        
        var messages = await db.Messages
            .Where(m => m.AuthorId == user.UserId && m.Flagged == 0)
            .OrderByDescending(m => m.PubDate)
            .Take(pageSize)
            .Select(m => new 
            {
                content = m.Text,
                pub_date = m.PubDate,
                user = username
            })
            .ToListAsync();

        return Ok(messages);
    }