'''
This file is under the MIT License.

Copyright 2019-2020 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# Pushd is a program that allows you to add directories to a "stack", then
# using it's companion, Popd, allows you to go to the last directory in
# that "stack". Really useful!

# Libraries
import os, systemvariables, cd

# Function to add a directory to the stack
def add(path):

    # Get ready for a loop
    i = 7
    while(i > 0):

        # Take the entry left to the one we are looking at and move
        # it to the one we are looking at now
        systemvariables.directorystack[i] = systemvariables.directorystack[i-1]

        # Go to look at the next entry
        i -= 1

    # Now fill in the first entry with the path we inputed
    systemvariables.directorystack[0] = path

# Function to remove an entry from the stack
def remove(times):

    # Commented lines of code are for debugging purposes only.
    #print(systemvariables.directorystack)

    # Counter
    j = 0

    # Loop to do this as many times as requested
    while(j != times):
        # Another Counter
        i = 0

        # Do this for all items in the stack
        while(i < 7):
            #print(systemvariables.directorystack)

            # Move the item we are looking at to the right
            systemvariables.directorystack[i] = systemvariables.directorystack[i+1]

            # Increment
            i += 1

        # Delete the last item
        systemvariables.directorystack[7] = ""

        # Increment the counter to prepare to do it again!
        j += 1
    #print(systemvariables.directorystack)

# Main Function
def go(path):
    # Check to make sure the path exists.
    if(os.path.exists(path) == True):
        # Add the current directory to the stack using the function we made earlier
        add(os.getcwd())

        # Create a variable to represent the stack for output
        stackDisplay = ""

        # Create a counter for the loop that we will program momentarily
        i = 0

        # Do this starting at the beginning of the stack going to the end for
        # all the items in the stack
        while(i <= 7):

            # Add the item we are looking at to the Display variable, insert
            # a space, then add on what we already have in the variable
            stackDisplay = systemvariables.directorystack[i] + " " + stackDisplay

            # Decrement to shift focus to the item to the right of the stack
            i += 1

        # Finally, display the display we made plus the current directory we
        # are in, but only after going to that directory that is first in
        # the stack
        cd.go(path)
        print(stackDisplay, os.getcwd())
    else:
        # Directory Not Found Error
        print("bash: pushd:", path + ": No such file or directory")
