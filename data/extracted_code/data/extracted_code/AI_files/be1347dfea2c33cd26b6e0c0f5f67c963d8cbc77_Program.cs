    static string filePath = @"../../data/Chirp.CLI/chirp_cli_db.csv";
    IDatabaseRepository db = new CsvDatabase(filePath);
    static string userName = Environment.UserName;
    static long timestamp = DateTimeOffset.UtcNow.ToUnixTimeSeconds();
    static int count = 0;
    
    public record Cheep(string Author, string Message, long Timestamp);
        
    static void Main(string[] args)
    {
        try