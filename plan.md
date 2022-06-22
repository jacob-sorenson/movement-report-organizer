# Plan

# Requirements
* Must be ran through the command line
* Must be able to choose a file in the same folder that program is in. 
* Opens said file, and using given information in a separate file, deletes columns of data that don't have purpose for
 the user.
* Doing this, we will add, or create a new file for the newly formed and organized data.
# Design

## Input
The user will run the program using command line while in the directory of the project. It will look like this:
`
python main.py {title of file}
`


## Process
We first need to import `sys` and then we must check if the arguments of `sys.argv` amounts to at least 2 with
an if statement. If not, we know that they just tried to run the file, but did not indicate which file they 
wanted to be edited. We will need to print a statement saying how to use the program (using 'usage: {the necessary 
arguments}) and then use the exit command `sys.exit(1)`. 

Once that is Successful, we will need to figure out what information we will be looking for. That will be in the `keep.csv`
file in the directory. As for now, this will just act more like a text file. We will just add all the column titles that
we want to be keeping on their own individual lines. This way, in our program, we can open up the file with the `open()`
function, set it to a variable, then using a for loop, take each line and add it to a list. Finally, calling a `.close()` 
function to close the file.

Afterwards we need to create a list to contain all the new data: `newData = []`

We will need then need to use the `open()` function again and take the 1st argument of `sys.argv` as the parameter for 
`.open()` and 
set that equal to a variable (recommended: file or f). We will then use the `.readline()` function to get the first line
of the file and set it to a new variable. With this, we will need to use a for loop, looping through the 'keep list' to 
find the index of each of those columns that we want to keep. We will create a `keepIndexList` and add these indexes to a
list that we will use shortly after. 

We will then use a for loop, go through each line in the variable of the file, (ie: `for line in f:`). With each line, 
we will then look at the index numbers of the numbers in the `keepIndexList` and take that data, and add it to a variable
called `row` which was initialized first as a list. (aka `row=[]`) Then we just use the `.append()` function using the
data associated with each index to be the parameter for the function. Eventually, we will have a list of the all the 
data associated with a row/item which we then can append to the list called `newData`






## Output

# Implementation

# Verification

# Ideas for future Development
* ways to name file
* ways to include the date range of the report at the top of the file
* make it so that we can control what order the new information is in
