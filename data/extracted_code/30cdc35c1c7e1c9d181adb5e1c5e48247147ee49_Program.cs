        public static void Main(string[] args)
        {
            try
            {
                switch (args[0])
                {
                    case "read":
                        Read();
                        break;

                    case "cheep":
                        CheepWrite(args.Skip(1).ToArray());
                        break;

                    default:
                        Console.WriteLine("Error: Invalid command.");
                        break;
                }
            }
            catch (IndexOutOfRangeException e)
            {
                Console.WriteLine("Error: " + e.Message);
                Console.WriteLine("It appears that you did not specify a command.");
                Console.WriteLine("* Try: read or cheep");