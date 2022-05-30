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
# Startup is the file that starts off Bash For Windows. You can only run Bash for Windows with this script.

# Import libraries
from time import sleep
import platform, os, shutil
# If we are not in the right place, get us to the right place
if(os.path.exists(os.getcwd() + "/../Include") == False):
    os.chdir("Bash/Bash/Source/Include")
import bash, os.path, username, usrmgr, repair, systemvariables, time

# The commented out lines are for me to use for debugging purposes only.
#print(os.getcwd())
#print(os.path.dirname(os.path.realpath(__file__)))

# Check to make sure we are running on Windows and if not start bash
#if(platform.system() != "Windows"):
#    print("Bash for Windows has seen that you are not using Windows. Launching Bash...")
#    os.system("bash")
#    exit()

# Set a system variable
systemvariables.init("exepath", os.getcwd())
systemvariables.init("settingspath", systemvariables.read("exepath") + "/../..")
    
# Move to the root of the file structure
os.chdir(systemvariables.read("exepath") + "/../..")

os.chdir("../..")

# See if any folders are deleted and if they are attempt to fix it using the repair script
try:
    if(os.path.exists("Bash/usrdata") == False):
        choice = input("Unfortunatly, Bash for Windows could not find your data. Do you want to try to fix this with Bash for Windows Repair? [y, N] # ")
        if((choice == "y") or (choice == "Y")):
            repair.baseusrrepair()
        else:
            print("Abort.")
except KeyboardInterrupt:
    exit(0)

# Check if the temp directory exists. If not, create it.
if(os.path.exists("Bash/temp") == False):
    os.mkdir("Bash/temp")

# Go back to here so that we don't trigger an unneeded repair
os.chdir(systemvariables.read("settingspath") + "/../..")

os.chdir(systemvariables.read("settingspath") + "/Settings")
try:
    if(os.path.exists("ver.bws") == False):
        ver = open("ver.bws", "w")
        ver.write(systemvariables.fixedData.verStr)
        ver.close()
    else:
        ver = open("ver.bws", "r")
        verstr = ver.read()
        ver.close()
        
        if(verstr == ""):
            print("WARNING: Nothing found in ver.bws, so Bash for Windows doesn't know what version this is. \
The system may be unstable...")
            print("If you are certain every area of Bash for Windows is up to date, you can run the \"update-bws-ver\" command \
to update the version string")
            sleep(5)
        else:
            verNum = 0.0
            indev = False
            error = False
            if(len(verstr.split("d")) == 1):
                try:
                    verNum = float(verstr)
                except ValueError:
                    error = True
                    print("Bash for Windows has run into a non-critical issue: VER_CANNOT_CONVERT_FLOAT\nThis \
    probably happened because of an invalid version string. An invalid version string may be okay now , but may \
    cause problems in the future. To fix, you can try deleting the ver.bws file in the Bash/Bash/Settings folder.\n")
                    input("Press enter to continue...")
            else:
                verArr = verstr.split("d")
                indev = True
                try:
                    verNum = float(verArr[0])
                except ValueError:
                    error = True
                    print("Bash for Windows has run into a non-critical issue: VER_CANNOT_CONVERT_FLOAT\nThis \
    probably happened because of an invalid version string. An invalid version string may be okay now , but may \
    cause problems in the future. To fix, you can try deleting the ver.bws file in the Bash/Bash/Settings folder.\n")
                    input("Press enter to continue...")
        
            # Make needed changes to keep folder structure up to date, if we aren't already
            # To be moved to seperate script in the future
            if(error == False):
                if(verNum < 2.1):
                    print("Bash for Windows has changed for this version and changes need to take place \
to the folder structure of Bash for Windows for it to continue to be operational.\nIf you do not want Bash for \
Windows to touch your data, you can skip this operation for now. However, Bash for Windows will probably crash.\n\
It is highly recommended to let Bash for Windows proceed. To see what changes will be made, check the changelog on the GitHub.")
                    approval = input("Should Bash for Windows continue? [Y,n] ")
                    if(approval.lower() != "n"):
                        if(os.path.exists("ivhzadgz.bws") == False):
                            print("\nBash for Windows ran into an issue! The system could not find the username. Bash for Windows \
cannot continue. Abort.")
                            exit(1)
                        usr = open("ivhzadgz.bws", "r")
                        usrnam = usr.read()
                        usr.close()
                        os.chdir("../..")
                        shutil.copytree("Users/" + usrnam, "usrdata")
                        shutil.rmtree("Users")
                        os.system("cls")
                        print("System successfully migrated!")
                        systemvariables.fixedData.updateVer()
                        os.chdir("Bash/Settings")

except KeyboardInterrupt:
    exit(0)

# Go back to here so that we don't trigger an unneeded repair
os.chdir(systemvariables.read("settingspath") + "/../..")

# Call the login prompt
try:
    usrmgr.logon()
except KeyboardInterrupt:
    exit(0)
