'''
This file is under the MIT License.

Copyright 2019-2021 Jeremiah Haven

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
# Startup is the file that starts off Bash For Windows. You can only run Bash for Windows with this script.

# Import libraries
import platform
import os
# If we are not in the right place, get us to the right place
if(os.path.exists(os.getcwd() + "/../Include") == False):
    os.chdir("Bash/Bash/Source/Include")
import bash
import os.path
import username
import usrmgr
import repair
import systemvariables
import time

# The commented out lines are for me to use for debugging purposes only.
#print(os.getcwd())
#print(os.path.dirname(os.path.realpath(__file__)))

# Set a system variable
systemvariables.init("exepath", os.getcwd())
systemvariables.init("settingspath", systemvariables.read("exepath") + "/../..")

# Check to make sure we are running on Windows and if not start bash
if(platform.system() != "Windows"):
    print("Bash for Windows has seen that you are not using Windows. Launching Bash...")
    os.system("bash")
    exit()
    
# Move to the root of the file structure
os.chdir(systemvariables.read("exepath") + "/../..")
#print(os.getcwd())

os.chdir("../..")
#print(os.getcwd())
#print(os.path.exists("Bash/Users"))
# See if any folders are deleted and if they are attempt to fix it using the repair script
try:
    if(os.path.exists("Bash/Users") == False):
        choice = input("Unfortunatly, Bash for Windows could not find your data. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
        if((choice == "y") or (choice == "Y")):
            repair.baseusrrepair()
        else:
            print("Abort.")
except KeyboardInterrupt:
    exit(0)

# Do the following if the username doesn't exist.
if(os.path.exists("Bash/Bash/Settings/ivhzadgz.bws") == False):
    print("Unfortunatly, Bash for Windows cannot find your user settings.")
    choice = input("Do you want to try to fix this problem? [Y,n] ")
    if((choice == "y") or (choice == "Y")):
        username.get()
        os.chdir("../..")
        usrname = open("Bash/Bash/Settings/ivhzadgz.bws")
    else:
        print("Abort. Username has been tempoarily set to null. Expect the enviornment to be unstable.")
        usrname = open("usrnam.txt", "w")
        usrname.write("null")
        usrname.close()
        usrname = open("usrnam.txt")
else:
    usrname = open("Bash/Bash/Settings/ivhzadgz.bws")

# Do the following if the password doesn't exist
try:
    if(os.path.exists("Bash/Bash/Settings/kvnnadgz.bws") == False):
        print("Unfortunatly, Bash for Windows cannot find your user settings.")
        choice = input("Do you want to try to fix this problem? [Y,n] ")
        if((choice == "y") or (choice == "Y")):
            username.get()
            os.chdir("../..")
        else:
            print("Abort. Expect the enviornment to be unstable.")
    else:
        usrname = open("Bash/Bash/Settings/kvnnadgz.bws")
except KeyboardInterrupt:
    exit(0)

# Check if the temp directory exists. If not, create it.
if(os.path.exists("Bash/temp") == False):
    os.mkdir("Bash/temp")

# Go back to here so that we don't trigger an unneeded repair
os.chdir(systemvariables.read("settingspath") + "/../..")
#print(os.getcwd())
# Check if the user folder was deleted
try:
    if(os.path.exists("Bash/Users/" + usrname.read()) == False):
        choice = input("Unfortunatly, Bash for Windows could not find your data. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
        if((choice == "y") or (choice == "Y")):
            repair.baseusrfilerepair()
        else:
            print("Abort.")
except KeyboardInterrupt:
    exit(0)

# We don't need this file to stay open
usrname.close()

# Go back to here so that we don't trigger an unneeded repair
os.chdir(systemvariables.read("settingspath") + "/../..")

# Call the login prompt
try:
    usrmgr.logon()
except KeyboardInterrupt:
    exit(0)
