    /// <summary>
    /// Initializes a new instance of the <see cref="UserTimelineModel"/> class.
    /// </summary>
    /// <param name="cheepService">The service that handles Cheep-related operations.</param>
    public UserTimelineModel(ICheepService cheepService) : base(cheepService)
    {
    }

    /// <summary>
    /// Handles the GET request to display the user's timeline along with their followers' posts.
    /// </summary>
    /// <param name="author">The username of the author whose timeline is being viewed.</param>
    /// <returns>An <see cref="ActionResult"/> representing the page result.</returns>