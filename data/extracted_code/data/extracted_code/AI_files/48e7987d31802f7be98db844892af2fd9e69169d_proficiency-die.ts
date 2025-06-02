	/**
	 * Maps the value of the proficiency die to the corresponding array of `EdgeOfTheEmpireDiceSymbol` results.
	 *
	 * @returns {EdgeOfTheEmpireDiceSymbol[]} An array of `EdgeOfTheEmpireDiceSymbol` representing the result of the die roll.
	 *
	 * The mapping is as follows:
	 * - 1: Blank
	 * - 2, 3: Success
	 * - 4, 5: Success, Success
	 * - 6: Advantage
	 * - 7, 8, 9: Success, Advantage
	 * - 10, 11: Advantage, Advantage
	 * - 12: Triumph
	 * - Default: Empty array
	 */