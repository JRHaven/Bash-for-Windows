'''
Copyright 2022 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without 
limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions 
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.
'''

# This is the new install script, borrowing code from the old install script

import os, platform, time, shutil, zipfile

# We also need the requests library. Note that this library needs to be installed via pip.
import requests

if(__name__ != "__main__"):
    print("The installer is not meant to run as a library. Goodbye.")
    exit(1)

# From old install script
def cdCheck(directory):
    if(os.path.exists(directory) == True):
        os.chdir(directory)

def rmCheck(directory):
    if(os.path.exists(directory) == True):
        shutil.rmtree(directory)

def cancelMsg():
    print("Setup canceled. Goodbye.")
    exit(1)

# We'll need this in the future
originDir = os.getcwd()

try:
    if(platform.system() != "Windows"):
        print("This install script can only work on Windows. Installing Bash for Windows on anything but Windows is not reccommended.\n\
Setup cannot continue. Press Enter to Exit...")
        input("")
        exit(1)
except KeyboardInterrupt:
    cancelMsg()

print("Welcome to the Bash for Windows Setup Wizard!")
print("This is a piece of software under the MIT License that makes a bash-like\nenviornment under Windows\
 for people who don't want to use WSL or aren't\nable to run WSL.\nTo cancel setup, press Ctrl + C at any time.\n")

try:
    input("Press Enter to Continue... ")
except KeyboardInterrupt:
    cancelMsg()

os.system("cls")
print("\n\n\nThe following is the MIT License. If you do not agree with this license,\ndon't install Bash\
 for Windows.\n\n")
print("Copyright 2019-2022 Jeremiah Haven\n\
\n\
Permission is hereby granted, free of charge, to any person obtaining a copy of\n\
this software and associated documentation files (the \"Software\"), to deal in\n\
the Software without restriction, including without limitation the rights to use,\n\
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the\n\
Software, and to permit persons to whom the Software is furnished to do so,\n\
subject to the following conditions:\n\
\n\
The above copyright notice and this permission notice shall be included in all\n\
copies or substantial portions of the Software.\n\
\n\
THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n\
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS\n\
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\n\
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER\n\
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION \n\
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n")

try:
    accept = input("Do you accept the license above? [y,N] ")
    if(accept.lower() != "y"):
        os.system("cls")
        print("Thanks for your intrest in Bash for Windows. Goodbye!")
        time.sleep(3)
        cancelMsg()
except KeyboardInterrupt:
    cancelMsg()

os.system("cls")
offline = False
print("This installer can be an offline installer if it has the required files.")
print("Do you want to activate the offline installer? If so, you will need\n\
the Startup.exe and Bash-for-Windows-2.1.zip files in Setups's directory.\n")

