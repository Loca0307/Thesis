		if (LoggedInAuthorUsername == null || AuthorToFollowUsername == null) {
			throw new ArgumentNullException("Usernames null");
		}
		Author LoggedInAuthor = GetAuthorFromUsername(LoggedInAuthorUsername);
		Author AuthorToFollow = GetAuthorFromUsername(AuthorToFollowUsername);
		if (LoggedInAuthor.Follows.Contains(AuthorToFollow))