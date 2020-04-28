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
import os, username, ls, cd, systemvariables, pwd, socket, cat, apt
import echo, nano, touch, rm, filechk, cp, pushd, popd

# Main function. First Set all other system variables
def run():
    os.chdir(systemvariables.exepath)
    os.chdir("../../../../")
    systemvariables.ROOT = os.getcwd()
    os.chdir("Bash/Users/" + systemvariables.usrsession)
    systemvariables.HOME = os.getcwd()
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
    zzz = 1
    
    # Get user name
    cd.go("/")
    user = open("Bash/Bash/Settings/ivhzadgz.bws", "r")
    usr = user.read()
    user.close()
    
    # Get back to "Home" folder
    cd.go("~")

    # Reset the lastdir variable
    systemvariables.lastdir = ""

    # Do this until told to exit
    while(zzz == 1):
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
        arg1 = ""

        # Counters
        i = 0
        j = 0
        k = 0

        # Only do it if there is indeed a space
        if(args != -1):
            for i in command:
                # Only do this after a space
                if(k > args):
                    # Put what we are looking at in the arg1 variable, delete the character
                    arg1 = arg1 + i
                    command = command[0 : k : ]
                else:
                    k += 1
        
        # Reset a counter
        i = 0

        # If we have at least 1 space, make sure you take out the last character
        # in the command variable that happens to be a space
        if(args != -1):
            command = command[:-1:]
        
        # Run the command. If it dosen't exist, display a message
        if(command == "exit"):
            zzz = 0
        elif(command == "ls"):
            ls.show()
        elif(command == "cd"):
            cd.go(arg1)
        elif(command == "pwd"):
            print(os.getcwd())
        elif(command == "cat"):
            cat.show(arg1)
        elif(command == "nano"):
            file = arg1
            nano.write(file) 
        elif(command == "clear"):
            os.system("cls")
        elif(command == "sudo apt install"):
            install = arg1
            apt.install(install)
        elif(command == "lsvar"):
            ls.vars()
        elif(command == "echo"):
            echo.reg(arg1)
        elif(command == "touch"):
            touch.write(arg1)
        elif(command == "rm"):
            rem = arg1
            rm.remove(rem)
        elif(command == "mv"):
            file = arg1
            dstfile = arg1
            if(filechk.check(file) == True):
                os.rename(file, dstfile)
            else:
                print("mv: The file", file, "dosen't exist so not moved!")
        elif(command == "cp"):
            file = arg1
            newfile = arg1
            cp.copy(file, newfile)
        elif(command == "pushd"):
            path = arg1
            pushd.go(path)
        elif(command == "popd"):
            popd.go()
        else:
            if(command == ""):
                sleep(0)
            else:
                if(os.path.exists(os.getcwd() + "/" + command) == True):
                   typee = arg1
                   if(typee == "exe"):
                       os.system(command)
                   elif(typee == "py"):
                       os.system("py " + command)
                   else:
                        print("Bash for Windows does not know how to handle this. To give Bash for Windows a definition of what to do, make a setting for it.")
                else:
                    print(command + ": command not found")
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
