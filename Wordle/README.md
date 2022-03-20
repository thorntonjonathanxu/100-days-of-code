# Wordle Auto Solver

## Summary

This project is associated to the popular NYTimes puzzle that has been trending in early 2022. The objective of the project is to build an application that start the puzzle and successfully guess within the six guesses that allocated to the player.

1. Application opens a new Google Browser incognito window
2. Application goes to the NYTimes wordle endpoint
3. Application plays game
4. Records output of a success or failure and writes to file.

---
### Phase 1 Development
Foucs on the process of solving the puzzle through automation. I have generated a list of words that contain 5 letters and are all valid dictionary words. Function will read in the words, select a random word for the puzzle. Program will then guess two unique words and read the input with the objective of getting at least 3 present letters. 

