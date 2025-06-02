        var schemaSQL = File.ReadAllText("data/schema.sql");
        ExecuteQuery(schemaSQL);

        var dumpSQL = File.ReadAllText("data/dump.sql");
        ExecuteQuery(dumpSQL);