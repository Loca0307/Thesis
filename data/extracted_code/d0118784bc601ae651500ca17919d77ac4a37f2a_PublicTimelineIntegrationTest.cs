
    [Fact]
    public async void FrontPageContains32Cheeps()
    {
        //Arrange & Act
        var rsp = await usableClient.GetAsync("/");
        string htmlContent = await rsp.Content.ReadAsStringAsync();

        //Parse the htmlContent to a HTMLDocument
        HtmlDocument doc = new HtmlDocument();
        doc.LoadHtml(htmlContent);

        int amountOfListItems = doc.DocumentNode.SelectNodes("//li").Count();

        Assert.Equal(32, amountOfListItems);
    }