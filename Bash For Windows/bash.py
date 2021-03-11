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
# Bash is the script that handles the commands. Most commands it will call on other scripts to get the job done

# Libraries
from time import sleep
import os, username, ls, cd, systemvariables, pwd, socket, cat
import echo, nano, touch, rm, filechk, cp, pushd, popd, mkdir
import mv, oschk, repair, tofile, uname, date, script

def runcmd(command):
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
    
    # If the value set in the system variable "varTrans" is set to true, then replace all
    # variables with their values. First, make sure it exists.
    varTrans = systemvariables.read("varTrans")
    j = 0
    l = 0
    i = 0
    if(varTrans != -1):
        if(varTrans == 1):
            for i in argsArr:
                var = 0
                varNam = ""
                k = ""
                for k in argsArr[j]:
                    # If this is the first character and it is a $, we are setting up to look
                    # at a possible variable.
                    if((l == 0) and (k == "$")):
                        var = 1
                        l += 1
                        continue
                    if((l >= 0) and (var != 1)):
                        break
                    else:
                        varNam = varNam + k
                # Check to make sure the variable called for exists. If it does, set this argument
                # to be the value in the variable.
                if(systemvariables.read(varNam) != -1):
                    argsArr[j] = systemvariables.read(varNam)
                j += 1
    
    # Commands
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
    elif(command == "date"):
        date.show(argsArr)
    else:
        if(argsArr[0] == "="):
            if(systemvariables.lookupIndex(command) == -1):
                systemvariables.init(command, argsArr[1])
            else:
                systemvariables.modifyVoid(command, argsArr[1])
        else:
            dirContents = ls.list()
            if(command == ""):
                sleep(0)
            elif(command in dirContents):
                if(".bwsh" in command):
                    if(os.path.exists(command) == True):
                        scriptContents = open(command, "r")
                        script.run(str(scriptContents.read()))
                        scriptContents.close()
                    else:
                        print(command + ": command not found")
                else:
                    print(command + ": command not found")
            else:
                print(command + ": command not found")


# Main function. First Set all other system variables
def run():
    # Check once again to make sure we are running Windows
    oschk.check()
    os.chdir(systemvariables.read("exepath"))
    os.chdir("../../../../")
    systemvariables.init("ROOT", os.getcwd())
    os.chdir("Bash/Users/" + systemvariables.read("usrsession"))
    systemvariables.init("HOME", os.getcwd())
    if(os.path.exists("Documents") == False):
        print("Unfortunatly, Bash for Windows cannot find your documents.")
        prompt = input("Do you want to try to repair the problem? [Y,n] ")
        if(prompt == "n"):
            print("Abort.")
            systemvariables.init("USRDOCS", "null")
        elif(prompt == "N"):
            print("Abort.")
            systemvariables.init("USRDOCS", "null")
        else:
            success = repair.docs()
            if(success == True):
                os.chdir("Documents")
                systemvariables.init("USRDOCS", os.getcwd())
    else:
        os.chdir("Documents")
        systemvariables.init("USRDOCS", os.getcwd())
    os.chdir(systemvariables.read("settingspath"))
    systemvariables.modify("settingspath", os.getcwd())
    os.chdir("Settings")
    systemvariables.init("loginfopath", os.getcwd())
    os.chdir("../Source")
    systemvariables.init("srcpath", os.getcwd())
    os.chdir("../../Users")
    systemvariables.init("usrpath", os.getcwd())
    os.chdir("..")
    systemvariables.init("bshpath", os.getcwd())

    # Figure out whether to enable functionality
    os.chdir(systemvariables.read("loginfopath"))
    # If the prompt.bws file doesn't exist, call on repair script to initialize one.
    if(os.path.exists("prompt.bws") == False):
        if(repair.promptInit() == 1):
            os.system("cls")
            print("Bash for Windows has run into a non-critical error:\nVARTRANSLATE_NOT_ACCESSABLE\n\n\
This is not a critical error, so Bash for Windows will continue to work ok,\nminus some optional \
functionality.")
            choice = input("Do you want to contnue using Bash for Windows? [y,N] ")
            if(choice.upper() != "Y"):
                exit(1)
            # Initialize variables with default values
            systemvariables.init("varTrans", False)
    else:
        # Store the contents of the prompt.bws file into memory
        file = open("prompt.bws", "r")
        promptConfigTxt = file.read()
        file.close()
        txtOnLine = [""]
        j = 0

        # Store each line of text in an array
        for i in promptConfigTxt:
            if(i == "\n"):
                txtOnLine.append("")
                j += 1
                continue
            txtOnLine[j] = txtOnLine[j] + i
        # Seperate each value with equals sign and put them in a system variable, unless it has
        # a # as it's first character
        j = 0
        l = 0
        for i in txtOnLine:
            varNam = ""
            varConts = ""
            shift = 0
            l = 0
            for k in txtOnLine[j]:
                if((l == 0) and (k == "#")):
                    break
                if(k == "="):
                    shift = 1
                    continue
                if(shift == 0):
                    varNam = varNam + k
                else:
                    varConts = varConts + k
                l += 1
            if(varNam != ""):
                systemvariables.init(varNam, varConts)
            j += 1
        
        # The varTrans variable's value should be converted into an integer.
        if((systemvariables.read("varTrans") == "1")):
            systemvariables.modifyVoid("varTrans", 1)
        else:
            if(systemvariables.read("varTrans") != -1):
                systemvariables.modifyVoid("varTrans", 0)

    # Get user name
    cd.go("/")
    user = open("Bash/Bash/Settings/ivhzadgz.bws", "r")
    usr = user.read()
    user.close()
    
    # Get back to "Home" folder
    cd.go("~")

    # Reset the lastdir variable
    systemvariables.modify("lastdir", "")

    # If the user has used Ctrl + C, quit without crashing
    try:
        # Do this until told to exit
        while(True):
            # Change display depending on where the user is in the file system
            if(os.getcwd() == systemvariables.read("ROOT")):
                display = "/"
            elif(os.getcwd() == systemvariables.read("HOME")):
                display = "~"
            elif(os.getcwd() == systemvariables.read("USRDOCS")):
                display = "~/Documents"
            elif(os.getcwd() == systemvariables.read("settingspath")):
                display = "/Bash/Bash"
            elif(os.getcwd() == systemvariables.read("loginfopath")):
                display = "/Bash/Bash/Settings"
            elif(os.getcwd() == systemvariables.read("srcpath")):
                display = "/Bash/Bash/Source"
            elif(os.getcwd() == systemvariables.read("usrpath")):
                display = "/Bash/Users"
            elif(os.getcwd() == systemvariables.read("exepath")):
                display = "/Bash/Bash/Source/Include"
            elif(os.getcwd() == systemvariables.read("bshpath")):
                display = "/Bash"
            else:
                display = os.getcwd()
                
            # Prompt
            command = input(usr + "@" + socket.gethostname() + ":" + display + " $ ")

            # Run the command using the function above.
            runcmd(command)
    except KeyboardInterrupt:
        # If the program gets a interrupt, exit without crashing
        exit()