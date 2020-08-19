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
# usrmgr is a script responsable for the login prompt, the not-yet implemented multiple user function and
# welcoming the user into Bash For Windows. Despite not being the first script executed, this is the first
# time the user interacts with Bash For Windows.

# Libraries
import os
import repair
import bash, platform
import systemvariables, oschk, touch, nano

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

# Login Prompt
def logon():
    # Check again to make sure we are running Windows
    oschk.check()

    os.chdir(systemvariables.exepath)
    os.chdir("../../")
    incorrect = True
    while(incorrect == True):
        user = open("Settings/ivhzadgz.bws", "r")
        userguess = input("Type a user name # ")
        if(userguess == user.read()):
           incorrect = False
        else:
           print("Incorrect Username.")
    incorrect = True

    # Check double check to make sure we are running Windows
    #if(platform.system() != "Windows"):
    #    print("Bash for Windows has seen that you are not using Windows. Launching Bash...")
    #    os.system("bash")
    #    exit()
    
    while(incorrect == True):
        password = open("Settings/kvnnadgz.bws", "r")
        passguess = input("password # ")
        if(passguess == password.read()):
            incorrect = False
            systemvariables.usrsession = userguess
        else:
            print("Incorrect Password.")
    password.close()
    print("Welcome to Bash(the Bourne Again Shell) for Windows!")

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

    user.close()
    bash.run()
    
# Function for checking a password based on username provided
def checkpassword():
    session = systemvariables.usrsession
    user = ""
    incorrect = True
    if(os.path.exists("Settings/ivhzadgzzoneth.bws") == True):
        potentialusr1 = open("Settings/ivhzadgzzoneth.bws" + "r")
        if(session == potentialusr1.read()):
            user = "Settings/ivhzadgzzoneth.bws"
    potentialusr2 = open("Settings/ivhzadgz.bws", "r")
    if(session == potentialusr2.read()):
        user = "Settings/ivhzadgzzoneth.bws"
    else:
        user = "No User"
    if(user != "No User"):
        if(user == "Settings/ivhzadgzzoneth.bws"):
            while(incorrect == True):
                password = open("Settings/kvnnadgzzoneth.bws", "r")
                passguess = input("password # ")
                if(passguess == password.read()):
                    incorrect = False
                else:
                   print("Incorrect Password.")
        else:
            while(incorrect == True):
                password = open("Settings/kvnnadgz.bws", "r")
                passguess = input("password # ")
                if(passguess == password.read()):
                    incorrect = False
                else:
                    print("Incorrect Password.")
    else:
        logon()
