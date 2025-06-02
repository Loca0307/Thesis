        private string _filePath;

        public CsvDatabase(string filePath)
        {
            _filePath = filePath;
        }

        public void AddCheep(Cheep cheep)
        {
            using (var sw = new StreamWriter(_filePath, append: true))
            using (var csv = new CsvWriter(sw, CultureInfo.InvariantCulture))
            {
                csv.WriteRecord(cheep);
                sw.WriteLine();
            }
        }

        public List<String> GetCheeps()
        {
            List<string> cheepsList = new List<string>();

            using (StreamReader sr = new StreamReader(_filePath))
            using (var csv = new CsvReader(sr, CultureInfo.InvariantCulture))
            {
                while (csv.Read())
                {
                    var cheep = csv.GetRecord<Cheep>();
                    cheepsList.Add($"{cheep.Author} @ {TimeStampConversion(cheep.Timestamp)}: {cheep.Message}");
                }
            }

            return cheepsList;
        }
        static string TimeStampConversion(long unix)
        {
            DateTimeOffset dto = DateTimeOffset.FromUnixTimeSeconds(unix);
            string Date = dto.ToString("dd/MM/yyyy HH:mm:ss");
            return Date;
        }