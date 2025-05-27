                IDatabase<Cheep> db = new CSVDatabase<Cheep>();
                //Read cheeps
                if (options.CheepCount != null)
                {

                    var cheeps = db.Read(options.CheepCount.Value);
                    UserInterface.PrintCheeps(cheeps);
                }

                //Cheep a cheep
                if (!string.IsNullOrWhiteSpace(options.CheepMessage))
                {

                    string Author = Environment.UserName;
                    string Message = options.CheepMessage;
                    long Timestamp = DateTimeOffset.UtcNow.ToUnixTimeSeconds();

                    db.Store(new Cheep(Author, Message, Timestamp));

                    UserInterface.PrintMessage($"Cheeped a cheep! The cheep is: {options.CheepMessage}");
                }
