    
    private void WaitUntilServerIsAvailable(string url)
    {
        var uri = new Uri(url);
        using var client = new TcpClient();

        var maxAttempts = 5;
        var attempt = 0;

        while (attempt < maxAttempts)
        {
            try
            {
                client.Connect(uri.Host, uri.Port);
                if (client.Connected)
                {
                    break;
                }
            }
            catch
            {
                attempt++;
                Thread.Sleep(1000);
            }
        }

        if (attempt == maxAttempts)
        {
            throw new Exception("Server did not start in time.");
        }
    }