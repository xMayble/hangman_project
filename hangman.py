import random

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

while not end_of_game:
    guess = input("Guess a letter!\n").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(display)
    if "_" not in display:
        end_of_game = True 
        print("You Win!")

