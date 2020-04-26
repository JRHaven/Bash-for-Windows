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

# Popd is the companion command to Pushd, which is a program that allows you
# to add directories to a "stack", then using it's companion, Popd, allows 
# you to go to the last directory in that "stack". Really useful!

# Libraries
import os, systemvariables, pushd

# Main Function
def go():
    # Only do the following if there is something in the directory stack!!!
    if(systemvariables.directorystack[0] != ""):

        # Go to the first path listed in the directory stack
        os.chdir(systemvariables.directorystack[0])

        # Remove 1 item from the stack using the pushd program's remove function
        pushd.remove(1)

        # Do the whole generate display thing like we did in the Pushd program
        stackDisplay = ""
        i = 0
        while(i <= 7):
            stackDisplay = systemvariables.directorystack[i] + " " + stackDisplay
            i += 1
        print(stackDisplay, os.getcwd())
    else:
        # Directory Stack Empty Error
        print("bash: popd: directory stack empty")
