        public IActionResult CreateTestData()
        {
            Officer testOfficer7 = new Officer
            {
                Id = "7",
                Firstname = "Test",
                Lastname = "Officer7",
                PhoneNumber = "123-456-7890",
                Email = "testofficer7@example.com",
                SupervisorsOfOfficer = new List<Supervises>()
            };

            Officer testOfficer8 = new Officer
            {
                Id = "8",
                Firstname = "Test",
                Lastname = "Officer8",
                PhoneNumber = "123-456-7891",
                Email = "testofficer8@example.com",
                SupervisorsOfOfficer = new List<Supervises>()
            };

            Supervisor testSupervisor9 = new Supervisor
            {
                Id = "9",
                Firstname = "Test",
                Lastname = "Supervisor9",
                PhoneNumber = "123-456-7892",
                Email = "testsupervisor9@example.com",
                OfficersSupervised = new List<Supervises>()
            };

            Supervisor testSupervisor10 = new Supervisor
            {
                Id = "10",
                Firstname = "Test",
                Lastname = "Supervisor10",
                PhoneNumber = "123-456-7893",
                Email = "testsupervisor10@example.com",
                OfficersSupervised = new List<Supervises>()
            };

            // Establish the relationship between Officer 7 and Supervisor 9
            Supervises supervises = new Supervises
            {
                Officer = testOfficer7,
                Supervisor = testSupervisor9,
                StartDate = DateTime.Now
            };

            testOfficer7.SupervisorsOfOfficer.Add(supervises);
            testSupervisor9.OfficersSupervised.Add(supervises);

            // Add the test data to the database
            _database.Officer.Add(testOfficer7);
            _database.Officer.Add(testOfficer8);
            _database.Supervisor.Add(testSupervisor9);
            _database.Supervisor.Add(testSupervisor10);
            _database.Supervises.Add(supervises);
            _database.SaveChanges();

            return RedirectToAction("Index");
        }