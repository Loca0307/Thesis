        [Test]
        public async Task End_To_End_Test()
        {
            // Arrange
            var username = Faker.Name.First();
            var email = Faker.Internet.Email();
            var password = $"{Faker.Name.First()}!{Faker.Name.Last()}{Faker.RandomNumber.Next()}";
            var message = Faker.Lorem.Sentence();
            await Page.GotoAsync(_factory.GetBaseAddress());

            // Act
            // Register
            await Page.GetByRole(AriaRole.Link, new() { Name = "register", Exact = true }).ClickAsync();
            await Page.GetByPlaceholder("name@example.com").ClickAsync();
            await Page.GetByPlaceholder("name@example.com").FillAsync(email);
            await Page.GetByPlaceholder("name", new() { Exact = true }).ClickAsync();
            await Page.GetByPlaceholder("name", new() { Exact = true }).FillAsync(username);
            await Page.GetByLabel("Password", new() { Exact = true }).ClickAsync();
            await Page.GetByLabel("Password", new() { Exact = true }).FillAsync(password);
            await Page.GetByLabel("Confirm Password").ClickAsync();
            await Page.GetByLabel("Confirm Password").FillAsync(password);
            await Page.GetByRole(AriaRole.Button, new() { Name = "Register" }).ClickAsync();

            // Assert
            // Should be logged in
            await Expect(Page.GetByRole(AriaRole.Heading, new() { Name = $"What's on your mind {username}?" })).ToBeVisibleAsync();

            // Act
            // Post Cheep
            await Page.Locator("#Message").ClickAsync();
            await Page.Locator("#Message").FillAsync(message);
            await Page.GetByRole(AriaRole.Button, new() { Name = "Share" }).ClickAsync();

            // Assert
            // Cheep should be visible
            var postLocator = Page.Locator("li").Filter(new() { HasText = $"{username}" }).First;
            await Expect(postLocator).ToHaveTextAsync(new Regex($".*{message}.*"));

            // Act
            // Follow
            var posterToFollow = Page.Locator("li").Filter(new() { HasText = "Follow 0" }).GetByRole(AriaRole.Button).Nth(1);
            var posterToFollowUsername = await posterToFollow.TextContentAsync();
            await posterToFollow.ClickAsync();

            Console.WriteLine($"Text: {posterToFollowUsername}");

            // Assert
            // Should be following
            await Expect(Page.GetByRole(AriaRole.Button, new() { Name = "Unfollow" })).ToBeVisibleAsync();
            await Expect(Page).ToHaveURLAsync(new Regex($".*{posterToFollowUsername}"));

            // Act
            // Unfollow

            await Page.GetByRole(AriaRole.Button, new() { Name = "Unfollow" }).ClickAsync();

            // Assert
            // Should be unfollowed
            await Expect(Page.GetByRole(AriaRole.Button, new() { Name = "Follow" })).ToBeVisibleAsync();

            // Act
            // Like a post
            await Page.GetByRole(AriaRole.Link, new() { Name = "public timeline" }).ClickAsync();
            var postToLike = Page.Locator("li").Filter(new() { HasText = "♡" }).First;
            var likeButton = postToLike.GetByRole(AriaRole.Button, new() { Name = "♡" });
            await likeButton.ClickAsync();

            // Assert
            // Should be liked
            await Expect(Page.GetByRole(AriaRole.Button, new() { Name = "♥" })).ToBeVisibleAsync();
            await Expect(postToLike).ToHaveTextAsync(new Regex(@".*1.*"));

            // Act
            // Unlike a post
            await Page.GetByRole(AriaRole.Button, new() { Name = "♥" }).ClickAsync();

            // Assert
            // Should be unliked
            await Expect(postToLike.GetByRole(AriaRole.Button, new() { Name = "♡" })).ToBeVisibleAsync();
            await Expect(postToLike).ToHaveTextAsync(new Regex(@".*0.*"));

            // Act  
            // Logout

            await Page.GetByRole(AriaRole.Link, new() { Name = $"logout [{username}]" }).ClickAsync();

            // Assert
            // Should be logged out
            await Expect(Page.GetByRole(AriaRole.Link, new() { Name = "login" })).ToBeVisibleAsync();
        }