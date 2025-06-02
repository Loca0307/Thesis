
    [Fact]
    public async Task GetIterations_ReturnsTeamIterations()
    {
        // Arrange
        var projectId = Guid.NewGuid();
        var teamId = Guid.NewGuid();
        var expectedIterations = new TeamIterations
        {
            Value =
            [
                new TeamIterationSettings { Id = Guid.NewGuid(), Name = "Iteration 1" },
                new TeamIterationSettings { Id = Guid.NewGuid(), Name = "Iteration 2" }
            ]
        };

        _httpMessageHandlerMock.Protected()
            .Setup<Task<HttpResponseMessage>>(
                "SendAsync",
                ItExpr.IsAny<HttpRequestMessage>(),
                ItExpr.IsAny<CancellationToken>())
            .ReturnsAsync(new HttpResponseMessage
            {
                StatusCode = HttpStatusCode.OK,
                Content = JsonContent.Create(expectedIterations)
            });

        // Act
        var result = await _teamSettingsService.GetIterations(projectId, teamId);

        // Assert
        Assert.NotNull(result);
        Assert.Equal(expectedIterations.Value.Length, result.Value.Length);
        Assert.Equal(expectedIterations.Value[0].Name, result.Value[0].Name);
    }

    [Fact]
    public async Task GetIterations_ReturnsNull_WhenNotFound()
    {
        // Arrange
        var projectId = Guid.NewGuid();
        var teamId = Guid.NewGuid();

        _httpMessageHandlerMock.Protected()
            .Setup<Task<HttpResponseMessage>>(
                "SendAsync",
                ItExpr.IsAny<HttpRequestMessage>(),
                ItExpr.IsAny<CancellationToken>())
            .ReturnsAsync(new HttpResponseMessage
            {
                StatusCode = HttpStatusCode.NotFound
            });

        // Act & Assert
        await Assert.ThrowsAsync<HttpRequestException>(() => _teamSettingsService.GetIterations(projectId, teamId));
    }

    [Fact]
    public async Task GetIterations_ThrowsException_OnErrorResponse()
    {
        // Arrange
        var projectId = Guid.NewGuid();
        var teamId = Guid.NewGuid();

        _httpMessageHandlerMock.Protected()
            .Setup<Task<HttpResponseMessage>>(
                "SendAsync",
                ItExpr.IsAny<HttpRequestMessage>(),
                ItExpr.IsAny<CancellationToken>())
            .ReturnsAsync(new HttpResponseMessage
            {
                StatusCode = HttpStatusCode.InternalServerError
            });

        // Act & Assert
        await Assert.ThrowsAsync<HttpRequestException>(() => _teamSettingsService.GetIterations(projectId, teamId));
    }

    [Fact]
    public async Task CreateIteration_SendsCorrectRequest()
    {
        // Arrange
        var projectId = Guid.NewGuid();
        var teamId = Guid.NewGuid();
        var iterationId = Guid.NewGuid();

        _httpMessageHandlerMock.Protected()
            .Setup<Task<HttpResponseMessage>>(
                "SendAsync",
                ItExpr.IsAny<HttpRequestMessage>(),
                ItExpr.IsAny<CancellationToken>())
            .ReturnsAsync(new HttpResponseMessage
            {
                StatusCode = HttpStatusCode.Created
            });

        // Act
        var response = await _teamSettingsService.CreateIteration(projectId, teamId, iterationId);

        // Assert
        Assert.Equal(HttpStatusCode.Created, response.StatusCode);
        _httpMessageHandlerMock.Protected().Verify(
            "SendAsync",
            Times.Once(),
            ItExpr.Is<HttpRequestMessage>(req =>
                req.Method == HttpMethod.Post &&
                req.Content != null && req.Content.ReadAsStringAsync().Result.Contains(iterationId.ToString())),
            ItExpr.IsAny<CancellationToken>());
    }

    [Fact]
    public async Task CreateIteration_ThrowsException_OnErrorResponse()
    {
        // Arrange
        var projectId = Guid.NewGuid();
        var teamId = Guid.NewGuid();
        var iterationId = Guid.NewGuid();

        _httpMessageHandlerMock.Protected()
            .Setup<Task<HttpResponseMessage>>(
                "SendAsync",
                ItExpr.IsAny<HttpRequestMessage>(),
                ItExpr.IsAny<CancellationToken>())
            .ReturnsAsync(new HttpResponseMessage
            {
                StatusCode = HttpStatusCode.BadRequest
            });

        // Act
        var response = await _teamSettingsService.CreateIteration(projectId, teamId, iterationId);

        // Assert
        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
    }

    [Fact]
    public async Task DeleteIteration_SendsCorrectRequest()
    {
        // Arrange
        var projectId = Guid.NewGuid();
        var teamId = Guid.NewGuid();
        var iterationId = Guid.NewGuid();

        _httpMessageHandlerMock.Protected()
            .Setup<Task<HttpResponseMessage>>(
                "SendAsync",
                ItExpr.IsAny<HttpRequestMessage>(),
                ItExpr.IsAny<CancellationToken>())
            .ReturnsAsync(new HttpResponseMessage
            {
                StatusCode = HttpStatusCode.NoContent
            });

        // Act
        var response = await _teamSettingsService.DeleteIteration(projectId, teamId, iterationId);

        // Assert
        Assert.Equal(HttpStatusCode.NoContent, response.StatusCode);
        _httpMessageHandlerMock.Protected().Verify(
            "SendAsync",
            Times.Once(),
            ItExpr.Is<HttpRequestMessage>(req =>
                req.Method == HttpMethod.Delete &&
                req.RequestUri != null &&
                req.RequestUri.ToString().Contains($"{projectId}/{teamId}/_apis/work/teamsettings/iterations/{iterationId}?api-version=7.1")),
            ItExpr.IsAny<CancellationToken>());
    }

    [Fact]
    public async Task DeleteIteration_ThrowsException_OnErrorResponse()
    {
        // Arrange
        var projectId = Guid.NewGuid();
        var teamId = Guid.NewGuid();
        var iterationId = Guid.NewGuid();

        _httpMessageHandlerMock.Protected()
            .Setup<Task<HttpResponseMessage>>(
                "SendAsync",
                ItExpr.IsAny<HttpRequestMessage>(),
                ItExpr.IsAny<CancellationToken>())
            .ReturnsAsync(new HttpResponseMessage
            {
                StatusCode = HttpStatusCode.BadRequest
            });

        // Act
        var response = await _teamSettingsService.DeleteIteration(projectId, teamId, iterationId);

        // Assert
        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
    }
}