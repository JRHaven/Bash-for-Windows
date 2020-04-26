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
# cd is a basic script that deciphers tildas and slashes then goes into desired directory

# Libraries
import os
import systemvariables

# Variable
currentdir = ""

# Main Function
def go(path):
    currentdir = os.getcwd()
    otherdir = systemvariables.lastdir
    
    # If we have inputed something special, go to a special place.
    # If not, go to where directed.
    if(path == "~"):
        os.chdir(systemvariables.HOME)
    elif(path == "-"):
        os.chdir(systemvariables.lastdir)
    elif(path == "/"):
        os.chdir(systemvariables.ROOT)
    elif(path == "$settingspath"):
        os.chdir(systemvariables.settingspath)
    elif(path == "$exepath"):
        os.chdir(systemvariables.exepath)
    elif(path == "/Bash"):
        os.chdir(systemvariables.bshpath)
    elif(path == "/Bash/Bash"):
        os.chdir(systemvariables.settingspath)
    elif(path == "/Bash/Users"):
        os.chdir(systemvariables.usrpath)
    elif(path == "/Bash/Bash/Settings"):
        os.chdir(systemvariables.loginfopath)
    elif(path == "/Bash/Bash/Source"):
        os.chdir(systemvariables.srcpath)
    elif(path == "/Bash/Bash/Source/Include"):
        os.chdir(systemvariables.exepath)
    elif(path == "$bshpath"):
        os.chdir(systemvariables.bshpath)
    elif(path == "$usrpath"):
        os.chdir(systemvariables.usrpath)
    elif(path == "$loginfopath"):
        os.chdir(systemvariables.loginfopath)
    elif(path == "$srcpath"):
        os.chdir(systemvariables.srcpath)
    else:
        if(path == ""):
            go("~")
        else:
            if(os.path.exists(path) == True):
                os.chdir(path)
            else:
                print("bash: cd:", path + ": No such file or directory")
    # Set the lastdir system variable
    systemvariables.lastdir = currentdir
    
    if(os.getcwd() == systemvariables.lastdir):
        systemvariables.lastdir = otherdir
