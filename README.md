# Hangman Game

This Python project implements the classic word-guessing game, Hangman. In this game, players try to guess a hidden word by suggesting letters within a certain number of attempts. With each incorrect guess, a part of the hangman is drawn, representing how many attempts remain before the game ends.

## Features

- **Word Selection**: The game randomly selects a word from a predefined list of words for the player to guess.
- **Interactive Gameplay**: Players can input their guesses through the command line interface.
- **Visual Feedback**: As players make guesses, the game provides visual feedback on the progress of the hangman drawing and displays the current state of the word with correctly guessed letters revealed.
- **Game Over Conditions**: The game ends when the player successfully guesses the word or runs out of attempts, resulting in a loss.

## How to Play

1. Run the Python script (`HangMan Game.py`) to start the game.
2. The game will randomly select a word from the word list and display a series of underscores representing each letter of the word.
3. Enter a letter guess at the prompt.
4. If the letter is correct, it will be revealed in the word. If incorrect, a part of the hangman will be drawn.
5. Continue guessing letters until you either successfully guess the word or run out of attempts.

## Word List

The word list used in the game can be customized by editing the `HangManGameWordList.py` file. Each word should be on a separate line.

## Contributing

Contributions to the Hangman project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code for personal or commercial purposes.

## Acknowledgments

- Inspired by the classic Hangman game, this project aims to provide a fun and interactive experience for players.
- Thanks to the Python community for providing resources and libraries to facilitate game development.

## Contact

For any questions or inquiries about the Hangman project, feel free to contact vinuri.rodrigo@gmail.com. Enjoy the game!
