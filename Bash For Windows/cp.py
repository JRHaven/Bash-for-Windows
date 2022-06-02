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
# cp is a basic script that copies a file

# Libraries
import os

# Main Function. First checks if the file wanted exists, then call system command to copy
def copy(argsArr):
    length = len(argsArr) - 1
    if(argsArr[0] == ""):
        print("cp: missing file operand")
    elif(length < 1):
        print("cp: missing file operand after '" + argsArr[0] + "'")
    else:
        srcfile = argsArr[0]
        dstfile = argsArr[1]
        if((dstfile == "..") or (dstfile == "../")):
            dstfile = "../" + srcfile
        if(os.path.isdir(dstfile) == True):
            cmdstfile = dstfile
            dstfile = cmdstfile + "/" + srcfile
        if(os.path.exists(srcfile) == True):
            cmd = "copy " + srcfile  + " " + dstfile
            os.system(str(cmd))
        else:
            print("cp: cannot stat '" + srcfile + "': No such file or directory")