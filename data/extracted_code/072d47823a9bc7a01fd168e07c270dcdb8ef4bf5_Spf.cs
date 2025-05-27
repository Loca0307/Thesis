    private readonly IServiceProvider _serviceProvider;
    private readonly List<ISpfPromptHandler> _handlers;
    private readonly ISpfExitor? _exitor;
    private readonly ISpfNoPromptMatchHandler? _noMatchHandler;
    private readonly SpfState _state = new();

    public Spf(string[] args, IServiceCollection services)
    {
        var serviceProvider = services.BuildServiceProvider();
        _serviceProvider = serviceProvider;
        _handlers = DiscoverHandlers(serviceProvider);
        _exitor = serviceProvider.GetService<ISpfExitor>();
        _noMatchHandler = serviceProvider.GetService<ISpfNoPromptMatchHandler>();
    }

    private static List<ISpfPromptHandler> DiscoverHandlers(IServiceProvider serviceProvider)
    {
        return [.. AppDomain.CurrentDomain.GetAssemblies()
            .SelectMany(a => a.GetTypes())
            .Where(t => typeof(ISpfPromptHandler).IsAssignableFrom(t) && !t.IsInterface && !t.IsAbstract)
            .Select(t => (ISpfPromptHandler)serviceProvider.GetRequiredService(t))];
    }

    public async Task StartAsync()
    {
        while (true)
        {
            Console.Write(" > ");
            var input = Console.ReadLine()?.Trim();
            if (string.IsNullOrEmpty(input)) continue;

            if (input.Equals("q", StringComparison.OrdinalIgnoreCase) || input.Equals("quit", StringComparison.OrdinalIgnoreCase))
            {
                if (_exitor != null && !await _exitor.ExitAsync(_state))
                    continue;
                break;
            }

            var tokens = input.Split(' ', StringSplitOptions.RemoveEmptyEntries);
            if (tokens.Length == 0) continue;

            var (path, cmdInput) = TokenizeInput(tokens);
            var handler = _handlers.FirstOrDefault(h => MatchesHandler(h, path));

            if (handler != null)
            {
                await handler.HandlePromptAsync(path, cmdInput, _state);
            }
            else if (_noMatchHandler != null && await _noMatchHandler.HandleNoMatch(tokens, _state))
            {
                continue;
            }
            else
            {
                Console.WriteLine("Error: Unrecognized command.");
            }
        }
    }

    private static (string[] path, string[] input) TokenizeInput(string[] tokens)
    {
        var lastIndex = tokens.ToList().FindLastIndex(t => char.IsUpper(t.FirstOrDefault()));
        if (lastIndex == -1) return (tokens, Array.Empty<string>());
        return (tokens[..(lastIndex + 1)], tokens[(lastIndex + 1)..]);
    }

    private static bool MatchesHandler(ISpfPromptHandler handler, string[] path)
    {
        var typeName = handler.GetType().Name;
        if (typeName.EndsWith("SpfPromptHandler"))
            typeName = typeName[..^15];