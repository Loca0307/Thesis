    [Fact]
    public async Task PostMessage_CreatesMessageSuccessfully()
    {
        // Arrange
        var context = fixture.GetDbContext(); // This should return a properly set up in-memory context

        var user = new User { Username = "Man", Email = "Man@test.com", PwHash = "hashedpassword" };
        await context.Users.AddAsync(user);
        await context.SaveChangesAsync();

        var content = "Hello from Man";
        
        // Act
        var response = await client.PostAsync("/msgs/Man", new FormUrlEncodedContent(new[] { new KeyValuePair<string, string>("content", content) }));

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.NoContent); // Expecting 204 No Content
        var savedMessage = await context.Messages.SingleOrDefaultAsync(m => m.AuthorId == user.UserId);
        savedMessage.Should().NotBeNull();
        savedMessage.Text.Should().Be(content);
    }
    