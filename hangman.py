import random

# hangman strings
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# collection of words
word_list = ["aardvark", "baboon", "camel"]

# randomly chosen word from collection
chosen_word = random.choice(word_list)

# variable to show to user as they try to uncover the word
display = []

# iterate through the random word and add a blank for every character
for letter in chosen_word:
    display.append("_")

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter!\n").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("You Lost!")
            end_of_game = True
    if "_" not in display:
        end_of_game = True 
        print("You Win!")
       

