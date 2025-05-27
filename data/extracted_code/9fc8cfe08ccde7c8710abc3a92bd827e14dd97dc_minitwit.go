	loggedIn, _ := isUserLoggedIn(c)
    if !loggedIn {
        c.String(http.StatusUnauthorized, "Unauthorized")
    }
	text := c.FormValue("text")
	userId, err := getSessionUserID(c)
	if err != nil {
		fmt.Printf("getSessionUserID returned error: %v\n", err)
		return err
	}
	
	Db.Exec(`insert into message (author_id, text, pub_date, flagged)
			 values (?, ?, ?, 0)`,
			 userId, text, time.Now().Unix(),
	)

	err = addFlash(c, "Your message was recorded")
	if err != nil {
		fmt.Printf("addFlash returned error: %v\n", err)
	}

	return c.Redirect(http.StatusFound, "/")