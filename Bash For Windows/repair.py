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
# Repair is a script that tries to solve any problems that comes up

# Libraries
import os
import username
import systemvariables

# Repair for anything missing in the base folder
def baserepair():
    if((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        username.get()
    print("Solving Problems...")
    usrname = open("../../Settings/ivhzadgz.bws")
    os.mkdir("Bash")
    os.mkdir("Bash/Users")
    os.mkdir("Bash/Users/" + usrname.read())
    os.mkdir("Bash/Users/" + usrname.read() + "/Downloads")
    os.mkdir("Bash/Users/" + usrname.read() + "/Documents")
    
# Repair for anything missing in the base of the user folder
def baseusrrepair():
    if((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        username.get()
    print("Solving Problems...")
    usrname = open("../../Settings/ivhzadgz.bws")
    os.mkdir("Bash/Users")
    os.mkdir("Bash/Users/" + usrname.read())
    os.mkdir("Bash/Users/" + usrname.read() + "/Downloads")
    os.mkdir("Bash/Users/" + usrname.read() + "/Documents")
    
# Like the function we just had, but only repairs in the user's personal folder
def baseusrfilerepair():
    if((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        username.get()
    print("Solving Problems...")
    usrname = open("../../Settings/ivhzadgz.bws")
    os.mkdir("Bash/Users/" + usrname.read())
    os.mkdir("Bash/Users/" + usrname.read() + "/Downloads")
    os.mkdir("Bash/Users/" + usrname.read() + "/Documents")
    
# Repair for anything missing in the settings folder
def settingsrepair():
    print("Solving Problems...")
    os.chdir(systemvariables.exepath + "/../..")
    os.mkdir("Settings")
    username.get(os.getcwd())
    os.chdir(systemvariables.exepath + "/../..")
