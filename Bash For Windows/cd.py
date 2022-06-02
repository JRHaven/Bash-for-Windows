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
# cd is a basic script that deciphers tildas and slashes then goes into desired directory

# Libraries
import os
import systemvariables

# Variable
currentdir = ""

# Main Function
def go(args):
    path = str(args[0])
    currentdir = os.getcwd()
    otherdir = systemvariables.read("lastdir")
    
    # If we have inputed something special, go to a special place.
    # If not, go to where directed.
    if((path == "~") or (path == "")):
        os.chdir(systemvariables.read("HOME"))
    elif(path == "-"):
        if(systemvariables.read("lastdir") == ""):
            print("bash: cd: $lastdir not set")
        else:
            os.chdir(systemvariables.read("lastdir"))
    elif(path == "/"):
        os.chdir(systemvariables.read("ROOT"))
    elif(path[0] == "$"):
        # This is how we are handling variables, if they aren't already translated by the system
        # First, get the variable requested by selecting the part of the variable that isn't a $
        varReq = path.split("$")[1]

        # Verification and changing of path
        if(systemvariables.lookupIndex(varReq) != -1):
            pathReq = systemvariables.read(varReq)
            if(os.path.exists(pathReq) == True):
                os.chdir(pathReq)
    else:
        if(os.path.exists(path) == True):
            os.chdir(path)
        else:
            print("bash: cd:", path + ": No such file or directory")
    # Set the lastdir system variable
    systemvariables.modifyVoid("lastdir", currentdir)
    
    if(os.getcwd() == systemvariables.read("lastdir")):
        systemvariables.modify("lastdir", otherdir)