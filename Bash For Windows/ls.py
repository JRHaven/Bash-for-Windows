'''
This file is under the MIT License.

Copyright 2019 Jeremiah Haven

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
import os
import glob
import systemvariables

# Function that prints out all files 1 by 1 virtically without any other characters on the screen
def show():
    dir_list = os.listdir(os.getcwd())
    i = 0
    for dirs in dir_list:
        print(dir_list[i])
        i += 1
        
# Function that returns a list of everything in the current directory
def list():
    theList = os.listdir(os.getcwd())
    return theList

# Function that prints out all of the variables, unlike the echo script that only prints out 1 requested
# variable
def vars():
    print("usrsession:", systemvariables.usrsession)
    print("HOME:", systemvariables.HOME)
    print("ROOT:", systemvariables.ROOT)
    print("exepath:", systemvariables.exepath)
    print("USRDOCS:", systemvariables.USRDOCS)
