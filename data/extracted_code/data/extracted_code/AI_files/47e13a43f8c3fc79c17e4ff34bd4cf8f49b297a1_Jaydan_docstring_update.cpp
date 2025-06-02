// Old undocumented code
void placeRandomPiece(int gameBoard[BOARD_HEIGHT][BOARD_WIDTH], bool& startOfGame)
{
	srand(time(0));

	if(startOfGame == true)
	{
		for(int i = 0; i < 2; i++)
		{
			int row = rand() % 4;
			int column = rand() % 4;

			if(gameBoard[row][column] == EMPTY)
			{
				gameBoard[row][column] = 1;
				continue;
			}
			else
			{
				continue;
			}
		}
		startOfGame = false;
	}
	else
	{
		do
		{
			int row = rand() % 4;
			int column = rand() % 4;

			if(gameBoard[row][column] == EMPTY)
			{
				gameBoard[row][column] = 1;
				break;
			}
			else
			{
				continue;
			}
		} while(true);
	}

	
}


// New documented code
void placeRandomPiece(int gameBoard[BOARD_HEIGHT][BOARD_WIDTH], bool& startOfGame)
{
    // Seed the random number generator with the current time to ensure different outputs each run
    srand(time(0));

    // Check if it's the start of the game
    if(startOfGame == true)
    {
        // At the beginning of the game, place two pieces randomly on the board
        for(int i = 0; i < 2; i++)
        {
            int row = rand() % 4;    // Generate a random row index (0 to 3)
            int column = rand() % 4; // Generate a random column index (0 to 3)

            // Check if the chosen position is empty
            if(gameBoard[row][column] == EMPTY)
            {
                gameBoard[row][column] = 1; // Place a new tile with the value 1
                continue; // Continue to the next piece placement
            }
            else
            {
                continue; // If the position is occupied, try again in the next loop iteration
            }
        }
        // After placing the initial two pieces, set startOfGame to false
        startOfGame = false;
    }
    else
    {
        // During normal gameplay, place a single piece in a random empty spot
        do
        {
            int row = rand() % 4;    // Generate a random row index
            int column = rand() % 4; // Generate a random column index

            // Check if the chosen position is empty
            if(gameBoard[row][column] == EMPTY)
            {
                gameBoard[row][column] = 1; // Place a new tile with the value 1
                break; // Exit the loop once a piece is placed successfully
            }
            else
            {
                continue; // If the position is occupied, retry until a valid position is found
            }
        } while(true); // Infinite loop until a valid placement is made
    }
}