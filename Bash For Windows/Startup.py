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
# Startup is the file that starts off Bash For Windows. You can only run Bash for Windows with this script.

# Import libraries
import platform
import bash
import os
import os.path
import username
import usrmgr
import usrmgr2
import repair
import systemvariables
import time

# The commented out lines are for me to use for debugging purposes only.
#print(os.getcwd())
#print(os.path.dirname(os.path.realpath(__file__)))

# Set a system variable
systemvariables.exepath = os.path.dirname(os.path.realpath(__file__))
systemvariables.settingspath = systemvariables.exepath + "/../.."

# Check to make sure we are running on Windows and if not start bash
if(platform.system() != "Windows"):
    print("Bash for Windows has seen that you are not using Windows. Launching Bash...")
    os.system("bash")
    exit()
    
# Move to the root of the file structure
os.chdir(systemvariables.exepath + "/../..")
#print(os.getcwd())

os.chdir("../..")
#print(os.getcwd())

usrname = open("Bash/Bash/Settings/ivhzadgz.bws")

# See if any folders are deleted and if they are attempt to fix it using the repair script
if(os.path.exists("Bash/Users") == False):
    choice = input("Unfortunatly, Bash for Windows could not find your data. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
    if((choice == "y") or (choice == "Y")):
        repair.baseusrrepair()
    else:
        print("Abort.")

# Go back to here so that we don't trigger an unneeded repair
os.chdir(systemvariables.settingspath + "/../..")

# Check if the user folder was deleted
if(os.path.exists("Bash/Users/" + usrname.read()) == False):
    choice = input("Unfortunatly, Bash for Windows could not find your data. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
    if((choice == "y") or (choice == "Y")):
        repair.baseusrfilerepair()
    else:
        print("Abort.")

# We don't need this file to stay open
usrname.close()

# Go back to here so that we don't trigger an unneeded repair
os.chdir(systemvariables.settingspath + "/../..")

# Tell the login prompt what folder we are in
usrmgr2.usrcheck(os.getcwd())
username = open("Bash/Bash/Settings/ivhzadgz.bws" , "r")

# Call the login prompt
usrmgr.logon()
