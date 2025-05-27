	usedNumbers := make([]bool, 10)
	letterToNumber := make(map[string]int)

	if solveBacktrack(&equation, letters, letterToNumber, usedNumbers, 0) {
		return letterToNumber, nil
	}
	return nil, errors.New("no solution found")
}

func solveBacktrack(equation *equation, letters []string, letterToNumber map[string]int, usedNumbers []bool, index int) bool {
	fmt.Printf("letters %v letterToNumber %v usedNumbers %v index %v\n", letters, letterToNumber, usedNumbers, index) // Debug statement
	if index == len(letters) {
		return equation.evaluate(letterToNumber)
	}

	for num := 0; num <= 9; num++ {
		if !usedNumbers[num] {
			letterToNumber[letters[index]] = num
			usedNumbers[num] = true

			fmt.Printf("Trying %s = %d\n", letters[index], num) // Debug statement
			fmt.Printf("Current map: %v\n", letterToNumber)     // Debug statement

			if !equation.isLeadingZero(letterToNumber) && solveBacktrack(equation, letters, letterToNumber, usedNumbers, index+1) {
				return true
			}

			usedNumbers[num] = false
			delete(letterToNumber, letters[index])