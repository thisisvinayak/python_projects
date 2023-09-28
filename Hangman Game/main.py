import random
from hangman_art import logo, stages
from word_list import words

print(logo)

chosen_word = random.choice(words)
word_length = len(chosen_word)
lives = 6
end_of_game = False

# print(f"The chosen word is {chosen_word}")

# Create Blanks
display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter:").lower()

  # check if the user has guessed the letter they have already guessed
  if guess in display:
    print(f"You have already guessed {guess}.")

  # check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  # taking lives and subracting it out of 6
  if guess not in chosen_word:
    print(
        f"You have guessed {guess}, that is not in the word. You lose a life")

    lives -= 1
    if lives == 0:
      end_of_game = True
      print(f"You Loose, the correct word was: {chosen_word}")
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  # check if there are any blanks left
  if "_" not in display:
    end_of_game = True
    print("You Win")

  print(stages[lives])
