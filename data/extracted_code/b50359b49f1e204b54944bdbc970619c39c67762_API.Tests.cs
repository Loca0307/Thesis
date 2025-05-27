
    [Fact]
    public async Task GetFilteredMessages_returnsFilteredMessages()
    {
        var context = fixture.GetDbContext();
        var user = new User { Username = "Man", Email = "Man@Man.com", PwHash = "23456" };
    
        var msg = new Message { AuthorId = user.UserId, Text = "Hello from Man", PubDate = (int)DateTimeOffset.Now.ToUnixTimeSeconds() };
        var msg2 = new Message { AuthorId = user.UserId, Text = "Hello again from Man", PubDate = (int)DateTimeOffset.Now.ToUnixTimeSeconds() };

        await context.Users.AddAsync(user);
        await context.Messages.AddAsync(msg);
        await context.Messages.AddAsync(msg2);

        await context.SaveChangesAsync();

        var response = await client.GetAsync("/msgs/Man");
        var json = await response.Content.ReadAsStringAsync();
        

        if (response.StatusCode == HttpStatusCode.OK)
        {
            var messagesResponse = JsonConvert.DeserializeObject<MessagesResponse>(json);
            var messages = messagesResponse.Messages; // Access the messages

            foreach (var message in messages)
            {
                message.User.Should().Be(user.Username);
            }
        }
    }
    
    
    [Fact]
    public async Task GetFilteredMessagesFromNonExistentUser_returnsErrorResponse()
    {
        var context = fixture.GetDbContext();
        
        var response = await client.GetAsync("/msgs/MysteryMan");
        
        Assert.Equal(HttpStatusCode.NotFound, response.StatusCode);
        
            
    }
    
    
    [Fact]
    public async Task GetEmptyFilteredMessages_returnsErrorResponse()
    {
        var context = fixture.GetDbContext();
        var user = new User { Username = "Man", Email = "Man@Man.com", PwHash = "23456" };

        await context.Users.AddAsync(user);
        await context.SaveChangesAsync();

        var response = await client.GetAsync("/msgs/Man");
        
        Assert.Equal(HttpStatusCode.NoContent, response.StatusCode);
    }
    
    
    public class MessageDto
    {
        public string Text { get; set; }
        public int PubDate { get; set; }
        public string User { get; set; }
    }
    
    public class MessagesResponse
    {
        public string Status { get; set; }
        public List<MessageDto> Messages { get; set; }
    }