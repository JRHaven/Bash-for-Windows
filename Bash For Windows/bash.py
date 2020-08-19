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
# Bash is the script that handles the commands. Most commands it will call on other scripts to get the job done

# Libraries
from time import sleep
import os, username, ls, cd, systemvariables, pwd, socket, cat
import echo, nano, touch, rm, filechk, cp, pushd, popd, mkdir
import mv, oschk, repair, tofile, uname

def runcmd(command, argsArr):
    if(command == "exit"):
        exit(0)
    elif(command == "ls"):
        ls.show(argsArr)
    elif(command == "cd"):
        cd.go(argsArr)
    elif(command == "pwd"):
        tofile.write(argsArr, os.getcwd())
    elif(command == "cat"):
        cat.show(argsArr)
    elif(command == "nano"):
        file = argsArr
        nano.write(file) 
    elif(command == "vi"):
        file = argsArr
        nano.write(file) 
    elif(command == "vim"):
        file = argsArr
        nano.write(file) 
    elif(command == "emacs"):
        file = argsArr
        nano.write(file) 
    elif(command == "clear"):
        os.system("cls")
    elif(command == "lsvar"):
        ls.vars(argsArr)
    elif(command == "echo"):
        echo.reg(argsArr)
    elif(command == "touch"):
        touch.write(argsArr)
    elif(command == "rm"):
        rm.remove(argsArr)
    elif(command == "mv"):
        file = argsArr[0]
        dstfile = argsArr[1]
        mv.move(file, dstfile)
    elif(command == "cp"):
        cp.copy(argsArr)
    elif(command == "pushd"):
        path = argsArr
        pushd.go(path)
    elif(command == "popd"):
        popd.go()
    elif(command == "uname"):
        uname.list(argsArr)
    elif(command == "mkdir"):
        mkdir.create(argsArr)
    else:
        if(command == ""):
            sleep(0)
        else:
            print(command + ": command not found")


# Main function. First Set all other system variables
def run():
    # Check once again to make sure we are running Windows
    oschk.check()
    os.chdir(systemvariables.exepath)
    os.chdir("../../../../")
    systemvariables.ROOT = os.getcwd()
    os.chdir("Bash/Users/" + systemvariables.usrsession)
    systemvariables.HOME = os.getcwd()
    if(os.path.exists("Documents") == False):
        print("Unfortunatly, Bash for Windows cannot find your documents.")
        prompt = input("Do you want to try to repair the problem? [Y,n] ")
        if(prompt == "n"):
            print("Abort.")
            systemvariables.USRDOCS = "null"
        elif(prompt == "N"):
            print("Abort.")
            systemvariables.USRDOCS = "null"
        else:
            success = repair.docs()
            if(success == True):
                os.chdir("Documents")
                systemvariables.USRDOCS = os.getcwd()
    else:
        os.chdir("Documents")
        systemvariables.USRDOCS = os.getcwd()
    os.chdir(systemvariables.settingspath)
    systemvariables.settingspath = os.getcwd()
    os.chdir("Settings")
    systemvariables.loginfopath = os.getcwd()
    os.chdir("../Source")
    systemvariables.srcpath = os.getcwd()
    os.chdir("../../Users")
    systemvariables.usrpath = os.getcwd()
    os.chdir("..")
    systemvariables.bshpath = os.getcwd()
    
    # Get user name
    cd.go("/")
    user = open("Bash/Bash/Settings/ivhzadgz.bws", "r")
    usr = user.read()
    user.close()
    
    # Get back to "Home" folder
    cd.go("~")

    # Reset the lastdir variable
    systemvariables.lastdir = ""

    # If the user has used Ctrl + C, quit without crashing
    try:
        # Do this until told to exit
        while(True):
            # Change display depending on where the user is in the file system
            if(os.getcwd() == systemvariables.ROOT):
                display = "/"
            elif(os.getcwd() == systemvariables.HOME):
                display = "~"
            elif(os.getcwd() == systemvariables.USRDOCS):
                display = "~/Documents"
            elif(os.getcwd() == systemvariables.settingspath):
                display = "/Bash/Bash"
            elif(os.getcwd() == systemvariables.loginfopath):
                display = "/Bash/Bash/Settings"
            elif(os.getcwd() == systemvariables.srcpath):
                display = "/Bash/Bash/Source"
            elif(os.getcwd() == systemvariables.usrpath):
                display = "/Bash/Users"
            elif(os.getcwd() == systemvariables.exepath):
                display = "/Bash/Bash/Source/Include"
            elif(os.getcwd() == systemvariables.bshpath):
                display = "/Bash"
            else:
                display = os.getcwd()
                
            # Prompt
            command = input(usr + "@" + socket.gethostname() + ":" + display + " $ ")

            # Find a space. If one is found, put it in another variable.
            args = command.find(" ", 0, len(command))
            argsArr = ['']

            # Counters
            i = 0
            j = 0
            k = 0
            flag = 0
            flag2 = 0

            # Only do it if there is indeed a space
            if(args != -1):
                for i in command:
                    # Only do this after a space
                    if(j > args):

                        # If the character is \, set a flag and remove the \. If not, turn off the flag
                        if(i == "\\"):
                            flag = 1
                            if(i == "\\"):
                                continue
                            
                        # If we come across a space, add an item to the array of arguments and skip the rest,
                        # unless the flag set before is set
                        if((i == " ") and (flag == 0)):
                            k += 1
                            argsArr.append("")
                            continue
                        elif((i == " " and (flag == 1))):
                            flag = 0

                        # Take the current item in the args array and put in each character of the input
                        # string, then delete that same character from the input string
                        argsArr[k] = argsArr[k] + i
                        command = command[0 : j : ]
                    else:
                        j += 1
            # Reset the counters
            i = 0
            j = 0
            k = 0

            # If we have at least 1 space, make sure you take out the last character
            # in the command variable that happens to be a space
            if(args != -1):
                command = command[:-1:]
            
            # Run the command. If it dosen't exist, display a message
            runcmd(command, argsArr)
    except KeyboardInterrupt:
        # If the program gets a interrupt, exit without crashing
        exit()

# More checking for other scripts to use
def usrcheck():
    incorrect = True
    while(incorrect == True):
        user = open("Settings/ivhzadgz.bws", "r")
        userguess = input("Type a user name # ")
        if(userguess == user.read()):
           incorrect = False
        else:
           print("Incorrect Username.")
    user.close()
def passcheck():
        incorrect = True
        while(incorrect == True):
            password = open("Settings/kvnnadgz.bws", "r")
            passguess = input("password # ")
            if(passguess == password.read()):
                incorrect = False
            else:
                print("Incorrect Password.")
        password.close()

# If the end user tries to run bash.py without Startup.py, then display this message
print("This file isn't ment to be run by itself. To run Bash for Windows,")
print("run the Startup program.")
