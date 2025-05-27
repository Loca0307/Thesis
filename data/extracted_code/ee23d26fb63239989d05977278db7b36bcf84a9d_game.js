class Game {
    constructor() {
        this.currentWord = '';
        this.maxAttempts = 6;
        this.currentAttempts = 0;
        this.guessedWords = [];
    }

    startGame() {
        this.currentWord = WordChecker.giveNewWord()
        console.log(this.currentWord)
        this.currentAttempts = 0;
        this.guessedWords = [];
        this.updateUI();
        this.setFeedback('New game started. Guess the word!');
    }

    guessWord(word) {
        if (this.currentAttempts >= this.maxAttempts) {
            this.setFeedback('No more attempts left!');
            return;
        }

        if (!WordChecker.isValidWord(word)) {
            this.setFeedback('Invalid word. Try again.');
            return;
        }

        this.guessedWords.push(this.generateFeedbackHTML(word));
        this.currentAttempts++;

        if (this.checkWin(word)) {
            this.updateUI();
            this.setFeedback('Congratulations! You guessed the word!');
        } else if (this.checkLoss()) {
            this.updateUI();
            this.setFeedback(`Game over! The word was ${this.currentWord}.`);
        } else {
            this.updateUI();
        }
    }

    checkWin(word) {
        if (word === this.currentWord) {
            document.getElementById('guessInput').style.display = 'none';
            document.getElementById('makeGuess').style.display = 'none';
            return true;
        }
        return false;
    }

    checkLoss() {
        if (this.currentAttempts >= this.maxAttempts) {
            document.getElementById('guessInput').style.display = 'none';
            document.getElementById('makeGuess').style.display = 'none';
            return true;
        }
        return false;
    }

    setFeedback(message) {
        document.getElementById('feedback').innerText = message;
    }

    updateUI() {
        document.getElementById('attemptsLeft').innerText = `${this.maxAttempts - this.currentAttempts} attempts left.`;
        document.getElementById('guessedWords').innerHTML = `Guessed Words:<br>${this.guessedWords.join('<br>')}`;
    }

    generateFeedbackHTML(word) {
        const feedback = WordChecker.compareWords(word, this.currentWord);
        let feedbackHTML = '';

        for (let i = 0; i < word.length; i++) {
            if (feedback[i] === word[i].toUpperCase()) {
                feedbackHTML += `<span class="correct">${word[i]}</span>`;
            } else if (feedback[i] === word[i].toLowerCase()) {
                feedbackHTML += `<span class="misplaced">${word[i]}</span>`;
            } else {
                feedbackHTML += `<span class="incorrect">${word[i]}</span>`;
            }
        }

        return feedbackHTML;
    }
}

class Player {
    constructor(name) {
        this.name = name;
        this.score = 0;
    }

    makeGuess(game, word) {
        game.guessWord(word);
    }
}

class WordChecker {
    constructor(wordList) {
        this.wordList = wordList;
    }

    static async loadWords() {
        try {
            const response = await fetch('words.txt');
            const text = await response.text();
            this.wordList = text.split('\n').map(word => word.trim()).filter(word => word.length === 5);
        } catch (error) {
            console.error('Error loading words:', error);
        }
    }

    static giveNewWord() {
        return this.wordList[Math.floor(Math.random() * this.wordList.length)];
    }

    static isValidWord(word) {
        if (this.wordList.includes(word)) {
            return true
        }
        return false;
    }

    static compareWords(guess, target) {
        let feedback = '';

        for (let i = 0; i < guess.length; i++) {
            if (guess[i] === target[i]) {
                feedback += guess[i].toUpperCase();
            } else if (target.includes(guess[i])) {
                feedback += guess[i].toLowerCase();
            } else {
                feedback += '_';
            }
        }

        return feedback;
    }
}

const game = new Game();
const wordList = new WordChecker()
const player = new Player('John');

function makeGuess() {
    const guessInput = document.getElementById('guessInput').value.toLowerCase();
    if (guessInput.length === 5) {
        player.makeGuess(game, guessInput);
        document.getElementById('guessInput').value = '';
    } else {
        game.setFeedback('Please enter a 5-letter word.');
    }
}

function resetGame() {
    document.getElementById('guessInput').style.display = 'inline';
    document.getElementById('guessInput').value = '';
    document.getElementById('makeGuess').style.display = 'inline';
    game.startGame();
}

window.onload = async () => {
    await WordChecker.loadWords();
    game.startGame();
}

document.getElementById('guessInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        makeGuess();
    }
});