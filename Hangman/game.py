# Hangman game

import random

from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

print(logo)
print('\n')
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'

end_of_game = False
lives = 6
not_guess = ''

while not end_of_game:
    print('\n')
    guess = input('Guess a letter: \n').lower()

    if guess in display:
        print(f'You have already guessed this letter: " {guess.upper()} "')

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        if guess in not_guess:
            print(f' You have already try  letter: {guess.upper()}! Please make a different choice. ')
        else:
            print(f'The letter " {guess.upper()} " it\'s not in the word.You lose a life.')
            lives -= 1
            not_guess += guess

    print(f'Life\'s remain:{lives}')
    print(f'Not correct already tried letters : {not_guess.upper()}')
    if lives:
        print(stages[lives])
    elif lives == 0:
        print(stages[0])
        print(f'GAME OVER! YOU LOST!\nThe word was: {chosen_word}')
        end_of_game = True

    display_word_part = '  '.join(display)
    print(display_word_part.upper())

    if '_' not in display:
        end_of_game = True
        print('Congratulations! YOU WON!')
