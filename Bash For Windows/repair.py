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
import systemvariables, mkdir

# Repair for anything missing in the base folder
# Repair for anything missing in the base of the user folder
def baseusrrepair():
    # We need to be in this directory, stored as a System Variable we
    # set at Startup
    os.chdir(systemvariables.settingspath)

    # If needed, create a new user account
    if((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        username.get()
    
    print("Solving Problems...")

    # Get the username information
    username = open("Settings/ivhzadgz.bws")

    # Put the contents of the username in a variable so we can use
    # it any time without having to be in that directory
    usrname = username.read()

    # We don't need the origonal variable anymore
    username.close()

    # Start Recreating Folders
    os.chdir("..")
    os.mkdir("Users")
    os.chdir("Users")
    os.mkdir(usrname + "/")
    os.chdir(usrname)
    os.mkdir("Documents")
    os.mkdir("Downloads")

    # Success message and go to the correct directory
    print("Repair has solved the problem")
    os.chdir(systemvariables.exepath)
    
# Like the function we just had, but only repairs in the user's personal folder
def baseusrfilerepair():
    # We need to be in this directory, stored as a System Variable we
    # set at Startup
    os.chdir(systemvariables.settingspath)

    # If needed, create a new user account
    if((os.path.exists("Settings/ivhzadgz.bws") == False) or (os.path.exists("Settings/kvnnadgz.bws") == False)):
        username.get()
    
    print("Solving Problems...")

    # Get the username information
    username = open("Settings/ivhzadgz.bws")

    # Put the contents of the username in a variable so we can use
    # it any time without having to be in that directory
    usrname = username.read()

    # We don't need the origonal variable anymore
    username.close()

    # Start Recreating Folders
    os.chdir("../Users")
    os.mkdir(usrname + "/")
    os.chdir(usrname)
    os.mkdir("Documents")
    os.mkdir("Downloads")

    # Success message and go to the correct directory
    print("Repair has solved the problem")
    os.chdir(systemvariables.exepath)
    
# Repair for anything missing in the settings folder
def settingsrepair():
    print("Solving Problems...")
    os.chdir(systemvariables.exepath + "/../..")
    os.mkdir("Settings")
    username.get(os.getcwd())
    os.chdir(systemvariables.exepath + "/../..")

# Repair the Documents Folder
def docs():
    print("Solving Problems")
    os.chdir(systemvariables.HOME)
    mkdir.create(["Documents"])
    if(os.path.exists("Documents") == True):
        print("Success! Note: Anything that was in the Documents folder before was deleted.")
        return True
    else:
        systemvariables.USRDOCS = "null"
        print("Failed. USRDOCS Variable set as null.")
        return False