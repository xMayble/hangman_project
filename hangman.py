import random
import hangman_words as words
import hangman_art as art

# randomly chosen word from collection
chosen_word = random.choice(words.word_list)

# variable to show to user as they try to uncover the word
display = []

# iterate through the random word and add a blank for every character
for letter in chosen_word:
    display.append("_")

end_of_game = False
lives = 6

print(art.logo)
print(f"Pssst, the solution is {chosen_word}")
while not end_of_game:
    guess = input("Guess a letter:" + " ").lower()
    for char in display:
        if char == guess:
            print(f"You already guessed {guess}")
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(display)    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life...")
        print("----------------------")
        lives -= 1
        if lives == 0:
            print("You Lost!")
            end_of_game = True
    print(art.stages[lives])
    if "_" not in display:
        end_of_game = True 
        print("You Win!")
       

