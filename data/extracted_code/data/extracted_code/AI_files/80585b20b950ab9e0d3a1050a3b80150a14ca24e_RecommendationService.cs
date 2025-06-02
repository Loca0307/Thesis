    
    public async Task EvaluateHoldoutAsync(float testFraction = 0.2f)
    {
        // 1) Fetch & filter
        var allRatings = await _db.Ratings
            .Select(r => new RatingInput {
                UserName = r.UserName,
                MovieId  = r.MovieId,
                Score    = r.Score
            })
            .ToListAsync();
        var popularMovieIds = allRatings
            .GroupBy(r => r.MovieId)
            .Where(g => g.Count() >= 5)
            .Select(g => g.Key)
            .ToHashSet();
        var filtered = allRatings
            .Where(r => popularMovieIds.Contains(r.MovieId))
            .ToList();

        // 2) Apply the same weighting‐by‐duplication
        var weighted = new List<RatingInput>();
        foreach (var r in filtered)
        {
            weighted.Add(r);
            if (r.Score <= 2 || r.Score >= 9)
                weighted.Add(r);
        }

        // 3) Split train/test
        var dataView = _mlContext.Data.LoadFromEnumerable(weighted);
        var split    = _mlContext.Data.TrainTestSplit(dataView, testFraction: testFraction);
        var trainSet = split.TrainSet;
        var testSet  = split.TestSet;

        // 4) Train & evaluate
        var pipeline = _mlContext.Transforms
            .Conversion.MapValueToKey("userKey", nameof(RatingInput.UserName))
            .Append(_mlContext.Transforms
                .Conversion.MapValueToKey("movieKey", nameof(RatingInput.MovieId)))
            .Append(_mlContext.Recommendation()
                .Trainers.MatrixFactorization(new MatrixFactorizationTrainer.Options
                {
                    MatrixColumnIndexColumnName = "userKey",
                    MatrixRowIndexColumnName    = "movieKey",
                    LabelColumnName             = "Label",
                    NumberOfIterations          = 30,
                    ApproximationRank           = 150,
                    Lambda                      = 0.1
                }));
        var model   = pipeline.Fit(trainSet);
        var preds   = model.Transform(testSet);
        var metrics = _mlContext.Regression.Evaluate(preds, "Label", "Score");

        Console.WriteLine($"=== Hold-out (weighted+filtered) {1-testFraction:P0}/{testFraction:P0} ===");
        Console.WriteLine($"  RMSE = {metrics.RootMeanSquaredError:F3}");
        Console.WriteLine($"  MAE  = {metrics.MeanAbsoluteError:F3}");
        Console.WriteLine($"  R²   = {metrics.RSquared:F3}");
    }