# Import Libraries

import enchant     
import webbrowser
import pyautogui
import time

# Function activates GoogleChrome application and opens a new Tab.
def openBrowser():
    url = 'https://www.nytimes.com/games/wordle/index.html'
    chrome_path = r'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)
    pyautogui.press('left')
    
    # Click screen to remove pop-up that appears
    
    # Close Web Browser
    time.sleep(20)
    pyautogui.hotkey('ctrl', 'w')
    print("tab closed")



# Function goes through the gameboard and loads the alphabet into a list of characters that 
# are currently active with the applicable status. 
    # Status 0 - Acitve but Not Used
    # Status 1 - Active and Wrong Space
    # Status 2 - Active and Correct
    # Status 3 - Inactive
def alphabetlist():

    return False

def main():
    openBrowser()
    return False

if __name__ == "__main__":
    main()