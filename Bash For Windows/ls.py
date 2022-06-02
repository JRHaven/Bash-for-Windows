'''
This file is under the MIT License.

Copyright 2019-2022 Jeremiah Haven

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
# ls is a basic script that either outputs the files in a directory or returns a list of files in the current
# directory

# Libraries
from os import walk
from time import sleep
import os, glob, tofile
import systemvariables

# Function that prints out all files 1 by 1 virtically without any other characters on the screen
def show(args):
    # Store all output in a variable
    output = ""

    # If the user didn't give any arguments, assume they wanted .
    if(args[0] == ""):
        dest = "."
    else:
        dest = args[0]

    # Make sure the directory requested exists and that it is a directory
    if((os.path.exists(dest) == True) and (os.path.isdir(dest) == True)):
        # Remember what directory we are currently in then change to the requested directory.
        lastDir = os.getcwd()
        os.chdir(dest)

        # Get a listing fo what is in the directory, then list them in a fancy way
        dir_list = os.listdir(os.getcwd())
        hold = []
        i = 0
        j = 0
        dirs = 0

        for file in dir_list:
            if(os.path.isdir(file) == True):
                dirs += 1

        for file in dir_list:
            # Debug message if it is enabled
            if(systemvariables.read("debugMsg") == 1):
                print(systemvariables.color.YELLOW + systemvariables.color.BOLD + "[Debug]" + systemvariables.color.END + " ls:", os.path.isdir(str(dir_list[i])))
            if(os.path.isdir(file) == True):
                if(i == len(dir_list) - 1):
                    if((dirs == 1) and (len(dir_list) > 1)):
                        output = output + file + " [DIR]\n"
                    else:
                        output = output + file + " [DIR]"
                else:
                    output = output + file + " [DIR]\n"
            else:
                hold.append(file)
            i += 1

        for k in hold:
            if(j == len(hold) - 1):
                output = output + k
            else:
                output = output + k + "\n"
            j += 1

        # Go to the directory we were just in.
        os.chdir(lastDir)

        tofile.write(args, output)
    else:
        # Error Message: if it is a file repeat file name
        if(os.path.isfile(dest) == True):
            print(dest)
        else:
            print("ls: cannot access '" + dest + "': No such file or directory")
        
# Function that returns a list of everything in the current directory
def list():
    theList = os.listdir(os.getcwd())
    return theList

# Function that prints out all of the variables, unlike the echo script that only prints out 1 
# requested variable
def vars(args):
    output = ""
    for i in systemvariables.varsNames:
        output = output + i + ": " + str(systemvariables.read(i)) + "\n"
    output = output + "directorystack: " + str(systemvariables.directorystack)
    flag = 0
    tofile.write(args, output)