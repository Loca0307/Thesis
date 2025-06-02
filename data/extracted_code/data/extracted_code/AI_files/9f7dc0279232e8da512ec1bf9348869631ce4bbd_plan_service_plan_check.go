	if project.Setting.GetCiSamplingSize() > 0 {
		var updatedRuns []*store.PlanCheckRunMessage
		countMap := make(map[string]int32)
		for _, run := range planCheckRuns {
			key := fmt.Sprintf("%s/%s/%s/%d", run.Type, run.Config.GetInstanceId(), run.Config.GetDatabaseName(), run.Config.GetSheetUid())
			if countMap[key] >= project.Setting.GetCiSamplingSize() {
				continue
			}
			updatedRuns = append(updatedRuns, run)
			countMap[key]++
		}
		planCheckRuns = updatedRuns
	}