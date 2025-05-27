        Cheeps = _cheepRepository.GetCheepsFromPage(CurrentPage);

        // Set follow status for each cheep author
        if (User.Identity?.IsAuthenticated == true)
        {
            foreach (var cheep in Cheeps)
            {
                var authorName = cheep.AuthorName;
                var isFollowing = _followerRepository
                    .GetFollowersFromAuthor(authorName)
                    .Any(follower => follower.Name == User.Identity.Name);

                FollowStatus[authorName] = isFollowing;
            }
        }
