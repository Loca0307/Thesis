    let gameBoard = Array(9).fill(null);
    let currentPlayer = 'X';
    let gameOver = false;
    let winner = null;
    let moveCount = 0;
    const winningCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6] // Diagonals
    ];
    const players = {
        X: { name: 'Player 1', symbol: 'X' },
        O: { name: 'Player 2', symbol: 'O' }
    };
    const gameStatus = {
        getCurrentPlayer: () => currentPlayer,
        getGameOver: () => gameOver,
        getWinner: () => winner,
        getMoveCount: () => moveCount,
        getGameBoard: () => gameBoard.slice(),
        getPlayers: () => players
    };
    const gameActions = {
        makeMove: (index) => {
            if (gameOver || gameBoard[index] !== null) return false;
            gameBoard[index] = currentPlayer;
            moveCount++;
            if (checkWinner()) {
                gameOver = true;
            } else if (moveCount === 9) {
                gameOver = true; // Draw
            } else {
                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            }
            return true;
        },
        resetGame: () => {
            gameBoard.fill(null);
            currentPlayer = 'X';
            gameOver = false;
            winner = null;
            moveCount = 0;
        }
    };
    function checkWinner() {
        for (const combination of winningCombinations) {
            const [a, b, c] = combination;
            if (gameBoard[a] && gameBoard[a] === gameBoard[b] && gameBoard[a] === gameBoard[c]) {
                winner = gameBoard[a];
                return true;
            }
        }
        return false;
    }
    return { gameStatus, gameActions }; 
}

// Example usage:
const ticTacToe = createGame();
console.log(ticTacToe.gameStatus.getGameBoard()); // Initial empty board
ticTacToe.gameActions.makeMove(0); // Player X makes a move     
console.log(ticTacToe.gameStatus.getGameBoard()); // Board after move
ticTacToe.gameActions.makeMove(1); // Player O makes a move
console.log(ticTacToe.gameStatus.getGameBoard()); // Board after move
ticTacToe.gameActions.makeMove(3); // Player X makes a move
console.log(ticTacToe.gameStatus.getGameBoard()); // Board after move
ticTacToe.gameActions.makeMove(4); // Player O makes a move
console.log(ticTacToe.gameStatus.getGameBoard()); // Board after move
ticTacToe.gameActions.makeMove(6); // Player X makes a move
console.log(ticTacToe.gameStatus.getGameBoard()); // Board after move
ticTacToe.gameActions.makeMove(7); // Player O makes a move
console.log(ticTacToe.gameStatus.getGameBoard()); // Board after move
ticTacToe.gameActions.makeMove(8); // Player X makes a move
console.log(ticTacToe.gameStatus.getGameBoard()); // Board after move
console.log(ticTacToe.gameStatus.getWinner()); // Check winner
console.log(ticTacToe.gameStatus.getGameOver()); // Check if game is over
ticTacToe.gameActions.resetGame(); // Reset the game
console.log(ticTacToe.gameStatus.getGameBoard()); // Board after reset
console.log(ticTacToe.gameStatus.getCurrentPlayer()); // Check current player after reset
console.log(ticTacToe.gameStatus.getMoveCount()); // Check move count after reset
console.log(ticTacToe.gameStatus.getPlayers()); // Check players information
// This code implements a simple Tic Tac Toe game using factory functions.
// It allows two players to take turns making moves, checks for a winner, and provides methods to reset the game.