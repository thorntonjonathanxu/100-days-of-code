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
    words = getpossiblewords()
    gameword = getgameword(words)
    guesses = []
    letters = builtalphabetdict()
    alphabetlist = letters.keys()
    printboard(guesses, alphabetlist)
    print(gameword)
    n = 0 
    ## GAME ROUNDS 
    while n < 2:
        # User Input is taken in
        guesses.append(guessword(words))

        # Find the bisection of the guess word and the solution word
        # correct_letters = list(set(list(guesses[0])).intersection(set(list(gameword))))

        
        
        # If correct letters is not null, loop through solution and guess word 
        temp1 = []
        temp2 = []
        for idx, i in enumerate(list(guesses[len(guesses)-1])):
            temp1.append([idx,i])
        for idx, i in enumerate(list(gameword)):
            temp2.append([idx,i])

        for i in range(5):
            for j in range(5):
                if temp1[i] == temp2[i]:
                    letters[temp1[i][1]] = 2
                    print('Correct', temp1[i], temp2[i])        
                elif temp1[i][1] == temp2[j][1] and i != j:
                    letters[temp1[i][1]] = 1
                    print('Present', temp1[i], temp2[j])
                else:
                    continue                


            # if i in list(gameword) and idx == idy:
            #     letters[i] = 2
            #     print(i, idx, f'Correct - {idx}')
            # elif i in list(gameword):
            #     letters[i] = 1
            #     print(i, idx, f'Present not in {idx}')
            # else:
            #     # print(i, 'Not Present')
            #     continue
        for key, val in letters.items():
            if val != 0:
                print(key,val)
        n += 1

if __name__ == "__main__":
    main()