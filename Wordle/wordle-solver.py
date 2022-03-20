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
            words.append(row)
    return words

# Function takes in a list of words, shuffles the list, and returns top value.
def getgameword(words:list) -> str:
    random.shuffle(words)
    return words[0]

def guessword(words:list) -> str:
    # while True:
        # try:
    guess = input('Please choose a word')
        # except ValueError:
        #     print("Not a! Please enter an integer.")
        #     continue
        # if len(guess) != 5 and guess not in words:
    return guess

def printboard(guesses:list, alphabetlist:list) -> None:
    for i in range(6):
        if len(guesses) > i:
            print(f'{i} {guesses[i]}')
        else:
            print(f'{i} ')
    print(alphabetlist)


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
    guesses = []
    letters = builtalphabetdict()
    alphabetlist = letters.keys()
    printboard(guesses, alphabetlist)

   ## GAME ROUNDS 
   # User Input is taken in
   # Append Users input 

if __name__ == "__main__":
    main()