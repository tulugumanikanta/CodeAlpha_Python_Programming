import random
import Hangman_stages
print('==========================================','\n',
      '           welcome to Hangman Game        ')
print('==========================================')
word_list = ['python','computer','keyboard','mouse','data']
lives = 6
print ('Total lives: ',lives)
random_word = random.choice(word_list) 
guess_word = []
for word in random_word:
    guess_word += '_'
print(guess_word)
game_over = False
while not game_over:
    guess_latter = input('Guess a latter: ').lower()
    for i in range(len(random_word)):
        latter = random_word[i]
        if latter == guess_latter:
            guess_word[i] = guess_latter
            print (guess_word)
            print ('Latter Mached')
    if guess_latter not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print('hangman stages are over you loose the game!!!')
    if '_' not in guess_word:
        game_over = True
        print ('word complete. you win!!!')
    print(Hangman_stages.stages[lives])

