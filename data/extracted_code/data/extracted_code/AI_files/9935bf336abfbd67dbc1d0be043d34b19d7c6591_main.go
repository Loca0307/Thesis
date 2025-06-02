func roll(dice string) int {
	matches := dicePattern.FindStringSubmatch(dice)
	if len(matches) != 3 {
		return 0
	}
	count, _ := strconv.Atoi(matches[1])
	sides, _ := strconv.Atoi(matches[2])
	sum := 0
	for i := 0; i < count; i++ {
		sum += 1 + rand.Intn(sides)
	}
	return sum