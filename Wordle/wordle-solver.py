# Import Libraries

import enchant     
import webbrowser
import pyautogui
import time
from string import ascii_lowercase
import random

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


def main():
    # openBrowser()
    # pyautogui.click()
    # letters = builtalphabetdict()

    # print(pyautogui.locateOnScreen('Wordle\word-row.png'))
    # print(letters)
    # alphabetlist()

    ## GAME START
    d = enchant.Dict("en_US")

    words = getpossiblewords()
    gameword = getgameword(words)
    guesses = []
    letters = builtalphabetdict()
    alphabetlist = letters.keys()
    printboard(guesses, alphabetlist)
    print(f'Game Word: {gameword}')
    n = 0 
    correct = []
    present = []
    absent = []

    ## GAME ROUNDS 
    while n < 5:
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
           
        print(f'Correct: {correct}')
        print(f'Present: {present}')      
        print(f'Absent: {absent}')      
        
        # Need to identify method of grabing the correct letters before running the loop to clean up the data

        # s1, s2, s3, s4, s5 = ("",)*5
        # if correct[0][0] == 0:
        #     s1 = correct[0][0]
        # if correct[1][0] == 1:
        #     s2 = correct[1][0]
        # if correct[2][0] == 2:
        #     s3 = correct[2][0]
        # if correct[3][0] == 3:
        #     s4 = correct[3][0]
        # if correct[4][0] == 4:
        #     s5 = correct[4][0]

        # for a in letters:
        #     for b in letters:
        #         for c in letters:
        #             for d in letters:
        #                 for e in letters:
                            
        # Example for current code that I use to run for words that have three solved letters.
        # the dict is the list of letters that are currently active on the board. 
        # This code takes each and every permutation of the code and concats the data together.
        # words = []
        # for i in dict:
        #     for j in dict:
        #         word = ""
        #         if d.check(word):
        #             words.append(word)

        # for i in words:
        #     print(i)

if __name__ == "__main__":
    main()