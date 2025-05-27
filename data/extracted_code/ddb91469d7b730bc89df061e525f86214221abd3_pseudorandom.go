func findMostCommon(nums []int) []int {
	countMap := make(map[int]int)
	maxCount := 0
	for _, num := range nums {
		countMap[num]++
		if countMap[num] > maxCount {
			maxCount = countMap[num]
		}
	}
	mostCommon := []int{}
	for num, count := range countMap {
		if count == maxCount {
			mostCommon = append(mostCommon, num)
		}
	}
	return mostCommon
}
