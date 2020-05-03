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
# nano is a basic script that opens a file in notepad. The nano script does NOT try to imitate the real GNU Nano
# text editor.

# Libraries
import os
import touch
import ls

# Main Function. First get a listing of the directory using the ls script
def write(args):
    theList = ls.list()
    i = 0
    # Find out if there is a file called the same as the input text. If not, create the file using the touch
    # script before opening notepad
    for j in args:
        filename = args[i]
        if(any(filename in s for s in theList)):
            os.system("notepad " + filename)
        else:
            giveArgs = [filename]
            touch.write(giveArgs)
            os.system("notepad " + filename)
        i += 1