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

    # If we don't request to list the current directory and don't want to send output of current
    # directory to file, do the following:
    if((args[0] != "") and ((args[0] != ">") and (args[0] != ">>"))):
        # Make sure the directory requested exists and that it is a directory
        if((os.path.exists(args[0]) == True) and (os.path.isdir(args[0]) == True)):
            # Remember what directory we are currently in then change to the requested directory.
            lastDir = os.getcwd()
            os.chdir(args[0])

            # Get a listing fo what is in the directory, then list them in a fancy way
            dir_list = os.listdir(os.getcwd())
            hold = []
            i = 0
            j = 0
            for dirs in dir_list:
                #print(os.path.isdir(str(dir_list[i])))
                if(os.path.isdir(dir_list[i]) == True):
                    if(i == len(dir_list) - 1):
                        output = output + dir_list[i] + " [DIR]"
                    else:
                        output = output + dir_list[i] + " [DIR]\n"
                else:
                    hold.append(dir_list[i])
                i += 1
            for k in hold:
                if(j == len(hold) - 1):
                    output = output + hold[j]
                else:
                    output = output + hold[j] + "\n"
                j += 1

            # Go to the directory we were just in.
            os.chdir(lastDir)

            # If asked to do so, send output to a file. Either overwrite a file or append to it.
            if(">>" in args):
                i = 0
                index = 0
                for j in args:
                    if(i == 0):
                        i += 1
                        continue
                    if(args[i] == ">>"):
                        index = i + 1
                        break
                    i += 1
                tofile.write(">>", output, args[index])
            elif(">" in args):
                i = 0
                index = 0
                for j in args:
                    if(i == 0):
                        i += 1
                        continue
                    if(args[i] == ">"):
                        index = i + 1
                        break
                    i += 1
                tofile.write(">", output, args[index])
            # If we don't want to send output of command to a file, print the output to the screen.
            else:
                print(output)
        else:
            # Error Message: if it is a file repeat file name
            if(os.path.isfile(args[0]) == True):
                print(args[0])
            else:
                print("ls: cannot access '" + args[0] + "': No such file or directory")

    # Either print listing of current directory or send output of command to file.
    # Pretty much the same as before.
    elif((args[0] == "") or (args[0] == ">") or args[0] == ">>"):
        dir_list = os.listdir(os.getcwd())
        hold = []
        i = 0
        j = 0
        for dirs in dir_list:
            #print(os.path.isdir(str(dir_list[i])))
            if(os.path.isdir(dir_list[i]) == True):
                if(os.path.isdir(dir_list[i]) == True):
                    if(i == len(dir_list) - 1):
                        if(len(hold) == 0):
                            output = output + dir_list[i] + " [DIR]"
                        else:
                            output = output + dir_list[i] + " [DIR]\n"
                    else:
                        output = output + dir_list[i] + " [DIR]\n"
            else:
                hold.append(dir_list[i])
            i += 1
        for k in hold:
            if(j == len(hold) - 1):
                output = output + hold[j]
            else:
                output = output + hold[j] + "\n"
            j += 1
        if(">>" in args):
            tofile.write(">>", output, args[1])
        elif(">" in args):
            tofile.write(">", output, args[1])
        else:
            print(output)
        
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
    print("settingspath:", systemvariables.settingspath)
    print("loginfopath:", systemvariables.loginfopath)
    print("srcpath:", systemvariables.srcpath)
    print("bshpath:", systemvariables.bshpath)
    print("lastdir:", systemvariables.lastdir)
    print("directorystack:", systemvariables.directorystack)
