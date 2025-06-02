  wordGuessed[strLength] = '\0'; // Null-terminate the guessed word

  print_word(wordGuessed);
  printf("\n");

  // Game loop
  while (strcmp(wordGuessed, random_word) != 0)
  {
    printf("\nGuess a character: ");
    scanf(" %c", &guess); // Use " %c" to skip whitespace

    for (int i = 0; i < strLength; i++)
    {
      if (random_word[i] == guess && wordGuessed[i] == '_')
      {
        wordGuessed[i] = guess;
      }
    }

    print_word(wordGuessed);
    printf("\n");

    turn++;
    printf("Turn: %d\n\n", turn);
  }

  printf("You won in %d turns!\n", turn);
  return 0;
}

// Function to print the current state of the guessed word
void print_word(char *word)
{
  int strLength = strlen(word);