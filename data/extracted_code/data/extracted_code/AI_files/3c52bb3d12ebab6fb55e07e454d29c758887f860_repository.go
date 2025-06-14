
func NewServer() Server {
	db, err := gorm.Open(sqlite.Open("../tmp/minitwit.db"), &gorm.Config{})

	if err != nil {
		log.Fatalln("Could not open Database", err)
	}

	s := Server{
		r:  mux.NewRouter(),
		db: db,
	}

	return s
}

func (s *Server) StartServer() {
	log.Println("Starting server on port", port)
	log.Fatal(http.ListenAndServe(port, s.r))
}

func (s *Server) InitRoutes() error {
	repo := repository.CreateRepository(s.db)
	rH := handler.CreateRegisterHandler(repo)
	lH := handler.CreateLoginHandler(repo)

	s.r.Handle("/register", mw.Auth(http.HandlerFunc(rH.RegisterHandler)))
	s.r.Handle("/login", mw.Auth(http.HandlerFunc(lH.LoginHandler)))

	s.r.PathPrefix("/static/").Handler(http.StripPrefix("/static/", http.FileServer(http.Dir("web/static"))))

	// s.Get("/latest", s.LatestHandler)
	// s.Post("/sim/register", s.RegisterSimHandler)

	// s.Get("/msgs/{username}", s.GetUserMsgsHandler)
	// s.Post("/msgs/{username}", s.PostUserMsgsHandler)
	// s.Get("/msgs", s.MsgsHandler)
	// s.Get("/fllws/{username}", s.GetUserFollowsHandler)
	// s.Post("/fllws/{username}", s.PostUserFollowsHandler)

	return nil
}

func (s *Server) InitDB() error {
	err := s.db.AutoMigrate(
		&model.User{},
		&model.Follower{},
		&model.Message{},
	)
	return err
}