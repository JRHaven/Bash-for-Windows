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
# rm is a basic script that removes a file

# Libraries
import os
import shutil
import ls
import systemvariables

# Main Function. First get a listing of the directory from the ls script
def remove(args):
    directory = ls.list()
    i = 0
    m = 0
    n = 0
    if("-r" in args):
        lastIndex = len(args) - 1
        if(args[0] == "-r"):
            args.pop(0)
            for j in args:
                file = args[i]
                if(os.path.exists(file)):
                    # Make sure it's' a directory
                    if(os.path.isdir(file) == True):
                        if(os.getcwd() == systemvariables.HOME):
                            if(file == "Documents"):
                                force = input("rm: remove write-protected directory '" + file + "'? ")
                                if((force == "y") or (force == "Y")):
                                    shutil.rmtree(file)
                            else:
                                shutil.rmtree(file)
                        else:
                            shutil.rmtree(file)
                    else:
                        print("rm: cannot remove '" + file + ": No such file or directory")
                else:
                    print("rm: cannot remove '" + file + ": No such file or directory")
                i += 1
        elif(args[lastIndex] == "-r"):
            args.pop(lastIndex)
            for j in args:
                file = args[i]
                if(os.path.exists(file)):
                    # Make sure it isn't a directory
                    if(os.path.isdir(file) == True):
                        shutil.rmtree(file)
                    else:
                        os.remove(file)
                else:
                    print("rm: cannot remove '" + file + ": No such file or directory")
                i += 1
    else:
        for j in args:
            file = args[i]
            # If it exists, remove it. If not, display a message
            if(os.path.exists(file)):
                # Make sure it isn't a directory
                if(os.path.isfile(file) == True):
                    os.remove(file)
                else:
                    print("rm: cannot remove '" + file + ": Is a directory")
            else:
                print("rm: cannot remove '" + file + ": No such file or directory")
            i += 1