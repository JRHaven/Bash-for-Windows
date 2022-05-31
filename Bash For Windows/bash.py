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
# Bash is the script that handles the commands. Most commands it will call on other scripts to get the job done

# Libraries
from time import sleep
import os, username, ls, cd, pwd, socket, cat
import echo, nano, touch, rm, filechk, cp, pushd, popd, mkdir
import mv, repair, tofile, uname, date, script, shutil
import systemvariables as svar

def runcmd(command):
    # Find a space. If one is found, put it in another variable.
    args = command.find(" ", 0, len(command))
    argsArr = ['']

    # Counters
    i = 0
    j = 0

    # We're going to need this for varTrans later!
    varsQ = command.find("$")

    # Get an array of arguments from the command the user entered
    if(args != -1):
        argsArr = command.split(" ")
    
    # Set the command to be the actual command that was typed in, not the whole string
    # the user typed. That would be very cluttered and hard to work with.
    if(args != -1):
        command = argsArr[0]

    # Take off the command. That isn't really needed in are array of arguments.
    argsArr = argsArr[1::]
    if(len(argsArr) == 0):
        argsArr.append("")
    
    # If the value set in the system variable "varTrans" is set to true, then replace all
    # variables with their values. First, make sure it exists.
    varTrans = svar.read("varTrans")

    if(varTrans != -1):
        if(varsQ != -1):
            for i in argsArr:
                if(i[0] == "$"):
                    varnam = i.split("$")[1]
                    if(svar.lookupIndex(varnam) != -1):
                        argsArr[j] = svar.read(varnam)

    # Give the list of arguments in a debug string if the user wanted in the prompt.bws file
    if(svar.read("debugMsg") == 1):
        print(svar.color.YELLOW + svar.color.BOLD + "[Debug]" + svar.color.END + " Arguments: " + str(argsArr))
    
    # Commands
    if(command == "exit"):
        os.chdir(svar.read("tmppath"))
        conts = ls.list()
        for i in conts:
            try:
                if(os.path.isfile(i) == True):
                    os.remove(i)
                elif(os.path.isdir(i) == True):
                    shutil.rmtree(i)
                else:
                    continue
            except Exception as e:
                print("Bash for Windows has run into a non-critical issue: TMP_DEL_ERR\nThe Error message is:\
\n" + str(e), "\nThis occured while deleting file", i, "in the temp directory.\nPress Enter to Continue...")
                input("")
                continue
        print("Goodbye!")
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
    elif(command == "update-bws-ver"):
        print("Updating the ver.bws file to version", svar.fixedData.ver + "...")
        svar.fixedData.updateVer()
        print("...done")
    elif(command == "restart"):
        # Debug Message
        if(svar.read("debugMsg") == 1):
            print(svar.color.YELLOW + svar.color.BOLD + "[Debug]" 
+ svar.color.END + " Bash: Restarting!")

        # Save current directory
        cwd = os.getcwd()
        os.chdir(svar.read("tmppath"))
        file = open("lastcwd.bws", "w")
        file.write(str(cwd))
        file.close()
        svar.modifyVoid("restart", 1)
        return 0
    else:
        if(argsArr[0] == "="):
            if(svar.lookupIndex(command) == -1):
                svar.init(command, argsArr[1])
            else:
                svar.modifyVoid(command, argsArr[1])
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
    # Debug Message
    if(svar.read("debugMsg") == 1):
        print(svar.color.YELLOW + svar.color.BOLD + "[Debug]" + 
svar.color.END + " Bash: Starting!")
    os.chdir(svar.read("exepath"))
    os.chdir("../../../../")
    svar.init("ROOT", os.getcwd())
    os.chdir("Bash/usrdata/")
    svar.init("HOME", os.getcwd())
    if(os.path.exists("Documents") == False):
        os.mkdir("Documents")
        os.chdir("Documents")
        svar.init("USRDOCS", os.getcwd())
    else:
        os.chdir("Documents")
        svar.init("USRDOCS", os.getcwd())
    os.chdir(svar.read("settingspath"))
    svar.modify("settingspath", os.getcwd())
    os.chdir("Settings")
    svar.init("loginfopath", os.getcwd())
    os.chdir("../Source")
    svar.init("srcpath", os.getcwd())
    os.chdir("../../usrdata")
    svar.init("usrpath", os.getcwd())
    os.chdir("..")
    svar.init("bshpath", os.getcwd())
    # Debug Message
    if(svar.read("debugMsg") == 1):
        print(svar.color.YELLOW + svar.color.BOLD + "[Debug]" 
+ svar.color.END + " Bash: " + os.getcwd())
    os.chdir("temp")
    svar.init("tmppath", os.getcwd())
    os.chdir("..")

    # If we want to restart Bash for Windows, we'll need this variable.
    svar.modifyVoid("restart", 0)

    # Get user name
    cd.go("/")
    user = open("Bash/Bash/Settings/ivhzadgz.bws", "r")
    usr = user.read()
    user.close()
    
    # Get back to "Home" folder
    cd.go("~")

    # If the system variable for the last directory exists, go to that directory
    # (in case of restart)
    if(svar.read("startDir") != -1):
        os.chdir(svar.read("startDir"))

    # Reset the lastdir variable
    svar.modify("lastdir", "")

    # If the user has used Ctrl + C, quit without crashing
    try:
        # Do this until told to exit
        while(True):
            # Change display depending on where the user is in the file system
            if(os.getcwd() == svar.read("ROOT")):
                display = "/"
            elif(os.getcwd() == svar.read("HOME")):
                display = "~"
            elif(os.getcwd() == svar.read("USRDOCS")):
                display = "~/Documents"
            elif(os.getcwd() == svar.read("settingspath")):
                display = "/Bash/Bash"
            elif(os.getcwd() == svar.read("loginfopath")):
                display = "/Bash/Bash/Settings"
            elif(os.getcwd() == svar.read("srcpath")):
                display = "/Bash/Bash/Source"
            elif(os.getcwd() == svar.read("usrpath")):
                display = "/Bash/usrdata"
            elif(os.getcwd() == svar.read("exepath")):
                display = "/Bash/Bash/Source/Include"
            elif(os.getcwd() == svar.read("bshpath")):
                display = "/Bash"
            else:
                display = os.getcwd()
                
            # Prompt. If color prompt is enabled, use color.
            if(svar.read("colorPrompt") == 1):
                command = input(svar.color.BOLD + 
svar.color.GREEN + usr + "@" + socket.gethostname() + svar.color.END + 
":" + svar.color.BOLD + svar.color.BLUE + display + svar.color.END + 
"$ ")
            else:
                command = input(usr + "@" + socket.gethostname() + ":" + display + "$ ")

            # Run the command using the function above.
            if(runcmd(command) == 0):
                return 0
    except KeyboardInterrupt:
        # If the program gets a interrupt, exit without crashing
        exit()