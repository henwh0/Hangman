import random
HANGMAN_NOOSE = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']                    
WORDS = 'apple aardvark ant antelope ape archery bear bat banana basketball berlin baboon badger beaver butt cat cow cherry cricket chicago camel clam cobra cougar coyote crow deer dog donkey duck date diving denver eagle elephant eel elderberry equestrian edinburg fox falcon flag fig football florence ferret frog goat goose giraffe grape golf glasgow hawk horse honeydew hockey hamburg iguana indiana istanbul jackal jaguar jackfruit judo jerusalem kangaroo koala kiwi kyoto kayak lion lamb lemon lacrosse london lizard llama mole monkey moose mouse mule mango marathon madrid newt narwhal naples nectarine otter owl ostritch orange ottawa penguin panther papaya polo paris panda pigeon python quail quebec rabbit rhino raspberry rowing rome raven salmon seal shark sheep sloth skunk snake spider swan strawberry soccer sydney stork tiger toad trout turkey turtle tangerine tennis tokyo vulture volleyball vienna wolf watermelon weasel whale wombat yak yoga zebra'.split()
def getRandomWord(wordlist):
    return random.choice(wordlist)
def displayBoard(HANGMAN_NOOSE, missedletters, correctletters, secretword):
    print(HANGMAN_NOOSE[len(missedletters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedletters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretword)
    for i in range(len(secretword)):
        if secretword[i] in correctletters:
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]
    print(blanks)
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input().lower()
        if len(guess) != 1:
            print('Enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Try again..')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Choose a LETTER.')
        else:
            return guess
def playAgain():
    while True:
        print('Do you want to play again? (Y or N)')
        response = input().lower()
        if response.startswith('y'):
            return True
        elif response.startswith('n'):
            return False
        else:
            print('Enter Y or N')
print('H A N G M A N')
while True:
    missedletters = ''
    correctletters = ''
    secretWord = getRandomWord(WORDS)
    gameIsDone = False
    while not gameIsDone:
        displayBoard(HANGMAN_NOOSE, missedletters, correctletters, secretWord)
        guess = getGuess(missedletters + correctletters)
        if guess in secretWord:
            correctletters = correctletters + guess
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctletters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('You win! The word is: "' + secretWord + '"')
                gameIsDone = True
        else:
            missedletters = missedletters + guess
            if len(missedletters) == len(HANGMAN_NOOSE) - 1:
                displayBoard(HANGMAN_NOOSE, missedletters, correctletters, secretWord)
                print('You are out of guesses.\nAfter ' + str(len(missedletters)) + ' missed guesses and ' + str(len(correctletters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True
    if not playAgain():
        exit()
