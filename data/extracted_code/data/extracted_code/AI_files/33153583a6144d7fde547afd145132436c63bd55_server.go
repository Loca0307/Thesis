	s.listObjectsCheckResolver, s.listObjectsCheckResolverCloser, err = graph.NewOrderedCheckResolvers([]graph.CheckResolverOrderedBuilderOpt{
		graph.WithLocalCheckerOpts([]graph.LocalCheckerOption{
			graph.WithResolveNodeBreadthLimit(s.resolveNodeBreadthLimit),
			graph.WithOptimizations(s.IsExperimentallyEnabled(ExperimentalListObjectsOptimizations)),
			graph.WithMaxResolutionDepth(s.resolveNodeLimit),
		}...),
		graph.WithLocalShadowCheckerOpts([]graph.LocalCheckerOption{
			graph.WithResolveNodeBreadthLimit(s.resolveNodeBreadthLimit),
			graph.WithOptimizations(true),
			graph.WithMaxResolutionDepth(s.resolveNodeLimit),
		}...),
		graph.WithShadowResolverEnabled(s.shadowListObjectsCheckResolverEnabled),
		graph.WithShadowResolverOpts([]graph.ShadowResolverOpt{
			graph.ShadowResolverWithName("list-objects"),
			graph.ShadowResolverWithLogger(s.logger),
			graph.ShadowResolverWithSamplePercentage(s.shadowListObjectsCheckResolverSamplePercentage),
			graph.ShadowResolverWithTimeout(s.shadowListObjectsCheckResolverTimeout),
		}...),
		graph.WithCachedCheckResolverOpts(s.cacheSettings.ShouldCacheCheckQueries(), checkCacheOptions...),
		graph.WithDispatchThrottlingCheckResolverOpts(s.checkDispatchThrottlingEnabled, checkDispatchThrottlingOptions...),
	}...).Build()
	if err != nil {
		return nil, err
	}
