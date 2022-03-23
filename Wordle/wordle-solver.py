# Import Libraries

import enchant     
import webbrowser
import pyautogui
import time
from string import ascii_lowercase
import random
import itertools


# Function activates GoogleChrome application and opens a new Tab.
def openBrowser():
    url = 'https://www.nytimes.com/games/wordle/index.html'
    chrome_path = r'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)
    
# Function closes the current GoogleChrome window.
def closeBrowser():    
    # Close Web Browser
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'w')
    print("tab closed")



# Function goes through the gameboard and loads the alphabet into a list of characters that 
# are currently active with the applicable status. 
    # Status 0 -  - letter has not be used in a word (default state)
    # Status 1 - present - letter has been used but incorrect location
    # Status 2 - correct - letter has been used and correct location
    # Status 3 - absent - letter used but not used

def alphabetlist(letters:dict):
    # Assume location on screen is always consistent
    # BeautifulSoup read in the html content from the current browser
    
    #Sample: <game-tile letter="w" evaluation="present" reveal=""></game-tile>
    # To obtian status we need to check the [evaluation] attribute for each [game-title] element
    
    # Grab All instances of "game-tile"
    # Loop through each letter until attribute doesn't exist then break
        # If found update dictionary
    
    
    return False

# Function generates a dictionary with all lowercase alphabet letters as the key and status as the value.
def builtalphabetdict():
    dict = {}
    for c in ascii_lowercase:
        dict[c] = 0
    return dict


# Function reads in locally generated CSV file and returns the full list of words. 
def getpossiblewords() -> list:
    words = []
    with open('.\Wordle\words.csv','r') as f:
        for row in f:
            row = row.strip('\n')[0:]
            words.append(row)
    return words

# Function takes in a list of words, shuffles the list, and returns top value.
def getgameword(words:list) -> str:
    random.shuffle(words)
    return words[0]

# Function takes in user input, checks that it is a valid word, and returns the word. 
def guessword(words:list) -> str:
    guess = ''
    while guess not in words:
        guess = input('Please choose a word:\n')
        print(guess)
    return guess

def printboard(guesses:list, alphabetlist:list) -> None:
    for i in range(6):
        if len(guesses) > i:
            print(f'{i} {guesses[i]}')
        else:
            print(f'{i} ')
    print(alphabetlist)

# def checkword(guess:str,solution:str, alphabetlist:dict):
    # for i in list(guess):

def possibilties(s:str,letters:list):
    n_wildcard = s.count('?')
    for subs in itertools.product(letters, repeat=n_wildcard):
        subs = iter(subs)
        yield ''.join([x if x != '?' else subs.__next__() for x in s])


def main():
    # openBrowser()
    # pyautogui.click()
    # letters = builtalphabetdict()

    # print(pyautogui.locateOnScreen('Wordle\word-row.png'))
    # print(letters)
    # alphabetlist()

    ## GAME START
    words = getpossiblewords()
    gameword = getgameword(words)


    n = 0 
    correct = []
    present = []
    absent = []
    letters = []
    guesses = []
    for c in ascii_lowercase:
        letters.append(c)

    alphabetlist = letters
    printboard(guesses, alphabetlist)
    print(f'Game Word: {gameword}')
    
    ## GAME ROUNDS 
    while n < 5:
        possible = set()
        # User Input is taken in
        currentword = guessword(words)
        guesses.append(currentword)

        # Find the bisection of the guess word and the solution word
        # correct_letters = list(set(list(guesses[0])).intersection(set(list(gameword))))

        # If user guesses the word correctly game ends
        if currentword == gameword:
            print('You Win')
            break
        
        # Compare the gameword and the current word to see which letters are the same or different.
        for idx, i in enumerate(gameword):
            for idy, j in enumerate(currentword):
                if i == j and idx == idy:
                    if [idx,i] not in correct:
                        correct.append([idx, i])
                elif i == j:
                    if [idx,i] not in present:
                        present.append([idx,i])
                else:
                    if j not in absent:
                        absent.append(j)
        # Clean up absent for any letters that exist are either correct or present
        for i in correct+present:
            print(i)
            if i[1] in absent:
                absent.remove(i[1])

        for i in absent:
            if i in letters:
                letters.remove(i)
           
        print(f'Correct: {correct}')
        print(f'Present: {present}')      
        print(f'Absent: {absent}')
        print(f'Alphabet: {letters}')

        #TODO Update Code and Refactor to simple method.
        correct_idx = {}
        for i in correct:
            letter = i[1]
            index = i[0]
            correct_idx[index] = letter
        print(correct_idx.items())

        s0, s1, s2, s3, s4 = ("?",)*5
        if correct_idx is not None:
            if 0 in correct_idx:
                s0 = correct_idx[0]
            if 1 in correct_idx:
                s1 = correct_idx[1]
            if 2 in correct_idx:
                s2 = correct_idx[2]
            if 3 in correct_idx:
                s3 = correct_idx[3]
            if 4 in correct_idx:
                s4 = correct_idx[4]

        # TODO 
        #-----------------------------------------------------------
        
        print(f's0: {s0}, s1: {s1}, s2: {s2}, s3: {s3}, s4: {s4}')

        temp = s0 + s1 + s2 + s3 + s4
        n_wildcard = temp.count('?')

        # Limit amount of checks when user has identifed at least 3 characters
        if n_wildcard < 3:
            for p in possibilties(temp,letters):
                print(p)
                if p in words:
                    possible.add(p)
            
            print(f'Possible Words Include: {possible}')

        else:
            print(f'Not enough information, guess again')


if __name__ == "__main__":
    main()
