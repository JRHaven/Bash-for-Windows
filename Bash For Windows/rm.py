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
# rm is a basic script that removes a file

# Libraries
import os
import shutil
import ls
import systemvariables

# Main Function. First get a listing of the directory from the ls script
def remove(args):
    i = 0

    # Check for Wildcards
    wildCard = False
    wildIndex = []
    for j in args:
        if("*" in args[i]):
            wildCard = True
            wildIndex.append(i)
        i += 1
    
    # Figure out if the wildcard has a dot, if it is before dot, or after dot
    if(wildCard == True):
        dot = -1
        flag = 0
        k = 0
        l = 0
        m = 0
        i = 0
        for i in wildIndex:
            for j in args[i]:
                if(j == "*"):
                    l = k
                if(j == "."):
                    flag = 1
                    m = k
                k += 1
        if(flag == 0):
            dot = -1
        elif(l > m):
            dot = 1
        elif(l < m):
            dot = 0
                
    # Reset Variable
    i = 0
    if("-r" in args):
        lastIndex = len(args) - 1
        if(args[0] == "-r"):
            args.pop(0)
            for j in args:
                file = j
                if(os.path.exists(file) and os.path.isdir(file)):
                    shutil.rmtree(file)
                else:
                    print("rm: cannot remove '" + file + ": No such file or directory")
                i += 1
        elif(args[lastIndex] == "-r"):
            args.pop(lastIndex)
            for j in args:
                file = j
                if(os.path.exists(file) and os.path.isdir(file)):
                    shutil.rmtree(file)
                else:
                    print("rm: cannot remove '" + file + ": No such file or directory")
                i += 1
    else:
        for j in args:
            file = j

            # If it exists and is a file, remove it. If not, display a message
            if(os.path.exists(file)):
                # Make sure it isn't a directory
                if(os.path.isfile(file) == True):
                    os.remove(file)
                else:
                    print("rm: cannot remove '" + file + ": Is a directory")
            
            # If we found a wildcard before, do the following depending on where the dot is
            elif(wildCard == True):
                if(dot == -1):
                    # Remove all files in the directory
                    dirList = ls.list()
                    n = ""
                    for n in dirList:
                        if(os.path.isdir(n) == True):
                            print("rm: cannot remove '" + n + ": Is a directory")
                        else:
                            os.remove(n)
                elif(dot == 0):
                    # Remove all files with the extension we asked for
                    k = 0
                    flag = 0
                    ext = ""
                    n = ""
                    for n in args[k]:
                        if(k == l):
                            flag = 1
                            k += 1
                            continue
                        if(flag == 1):
                            ext = ext + n
                        k += 1
                    k = 0
                    n = ""
                    dirList = ls.list()
                    for n in dirList:
                        if(ext in n):
                            if(os.path.isdir(n) == True):
                                print("rm: cannot remove '" + n + ": Is a directory")
                            else:
                                os.remove(n)
                else:
                    # Remove all files with the filename we asked for
                    n = ""
                    k = 0
                    name = ""
                    for n in args[i]:
                        if(n == "."):
                            name = name + n
                            break
                        name = name + n
                    dirList = ls.list()
                    n = ""
                    for n in dirList:
                        if(name in n):
                            if(os.path.isdir(n) == True):
                                print("rm: cannot remove '" + n + ": Is a directory")
                            else:
                                os.remove(n)
            else:
                print("rm: cannot remove '" + file + ": No such file or directory")
            i += 1
