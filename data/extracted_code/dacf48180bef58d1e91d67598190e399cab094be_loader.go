
func (tc *OLAPControllerImpl) sample(workflowRunID string) bool {
	if tc.samplingHashThreshold == nil {
		return true
	}

	bucket := hashToBucket(workflowRunID, 100)

	return int64(bucket) < *tc.samplingHashThreshold
}

func hashToBucket(workflowRunID string, buckets int) int {
	hasher := fnv.New32a()
	idBytes := []byte(workflowRunID)
	hasher.Write(idBytes)
	return int(hasher.Sum32()) % buckets
}