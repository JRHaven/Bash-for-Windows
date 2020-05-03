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

# mkdir simply makes directories, but is written as a seperate script to take advantage of multiple arguments

# Library
import os

def create(args):
    if("-p" in args):
        i = 0
        index = 0
        for j in args:
            if(args[i] == "-p"):
                index = i
                break
            i += 1
        if(index == 0):
            index += 1
        else:
            index -= 1
        path = args[index]
        i = 0
        j = ""
        k = 0
        directories = [""]
        for j in path:
            if(path[i] == "/"):
                directories.append("")
                k += 1
                i += 1
                continue
            directories[k] = directories[k] + j
            i += 1
        i = 0
        j = 0
        lastDir = os.getcwd()
        for j in directories:
            if(os.path.exists(j) == True):
                os.chdir(j)
            else:
                os.mkdir(j)
                os.chdir(j)
        os.chdir(lastDir)
    else:
        i = 0
        for j in args:
            os.mkdir(args[i])
            i += 1