try:
    offlineIn = input("Enable offline mode? [N,y] ")
    if(offlineIn.lower() == "y"):
        offline = True
        
        while(True):
            # Check for files and alert user if they aren't found
            print("Checking for necessary files...")
            if(os.path.exists("Startup.exe") == False):
                print("ERROR: Setup cannot find the Startup.exe file.\nIf you haven't downloaded it already, you can \
download it from https://github.com/JR-Tech-and-Software/Bash-for-Windows/releases/tag/2.1\n \n\
in the \"Stable Zips of Source Code for 2.1\" release.\nIf you have downloaded it already, make sure it is in \
the same directory as the installer with the same name you downloaded it as.\n")
                prompt = input("Press Enter to retry, or Q to return to online install ")
                if(prompt.lower() == "q"):
                    offline = False
                    break
            elif(os.path.exists("Bash-for-Windows-2.1.zip") == False):
                print("ERROR: Setup cannot find the Bash-for-Windows-2.1.zip file.\nIf you haven't downloaded it already, you can \
download it from https://github.com/JR-Tech-and-Software/Bash-for-Windows/releases/tag/2.1\n\
in the \"Stable Zips of Source Code for 2.1\" release.\nIf you have downloaded it already, make sure it is in \
the same directory as the installer with the same name you downloaded it as.\n")
                prompt = input("Press Enter to retry, or Q to return to online install ")
                if(prompt.lower() == "q"):
                    offline = False
                    break
            else:
                break
    else:
        # Check for an internet connection (using GitHub)
        print("Checking for an Internet Connection...")
        try:
            requests.head("https://github.com", timeout=10)
            print("...connected!")
        except requests.ConnectionError:
            print("ERROR: Cannot establish a connection to GitHub. Check your internet connection, then restart Setup.")
            time.sleep(10)
            cancelMsg()
    

    os.system("cls")
    path = ""
    while(True):
        print("Which personal folder do you want to install Bash for Windows into?")
        userName = os.environ.get("USERNAME")
        folder = input("")
        path = "C:\\Users\\" + userName + "\\" + folder
        if(os.path.exists("C:\\Users\\" + userName + "\\" + folder) == True):
            break
        else:
            print("\nFolder,", folder + ", doesn't exist.\n")
    path = path + "\\Bash for Windows"

    os.system("cls")
    print("What kind of Installation do you want?\n")
    print("(N)ormal Installation : Full installation with all the code intact")
    print("(M)inimal Installation: Only copy over Startup.exe, then continue to setup\nthe User Account\n")
    mN = input("[m,N] ")
    normalInstall = True
    if(mN.lower() == "m"):
        normalInstall = False
    
    os.system("cls")
    print("INSTALLATION SUMMARY:")
    if(offline == True):
        print("Performing an Offline Install")
    else:
        print("Performing a Net Install")
    
    if(normalInstall == False):
        print("Minimal Installation Chosen")
    else:
        print("Normal Installation Chosen")
    
    print("Installing Bash for Windows to:", path + "\n")
    print("Are you sure you want to install Bash for Windows?")
    confirm = input("[y,N] ")
    if(confirm.lower() != "y"):
        cancelMsg()
    
    # Get Folder Structure All Chill
    if(os.path.exists(path) == True):
        print("Bash for Windows Setup Wizard has detected that there is already an install at\n" + path + " .\n")
        confirm = input("Do you want Bash for Windows to overwrite this installation? [y,N] ")
        if(confirm.lower() == "y"):
            try:
                os.chdir(path)
                cdCheck("Bash")
                cdCheck("Bash")
                rmCheck("Users")
                cdCheck("Source")
                rmCheck("Include")
                os.chdir(path)
                cdCheck("Bash")
                cdCheck("Bash")
                rmCheck("Settings")
                rmCheck("Source")
                os.chdir(path + "/..")
                shutil.rmtree(path)
            except PermissionError:
                os.system("cls")
                print("ERROR: Setup cannot delete the old Bash for Windows Installation. It either does")
                print("not have permission to do so or another process is currently using it. Make sure")
                print("that you have permission to do things in this folder and that there isn't already")
                print("a program using this folder, e.g. File Explorer, and start Setup again.")
                input("Press Enter to Cancel...")
                os.system("cls")
                cancelMsg()
        else:
            print("Bash for Windows cannot continue. Goodbye!!!")
            time.sleep(5)
            cancelMsg()
        
        os.system("cls")
        print("Installing Bash for Windows. This does not take long.\nIf Installation fails, delete:\n" + path + "\n" + "\
and run setup again. To cancel, hit Ctrl + C.\n")
        time.sleep(1)

        # Now to get on with the installation! Download files if requested
    if(offline == False):
        print("Downloading Files...")

        # What we should do if a file called "Startup.exe" or "Bash-for-Windows-2.1.zip" already exists
        if(os.path.exists("Startup.exe") == True):
            print("There is already a Startup.exe file! Do you want to replace it (d) or rename it (RN)?")
            prompt = input("[RN,d] ")
            if(prompt.lower() == "d"):
                os.remove("Startup.exe")
                print("OK, Startup.exe has been deleted to make way for the new one.")
            else:
                os.rename("Startup.exe", "OldStartup.exe")
                print("OK, Startup.exe has been renamed to OldStartup.exe")
        
        if(normalInstall == True):
            if(os.path.exists("Bash-for-Windows-2.1.zip") == True):
                print("There is already a Bash-for-Windows-2.1.zip file! Do you want to replace it (d) or rename it (RN)?")
                prompt = input("[RN,d] ")
                if(prompt.lower() == "d"):
                    os.remove("Bash-for-Windows-2.1.zip")
                    print("OK, Bash-for-Windows-2.1.zip has been deleted to make way for the new one.")
                else:
                    os.rename("Bash-for-Windows-2.1.zip", "Old-Bash-for-Windows-2.1.zip")
                    print("OK, Bash-for-Windows-2.1.zip has been renamed to Old-Bash-for-Windows-2.1.zip")
        
        # Now Download Files
        os.chdir(originDir)
        startupGet = requests.get("https://github.com/JR-Tech-and-Software/Bash-for-Windows/releases/download/2.1/Startup.exe")
        with open("Startup.exe", "wb") as file:
            file.write(startupGet.content)
            file.close()
        
        if(normalInstall == True):
            sourceGet = requests.get("https://github.com/JR-Tech-and-Software/Bash-for-Windows/archive/refs/tags/2.1.zip")
            with open("Bash-for-Windows-2.1.zip", "wb") as file:
                file.write(sourceGet.content)
                file.close()
        
    # Now to create folder structures
    print("Creating Directory Structure...")
    os.chdir(path + "\\..")
    os.mkdir("Bash for Windows")
    os.chdir("Bash for Windows")
    os.mkdir("Bash")
    os.mkdir("Bash/Bash")
    os.mkdir("Bash/usrdata")
    os.mkdir("Bash/usrdata/Documents")
    os.mkdir("Bash/Bash/Settings")
    os.mkdir("Bash/Bash/Source")
    os.mkdir("Bash/Bash/Source/Include")
    os.chdir("Bash/Bash/Source/Include")
    includeDir = os.getcwd()

    # Copy files over
    print("Copying Files...")
    shutil.copyfile((originDir + "/Startup.exe"), "./Startup.exe")

    # Unzip our zip file (if normal install is chosen)
    if(normalInstall == True):
        print("Extracting Source Code...")
        with zipfile.ZipFile(originDir + "/Bash-for-Windows-2.1.zip") as zip:
            zip.extractall()
        os.chdir("Bash-for-Windows-2.1/Bash For Windows")
        files = os.listdir(".")
        # Move each file to Include Directory
        for file in files:
            shutil.move(file, "../../" + file)
        # Remove unwanted crap
        os.chdir("../..")
        shutil.rmtree("Bash-for-Windows-2.1")
    
    # Config stage
    os.chdir(path + "/Bash/Bash/Settings")
    print("Configuring Installation")
    # Username stuffs
    while(True):
        usrnam = input("What do you want your username to be? ")
        if(usrnam != ""):
            break
        else:
            print("You should have a username.")
    with open("ivhzadgz.bws", "w") as file:
        file.write(usrnam)
    
    # Prompt.bws stuffs
    with open("prompt.bws", "w") as prompt:
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
        prompt.write("of your own variables under this first set of variables.\n")
        prompt.write("#debugMsg=1\n")
        prompt.write("#varTrans=1\n")
        prompt.write("#colorPrompt=1\n")
        prompt.write("#disableOSCheck=1\n")
        prompt.write("\n# Put your custom variables below:\n")
        prompt.close()
    
    # Autorun?
    if(input("Do you want an autorun.bws file? [Y,n] ").lower() == "n"):
        with open("noauto.bws", "w") as file:
            file.write("")
            file.close()
        print("OK. If you change your mind, delete the noauto.bws file in Bash/Bash/Settings\nand replace with an autorun.bws file.")
    else:
        with open("autorun.bws", "w") as file:
            file.write("")
            file.close()
        print("OK, autorun.bws file created in Bash/Bash/Settings.")
    time.sleep(3)
    
    # ver.bws stuffs
    with open("ver.bws", "w") as file:
        file.write("2.1")
        file.close()
    
    # Final readmes, shortcuts, all that stuffs
    print("Finalizing...")
    if(normalInstall == True):
        os.chdir("../../usrdata/Documents")
        with open("Modify_Code_Notes.txt", "w") as writeFile:
            writeFile.write("You have chosen a normal install, which includes all the code for you to modify.\n")
            writeFile.write("If you want to look at and/or modify the code, you may want to know how it works to\n")
            writeFile.write("more easily modify it. If you don't want to modify anything, you can simply delete this\n")
            writeFile.write("file.\n\n\n\n")
            writeFile.write("Here is a visual of how the user goes through the code including all files executed:\n")
            writeFile.write("execute: Startup.py\n")
            writeFile.write("             |\n")
            writeFile.write("             +----- Check to see if the file system is intact and if so, repair it\n")
            writeFile.write("             |                    |\n")
            writeFile.write("             |                    +---- repair.py\n")
            writeFile.write("             +----- Check if versions match up and deal with it if it doesn't\n")
            writeFile.write("             |\n")
            writeFile.write("          usrmgr.py\n")
            writeFile.write("             |\n")
            writeFile.write("             +---- Load Prompt.bws variables\n")
            writeFile.write("             |                    |\n")
            writeFile.write("             |     Do an OS check if not disabled in prompt.bws\n")
            writeFile.write("             |                    |\n")
            writeFile.write("             |                    +---- Not Windows?\n")
            writeFile.write("             |                    |            |\n")
            writeFile.write("             |                    |    Launch the actual bash\n")
            writeFile.write("             |\n")
            writeFile.write("             +----- Perform autorun commands, ask if file doesn't exist\n")
            writeFile.write("             |\n")
            writeFile.write("          bash.py\n")
            writeFile.write("             |\n")
            writeFile.write("             +---- Set some enviornment variables\n")
            writeFile.write("                                  |\n")
            writeFile.write("                                  +---- systemvariables.py\n")
            writeFile.write("                                  |\n")
            writeFile.write("                                  |<-------------------------+\n")
            writeFile.write("                                  |                          |\n")
            writeFile.write("                   Input Command and any arguments           |\n")
            writeFile.write("                                  |                          |\n")
            writeFile.write("                   Seperate Command from Arguments           |\n")
            writeFile.write("                                  |                          |\n")
            writeFile.write("                   Check command entered and check it against|list of commands\n")
            writeFile.write("                                  |                          |\n")
            writeFile.write("                                  +---- *.py                 |\n")
            writeFile.write("                                  |                          |\n")
            writeFile.write("                   Does the command match list of commands?  |\n")
            writeFile.write("                                  |                          |\n")
            writeFile.write("                                  +---- No?                  |\n")
            writeFile.write("                                         |                   |\n")
            writeFile.write("                               Display error message         |\n")
            writeFile.write("                                         |                   |\n")
            writeFile.write("                                         +-------------------+")
            writeFile.close()
        
    # Generate a shortcut lnk file
    os.chdir(path)
    os.mkdir("Temporary Install Files")
    os.chdir("Temporary Install Files")
    tmpInsFil = os.getcwd()
    writeFile = open("shortcut.bat", "w")
    writeFile.write("@echo off\n")
    writeFile.write("echo Set oWS = WScript.CreateObject(\"WScript.Shell\") > CreateShortcut.vbs\n")
    writeFile.write("echo sLinkFile = \"" + path + "\\Startup.lnk\" >> CreateShortcut.vbs\n")
    writeFile.write("echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs\n")
    writeFile.write("echo oLink.TargetPath = \"" + includeDir + "\\Startup.exe\" >> CreateShortcut.vbs\n")
    writeFile.write("echo oLink.Save >> CreateShortcut.vbs\n")
    writeFile.write("cscript CreateShortcut.vbs\n")
    writeFile.write("del CreateShortcut.vbs\n")
    writeFile.close()
    os.system("shortcut.bat > lnkout")

    # Generate Readme File
    os.chdir("..")
    writeFile = open("Readme.txt", "w")
    writeFile.write("==============================================\n")
    writeFile.write("   Bash for Windows: The Bourne Again SHell   \n")
    writeFile.write("==============================================\n")
    writeFile.write(" Welcome to Bash for Windows! First off:      \n")
    writeFile.write(" there isn't really any type of help          \n")
    writeFile.write(" document in Bash for Windows. Bash for       \n")
    writeFile.write(" Windows tries to work as much like the real  \n")
    writeFile.write(" Bash as possible, and as far as I can tell,  \n")
    writeFile.write(" there isn't any sort of help document in     \n")
    writeFile.write(" Bash that tells you commands. The closest    \n")
    writeFile.write(" thing there is to a help document is the man \n")
    writeFile.write(" page, which hasn't been implemented yet. If  \n")
    writeFile.write(" you want to learn Bash, Google is your       \n")
    writeFile.write(" friend.                                      \n")
    writeFile.write("==============================================\n")
    writeFile.write(" Bash for Windows is not exactly like Bash.   \n")
    writeFile.write(" It has taken many hours of my free time to   \n")
    writeFile.write(" get it to where it is today.                 \n")
    writeFile.write(" This being said, there are a few things that \n")
    writeFile.write(" work in Bash that don't work in Bash for     \n")
    writeFile.write(" Windows. A few of them are:                  \n")
    writeFile.write("  - Sudo doesn't execute things as            \n")
    writeFile.write("    Administrator                             \n")
    writeFile.write("  - No such thing as Apt, Dnf, Pacman, etc.   \n")
    writeFile.write("  - Many other commands in Bash don't work in \n")
    writeFile.write("    Bash for Windows                          \n")
    writeFile.write("==============================================\n")
    writeFile.write("            Scripting and autorun.bws         \n")
    writeFile.write("==============================================\n")
    writeFile.write(" When you first log into Bash for Windows,    \n")
    writeFile.write(" you will be prompted to create an autorun.bws\n")
    writeFile.write(" file. Don't feel forced to do this. This will\n")
    writeFile.write(" only be asked once. If you answer no, it will\n")
    writeFile.write(" remember to not ask to create an autorun.bws \n")
    writeFile.write(" file. If you change your mind, you can create\n")
    writeFile.write(" an autorun.bws file in the Bash/Bash/Settings\n")
    writeFile.write(" folder. If you choose to create an           \n")
    writeFile.write(" autorun.bws file, you will be asked if you   \n")
    writeFile.write(" want to start editing it immediatly. If so,  \n")
    writeFile.write(" it will open up notepad and you can start to \n")
    writeFile.write(" write commands to be run on startup.         \n")
    writeFile.write("                                              \n")
    writeFile.write(" The same code that makes autorun work will   \n")
    writeFile.write(" make scripting work. If you want to create a \n")
    writeFile.write(" script, the extension Bash for Windows looks \n")
    writeFile.write(" for is the .bwsh extension. As of version 2.0\n")
    writeFile.write(" Bash for Windows Scripting doesn't do much.  \n")
    writeFile.write(" I hope to improve this over time. But hey, at\n")
    writeFile.write(" least it's there! Remember, developers! Bash \n")
    writeFile.write(" for Windows is written exclusively in python \n")
    writeFile.write(" by a developer that only works on Bash for   \n")
    writeFile.write(" Windows in his free time!                    \n")
    writeFile.write("==============================================\n")
    writeFile.write("                  Prompt.bws                  \n")
    writeFile.write("==============================================\n")
    writeFile.write(" New in version 2.1 is the prompt.bws file.   \n")
    writeFile.write(" You can sort of think of the prompt.bws file \n")
    writeFile.write(" as the .bashrc file in regular bash. It is   \n")
    writeFile.write(" a place to adjust various settings in BFW and\n")
    writeFile.write(" create some of your own variables at Startup.\n")
    writeFile.write(" Some of the features that can be enabled in  \n")
    writeFile.write(" the prompt.bws file include debugMsg,        \n")
    writeFile.write(" varTrans, colorPrompt, and disableOSCheck.   \n")
    writeFile.write(" debugMsg will enable debug messages. You     \n")
    writeFile.write(" should probably run this in a command line   \n")
    writeFile.write(" that supports color, as the messages will be \n")
    writeFile.write(" in a yellow text color. colorPrompt will     \n")
    writeFile.write(" enable the ability for BFW to display things \n")
    writeFile.write(" in color, once again, only in supported      \n")
    writeFile.write(" terminals. varTrans will automatically       \n")
    writeFile.write(" replace all variable keywords with the       \n")
    writeFile.write(" contents of those variables before sending   \n")
    writeFile.write(" the arguments to the command. disableOSCheck \n")
    writeFile.write(" will disable the Operating System check, so  \n")
    writeFile.write(" it is now possible (not recommended) to run  \n")
    writeFile.write(" BFW on Linux and Mac by enabling this        \n")
    writeFile.write(" variable.                                    \n")
    writeFile.write("==============================================\n")
    writeFile.write(" Bash for Windows's code is avalible on       \n")
    writeFile.write(" GitHub! Either run uname -g from the prompt  \n")
    writeFile.write(" or go to https://bit.ly/2KPHRmu to look at   \n")
    writeFile.write(" the code behind Bash for Windows!            \n")
    writeFile.write("==============================================")
    writeFile.close()
    shutil.copyfile("Readme.txt", "Bash/usrdata/Documents/Readme.txt")

    # Final cleaning up
    os.chdir(path)
    shutil.rmtree("Temporary Install Files")
    time.sleep(1)
except KeyboardInterrupt:
    cancelMsg()

os.system("cls")
print("Bash for Windows Setup is Complete! To start Bash for Windows,\nExecute the Startup executable,\
 both in the base folder that you installed\nBash for Windows into and in Bash/Bash/Source/Include.\n")
try:
    input("Press Enter to Exit...")
    exit(0)
except KeyboardInterrupt:
    exit(0)