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
# Bash is the script that handles the commands. Most commands it will call on other scripts to get the job done

# Libraries
from time import sleep
import os
import username
import ls
import cd
import systemvariables
import pwd
import socket
import cat
import apt
import echo
import nano
import touch
import rm
import filechk
import cp

# Main function. First Set all other system variables
def run():
    os.chdir(systemvariables.exepath)
    os.chdir("../../../../")
    systemvariables.ROOT = os.getcwd()
    os.chdir("Bash/Users/" + systemvariables.usrsession)
    systemvariables.HOME = os.getcwd()
    os.chdir("Documents")
    systemvariables.USRDOCS = os.getcwd()
    zzz = 1
    
    # Get user name
    cd.go("/")
    user = open("Bash/Bash/Settings/ivhzadgz.bws", "r")
    usr = user.read()
    user.close()
    
    # Get back to "Home" folder
    cd.go("~")
    while(zzz == 1):
        # Change display depending on where the user is in the file system
        if(os.getcwd() == systemvariables.ROOT):
            display = "/"
        elif(os.getcwd() == systemvariables.HOME):
            display = "~"
        elif(os.getcwd() == systemvariables.USRDOCS):
            display = "~/Documents"
        else:
            display = os.getcwd()
            
        # Prompt
        command = input(usr + "@" + socket.gethostname() + ":" + display + " $ ")
        
        # Run the command. If it dosen't exist, display a message
        if(command == "exit"):
            zzz = 0
        elif(command == "ls"):
            ls.show()
        elif(command == "cd"):
            cd.go(input(""))
        elif(command == "pwd"):
            print(pwd.get())
        elif(command == "cat"):
            cat.show(input(""))
        elif(command == "nano"):
            file = input("")
            nano.write(file) 
        elif(command == "clear"):
            os.system("cls")
        elif(command == "sudo apt install"):
            install = input("")
            apt.install(install)
        elif(command == "lsvar"):
            ls.vars()
        elif(command == "echo"):
            echo.reg(input(""))
        elif(command == "touch"):
            touch.write(input(""))
        elif(command == "rm"):
            rem = input("")
            rm.remove(rem)
        elif(command == "mv"):
            file = input("")
            dstfile = input("")
            if(filechk.check(file) == True):
                os.rename(file, dstfile)
            else:
                print("mv: The file", file, "dosen't exist so not moved!")
        elif(command == "cp"):
            file = input("")
            newfile = input("")
            cp.copy(file, newfile)
        else:
            if(command == ""):
                sleep(0)
            else:
                if(os.path.exists(os.getcwd() + "/" + command) == True):
                   typee = input("")
                   if(typee == "exe"):
                       os.system(command)
                   elif(typee == "py"):
                       os.system("py " + command)
                   else:
                        print("Bash for Windows does not know how to handle this. To give Bash for Windows a definition of what to do, make a setting for it.")
                else:
                    print('Bash: ' + command + " command not found")
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
