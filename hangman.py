import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")
print(display)

guess = input("Guess a letter!\n").lower()

for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        display[i] = guess
print(display)