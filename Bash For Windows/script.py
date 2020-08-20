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
# script.py simply reads a script, processes it, and runs commands in the script.

# Library
import bash

def run(script):
    commands = [""]
    i = 0
    j = 0
    k = 0
    flag = 0
    for i in script:
        # If we come across a #, ignore that line by setting a flag until a newline character
        # is hit
        if(i == "#"):
            flag = 1
        
        # If we hit a new line and the flag is set, disable the flag
        if((i == "\n") and (flag == 1)):
            flag = 0

        # If flag is set, ignore everyting else
        if(flag == 1):
            continue

        # If we come across a ; or new line character, add an item to the array and skip the rest
        if((i == ";") or (i == "\n")):
            k += 1
            commands.append("")
            continue

        # Take the character and put it in the appropriate spot in the array.
        commands[k] = commands[k] + i
    i = 0
    j = 0
    for i in commands:
        bash.runcmd(commands[j])
        j += 1