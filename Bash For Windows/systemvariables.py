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
# systemvariables holds all variables open to all parts of the system who import them. The variables can be set, modified,
# and read depending on what a script may need to do with them. The end user may only see what are in the variables through
# means of the lsvars and echo commands.

# Import the OS library
import os

# Put any arrays seperately, we cannot handle arrays in the dynamic format of variables.
directorystack = ["","","","","","","",""]

# Universal color class to print color and bold text
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

varsNames = []
varConts = []

def lookupIndex(name):
    j = 0
    for i in varsNames:
        if(i == name):
            return j
        j += 1
    return -1

def read(name):
    i = lookupIndex(name)
    if(i == -1):
        return -1
    else:
        # Show Debug Messages if it's enabled. To avoid endless looping, don't do this
        # if the name given is debugMsg.
        if(name != "debugMsg"):
            if(read("debugMsg") == 1):
                print(color.YELLOW + color.BOLD + "[Debug]" + color.END + " Var Read. Name:", name)
        return varConts[i]

def modify(name, conts):
    i = lookupIndex(name)
    if(i == -1):
        return -1
    else:
        oldVar = read(name)
        varConts[i] = conts

        # Debug Message
        if(read("debugMsg") == 1):
            print(color.YELLOW + color.BOLD + "[Debug]" + color.END + " Var Modify. Name:", name, "\nOld Value:", oldVar, "New Value:", conts)
        return 0

def modifyVoid(name, conts):
    if(modify(name, conts) == -1):
        init(name, conts)

def init(name, conts):
    if(lookupIndex(name) != -1):
        # Debug Message
        if(read("debugMsg") == 1):
            print(color.YELLOW + color.BOLD + "[Debug]" + color.END + " Init Exists! Modifying instead. Name:", name)
        modify(name, conts)
    else:
        # Debug Message
        if(read("debugMsg") == 1):
            print(color.YELLOW + color.BOLD + "[Debug]" + color.END + " New Init! Name:", name, "Value:", conts)
        varsNames.append(name)
        varConts.append(conts)



# This will hold universal data set by me and not (easily) changed by the system
class fixedData:
    verStr = "2.1"
    verNum = 2.1
    inDev = False

    # An update ver.bws function
    def updateVer(verStr):
        oldPWD = os.getcwd()
        if(lookupIndex("settingspath") != -1):
            os.chdir(read("settingspath") + "/Settings")
            verbws = open("ver.bws", "w")
            # Change Below Tambien!!!
            verbws.write(verStr)
            # Change Above Tambien!!!
            verbws.close()
            os.chdir(oldPWD)