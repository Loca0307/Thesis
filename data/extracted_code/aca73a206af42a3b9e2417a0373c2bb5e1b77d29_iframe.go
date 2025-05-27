	author, err := a.p.API.GetUser(post.UserId)
	if err != nil {
		a.p.API.LogError("Failed to get author", "user_id", post.UserId, "error", err.Error())
		http.Error(w, "failed to get author", http.StatusInternalServerError)
		return
	}

	channel, err := a.p.API.GetChannel(post.ChannelId)
	if err != nil {
		logrus.Errorf("failed to get channel for channel ID %s: %v", post.ChannelId, err)
		http.Error(w, fmt.Sprintf("failed to get channel: %v", err), http.StatusInternalServerError)
	}
