# Plan

# Requirements
* Must be ran through the command line
* Must be able to choose a file in the same folder that program is in. 
* Opens said file, and using some pre-determined information, delete columns of data that don't have purpose for 
us.
* Doing this, we will add, or create a new file for the newly formed and organized data. 
* Must have a way to name the new or edited file. 
# Design

## Input
The user will run the program using command line. It will look like this:
`
python main.py {title of file}
`


## Process
We first need to import `sys` and then we must check if the arguments of `sys.argv` amounts to at least 2 with
an if statement. If not, we know that they just tried to run the file, but did not indicate which file they 
wanted to be edited. We will need to print a statement saying how to use the program (using 'usage: {the necessary 
arguments}) and then use the exit command `sys.exit(1)`. 

If that passes, we will need to take the `open()` function and take the 1st argument of `sys.argv` and 
set that equal to a variable (recommended file or f). We will then use the `.readline()` function and using a 
for loop, go through each line in the variable for the file, (ie: `for line in f:`). 


## Output

# Implementation

# Verification

# Ideas for future Development
* ways to name file
* ways to include the date range of the report at the top of the file
