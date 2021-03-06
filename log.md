# #100DaysOfCode Log - Round 1 - Jonathan Thornton

The log of my #100DaysOfCode challenge. Started on 03/16/2022.

## Log

### Day 1: 
For my first project for this challenge, I'd like to review some of the open-source data sources that are available and general effective and appear visualizations using only python libraries/extensions. 

I implemented a simple request API request to pull down the records related to safety information and tried to map out bar charts and distribution content for categorical data including age and gender. Had issues trying to map neighborhood and lat/log data but will pursue this in the coming days as I work through this content. 

Applicable Source Data:
https://data.cincinnati-oh.gov/safety/Traffic-Crash-Reports-CPD-/rvmt-pkmq

### Day 2:
Today I wanted to focus on the aspects of categorizing data and displaying that information with matplotlib. Was able to build out a few pivot tables to show the breakdown by neighbor and built simple dataframe calls to display the content for age, gender, and neighborhood. 

I also inserted the mass data dump for the CSV file which I’ll use for my overall dataset now that I have general familiarization of the data. Am interested in refining the API call to grab the most current result-set every x number of days and determine where I’ll store this information in the longer term.


### Day 3:
Today I focused on import libraries for additional visualization tools including Plotly and Altair and getting the basic framework content interacting with Vscode. Didn't make a lot of progress as I was having issues with Anaconda rendering the visualizations and then realized that VSC doesn't host the plotly or altair visualizations locally so switched to Jupyter Notebook environment. 

A bit of a light day for development on the project but this is a rest day before going into more intense data models. 

### Day 4:

Decided to take a break from the visaulization project and foucs more on the Wordle Solver algorithm. Was able to build the basic game functionality and a simple loop that takes in user input and checks if the values exist and stores it in a list.

### Day 5:

Was able to update my logic from yesterday for how I am oranizing the data that is captured when checking for the word existence in the function. Rather than have a list with 3 elements [index, letter, status] decided to just have separate list for each status state and then check the list individually. This skimmed down the noise and complexity of the function checks and make sthe code more readable. 

Need to figure out how to generate the substring permutations without completely writting 5 loops which is my main objective for tomorrow.

### Day 6

Decided to refactor the method on generating the words by leveraging the itertools generator object. Rather than trying to build out a dynamic list, I decided to create a string with the indexes of the know characters set and then keeping the unknown set to a '?' indicator. The method generates all permutations and checks if its a valid word. To save on runtime, the user needs to guess at least 3 positional letters. 

Never really enjoyed using generators but this was definitely an ideal use case for leveraging it. Next steps will be to build methods on using the information about the words that are present and loading that content into the string checks.

### Day 7

For todays code I refactored most of the functions and removed the content that is no longer being leveraged in the build. With the method that parses out the content there was a lot of manual effort on calculating the index when a simple build handled the case as needed. Currently reviewing the next steps on how to handle this project and thinking I may go towards a simple Tkinter UI for the game to show the scores as they come up.

### Day 8
Removed redundant code around the solved string indicies and started to experiment with mapping content on a canvas. Had issues with the tkinter library rendering the content and will experiment with simple code blocks until I get the format similar to the wordle page. My objective with the UI is to be able to generate a simple gameboard utilizing tkinter. 