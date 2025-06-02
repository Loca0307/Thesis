
    [Fact]
    public async Task RegisterNewUserTest()
    {
        // Arrange
        var client = _factory.CreateClient();
        
        var getResponse = await client.GetAsync("/Identity/Account/Register");
        var getContent = await getResponse.Content.ReadAsStringAsync();
        

        // Step 2: Parse the anti-forgery token from the page content
        var tokenValue = ExtractAntiForgeryToken(getContent);
        
        var registerData = new Dictionary<string, string>
        {
            {"Input.Email","testuser@gmail.com"},
            {"Input.Password","Test@12345"}, 
            {"Input.ConfirmPassword","Test@12345"},
            { "__RequestVerificationToken", tokenValue},
            {"returnUrl","/"}
        };
        
        // Act
        var response = await client.PostAsync("/Identity/Account/Register", new FormUrlEncodedContent(registerData));
        
        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK); // Expecting HTTP 200
        var responseBody = await response.Content.ReadAsStringAsync();
        responseBody.Should().Contain("Register confirmation"); 
    }
    
    [Fact]
    public async Task LoginUserTest()
    {
        // Arange 
        //var client = _factory.CreateClient();
        
        //var getResponse = await client.GetAsync("/Identity/Account/Login");
        //var 
    }
    
    // Helper method to extract anti forgery token
    private string ExtractAntiForgeryToken(string htmlContent)
    {
        // Updated regex pattern for finding the anti-forgery token value
        var match = Regex.Match(htmlContent, @"<input[^>]*name=""__RequestVerificationToken""[^>]*value=""([^""]+)""", RegexOptions.IgnoreCase);
        if (!match.Success)
        {
            throw new InvalidOperationException("Anti-forgery token not found");
        }
        return match.Groups[1].Value;
    }
