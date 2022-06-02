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

# mv is a file to move files or rename files, as a new file to help with multiple arguments

# Library
import os

# Main Function
def move(file, dstfile):
    holder = ""
    i = 0
    j = 0
    if((dstfile == "..") or (dstfile == "../")):
        dstfile = "../" + file
    if(os.path.isdir(dstfile) == True):
        dstfile = dstfile + "/" + file
    if(dstfile.find("/") != -1):
        holder = dstfile.split("/")[0]
    if(os.path.exists(file) == True):
        if(os.path.isdir(holder) == True):
            os.rename(file, dstfile)
        else:
            if(holder != ""):
                print("mv: cannot move '" + file + "' to '" + dstfile + "': No such file or directory")
            else:
                os.rename(file, dstfile)
    else:
        print("mv: cannot stat '" + file + ": No such file or directory")