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
# usrmgr is a script responsable for the login prompt, the not-yet implemented multiple user function and
# welcoming the user into Bash For Windows. Despite not being the first script executed, this is the first
# time the user interacts with Bash For Windows.

# Libraries
import os, repair, bash, platform, time, systemvariables, oschk, touch, nano, socket

# Clear the screen to get rid of the messages from the imported libraries
os.system("cls")

def autoRun(autorun):
    commands = [""]
    i = 0
    j = 0
    k = 0
    for i in autorun:
        # If we come across a ;, add an item to the array and skip the rest
        if(i == ";"):
            k += 1
            commands.append("")
            continue

        # Take the character and put it in the appropriate spot in the array.
        commands[k] = commands[k] + i
    i = 0
    j = 0
    for i in commands:
        bash.runcmd(commands[j])
        j += 1

# Login
def logon():
    os.chdir(systemvariables.read("settingspath") + "/Settings")
    # If the prompt.bws file doesn't exist, call on repair script to initialize one.
    if(os.path.exists("prompt.bws") == False):
        if(repair.promptInit(os.getcwd()) == 1):
            os.system("cls")
            print("Bash for Windows has run into a non-critical error:\nPROMPT_NOT_ACCESSABLE\n\n\
This is not a critical error, so Bash for Windows will continue to work ok,\nminus some optional \
functionality.")
            choice = input("Do you want to contnue using Bash for Windows? [y,N] ")
            if(choice.upper() != "Y"):
                exit(1)
            # Initialize variables with default values
            systemvariables.init("debugMsg", 0)
            systemvariables.init("varTrans", 0)
            systemvariables.init("colorPrompt", 0)
    else:
        print("Welcome to Bash(the Bourne Again Shell) for Windows!")

        while(True):
            # Load in prompt.bws variables
            os.chdir(systemvariables.read("settingspath") + "/Settings")

            # Store the contents of the prompt.bws file into memory
            file = open("prompt.bws", "r")
            promptConfigTxt = file.read()
            file.close()
            j = 0

            # Store each line of text in an array
            txtOnLine = promptConfigTxt.split("\n")

            # Seperate each value with equals sign and put them in a system variable, unless it has
            # a # as it's first character
            j = 0
            l = 0
            for i in txtOnLine:
                varNam = ""
                varConts = ""
                shift = 0
                l = 0
                if(i != ""):
                    if((i[0] != "#") and ("=" in i)):
                        var = i.split("=")
                        systemvariables.init(var[0], var[1])
                j += 1
            
            # The variables that come with the prompt.bws file should be turned into integers
            if((systemvariables.read("varTrans") == "1")):
                systemvariables.modifyVoid("varTrans", 1)
            else:
                if(systemvariables.read("varTrans") != -1):
                    systemvariables.modifyVoid("varTrans", 0)
            if((systemvariables.read("debugMsg") == "1")):
                systemvariables.modifyVoid("debugMsg", 1)
            else:
                if(systemvariables.read("debugMsg") != -1):
                    systemvariables.modifyVoid("debugMsg", 0)
            if((systemvariables.read("colorPrompt") == "1")):
                systemvariables.modifyVoid("colorPrompt", 1)
            else:
                if(systemvariables.read("colorPrompt") != -1):
                    systemvariables.modifyVoid("colorPrompt", 0)
            if((systemvariables.read("colorPrompt") == "1")):
                systemvariables.modifyVoid("colorPrompt", 1)
            else:
                if(systemvariables.read("colorPrompt") != -1):
                    systemvariables.modifyVoid("colorPrompt", 0)
            if((systemvariables.read("disableOSCheck") == "1")):
                systemvariables.modifyVoid("disableOSCheck", 1)
            else:
                if(systemvariables.read("disableOSCheck") != -1):
                    systemvariables.modifyVoid("disableOSCheck", 0)
            
            # Run an OS Check
            oschk.check()
            
            # We need to go to the parent directory
            os.chdir("..")

            # Check for autorun.bws file, and call a function to take care of the rest
            if(os.path.exists("Settings/autorun.bws") == False):
                if(os.path.exists("Settings/noauto.bws") == False):
                    autorun = input("Bash for Windows cannot find a autorun.bws file. Create one? (Y,n) ")
                    if((autorun == "n") or (autorun == "N")):
                        touch.write(["Settings/noauto.bws"])
                    else:
                        touch.write(["Settings/autorun.bws"])
                        print("autorun.bws file has been placed inside of the Bash/Bash/Settings folder.")
                        edit = input("Would you like to modify the autorun.bws file? (Y,n) ")
                        if((edit != "n") and (edit != "N")):
                            nano.write(["Settings/autorun.bws"])
                            file = open("Settings/autorun.bws", "r")
                            autoRun(str(file.read()))
                            file.close()
            else:
                file = open("Settings/autorun.bws", "r")
                autoRun(str(file.read()))
                file.close()

            if(bash.run() == 0):
                if(systemvariables.read("restart") == 1):
                    os.chdir(systemvariables.read("tmppath"))
                    file = open("lastcwd.bws", "r")
                    todir = file.read()
                    file.close()
                    systemvariables.modifyVoid("startDir", str(todir))
                    continue
            break