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
# Repair is a script that tries to solve any problems that comes up

# Libraries
import os
import username
import systemvariables, mkdir

# Repair for anything missing in the base of the user folder
def baseusrrepair():
    # Get where we are now so we can return to it later
    oldPWD = os.getcwd()

    # We need to be in this directory, stored as a System Variable we
    # set at Startup
    os.chdir(systemvariables.read("settingspath"))

    # If needed, create a new user account
    if(os.path.exists("Settings/ivhzadgz.bws") == False):
        if(os.path.exists("Settings") == False):
            os.mkdir("Settings")
        username.get()
    
    print("Solving Problems...")

    # Get the username information
    usrnam = open("Settings/ivhzadgz.bws")

    # Put the contents of the username in a variable so we can use
    # it any time without having to be in that directory
    usrname = usrnam.read()
    usrnam.close()

    # Start Recreating Folders
    os.chdir("..")
    os.mkdir("usrdata")
    os.chdir("usrdata")
    os.mkdir("Documents")
    os.mkdir("Downloads")

    # Success message and go to the correct directory
    print("Repair has solved the problem")
    os.chdir(oldPWD)

def promptInit(pth):
    os.chdir(pth)
    if(os.path.exists("prompt.bws") == False):
        prompt = open("prompt.bws", "w")
        prompt.write("# prompt.bws\n")
        prompt.write("# This is a configuration file that tells Bash for Windows to initialize system variables defined within this file.\n")
        prompt.write("# Format:\n#     name=contents\n# You can make a comment using a hash (#) symbol.\n")
        prompt.write("# DO NOT delete this file. If it is deleted, it isn't fatel, however, upon next login to Bash for Windows, Bash for \
Windows will initalize a new prompt.bws file, which means any modifications you or the system makes to this file will be lost.\n")
        prompt.write("# DO NOT put any spaces on any line, the space will be preserved in the variable name or its contents. For example:\n")
        prompt.write("#     variablename = test\n# The above will result in a variable being created called \"variablename \" \
with its contents being \" test\".\n")
        prompt.write("# You must ALWAYS have an equals sign, don't just call a variable name without put an equals sign.\n")
        prompt.write("# If you don't want this, don't put any spaces anywhere.\n# \n# The following variables that will be initalized \
are optional variables that directly corellate with Bash for Windows itself,\n# some are fore experimental use, some unlock optional functionality ")
        prompt.write("from within Bash for Windows. To enable them, just uncomment them by removing the hash mark in front of them.\n")
        prompt.write("# Although Bash for Windows shouldn't care if these aren't in this file, because some of them are for experimental use,\
you should keep these in the file.\n\n# To add more variables, it is suggested for this file to stay organized to put any ")
        prompt.write("of your own variables under this first set of variables.\n# Any variables before the \"protectend\" line will be\
read and write protected, only avalible to the system or an internally elevated user.\n")
        prompt.write("#debugMsg=1\n")
        prompt.write("#varTrans=1\n")
        prompt.write("#colorPrompt=1\n")
        prompt.write("\n# Put your custom variables below:\n")
        prompt.close()
        return 0
    else:
        return 1