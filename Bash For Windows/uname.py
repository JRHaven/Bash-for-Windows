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
import platform, tofile, os

def list(args):
    output = ""
    if((args[0] == "") or (args[0] == ">") or (args[0] == ">>")):
        output = output + platform.system()
    elif((args[0] == "-r") or (args[0] == "--kernel-release")):
        output = output + platform.release()
    elif((args[0] == "-a") or (args[0] == "--all")):
        output = output + platform.system() + " " + platform.node() + " "\
            + platform.release() + " " + platform.version() + " " + platform.machine()\
            + " " + platform.processor()
    elif((args[0] == "-s") or (args[0] == "--kernel-name")):
        output = output + platform.system()
    elif((args[0] == "-n") or (args[0] == "--nodename")):
        output = output + platform.node()
    elif((args[0] == "-v") or (args[0] == "--kernel-version")):
        output = output + platform.version()
    elif((args[0] == "-m") or (args[0] == "--machine")):
        output = output + platform.machine()
    elif((args[0] == "-p") or (args[0] == "--processor")):
        output = output + platform.processor()
    elif((args[0] == "-o") or (args[0] == "--operating-system")):
        output = output + platform.system()
    elif((args[0] == "-i") or (args[0] == "--information") or (args[0] == "--version")):
        output = output + "Bash for Windows: The Bourne Again Shell! Version 2.0\n\nAll\
 the code is avalible at GitHub! Check it out! Use the -g argument to be taken to the page!\
\n\nBash for Windows is under the MIT License. Check it out on GitHub as well."
    elif((args[0] == "-g") or (args[0] == "--github")):
        output = output + "Bash for Windows: The Bourne Again Shell! Version 2.0\nTaking you to the GitHub page...\n"
        os.system("iexplore https://github.com/JR-Tech-and-Software/Bash-for-Windows")
    elif(args[0] == "--help"):
        output = output + "Bash for Windows: The Bourne Again Shell!\nuname updated for version 1.3\
\n\nUsage: uname [OPTION]\nPrints information about your computer. Arguments:\n\n-a, --all: Print\
all information in the other arguments to the screen\n-r, --kernel-release: Prints Kernel Release\
 Information to the screen\n-s, --kernel-name: Prints Kernel Name to the Screen\n-n, --nodename: \
Prints hostname to the Screen\n-v, --kernel-version: Prints System Version to the Screen\n-m, \
--machine: Prints information about your computer to the screen\n-p, --processor: Prints the type\
 of your processor to the screen\n-o, --operating-system: Prints the same information of -s\n-i, \
--information: Prints out information about Bash for Windows\n-g, --github: Takes you to the GitHub\
 Page of Bash for Windows\n--help: Prints this help screen"
    else:
        if((args[0] != ">") and (args[0] != ">>")):
            print("uname: extra operand ‘" + args[0] + "`: Try again with --help")
    tofile.write(args, output)
