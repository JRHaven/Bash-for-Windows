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
# Cat is a basic script to show the contents of a file

# Libraries
import os, touch, rm, tofile

# Main Function. First check if the file exists
def show(args):
    # Get the file to print out from our array of arguments
    file = args[0]
    output = ""
    firstLetter = ""
    flag = 0
    # Make sure the requested file exists and is indeed a file and not a folder.
    if(os.path.exists(file) == False):
        print("cat: " + file + " file not found")
    elif(os.path.isdir(file) == True):
        print("cat: " + file + ": Is a directory")
    else:
        show = open(file)
        output = show.read()
        show.close()
        # If told to do so, either append or overwrite a file where we send all output to
        if(">>" in args):
            i = 0
            index = 0
            flag = 1
            for j in args:
                if(i == 0):
                    i += 1
                    continue
                if(args[i] == ">>"):
                    index = i + 1
                    break
                i += 1
            tofile.write(">>", output, args[index])
        elif(">" in args):
            if(flag == 0):
                i = 0
                index = 0
                for j in args:
                    if(i == 0):
                        i += 1
                        continue
                    if(args[i] == ">"):
                        index = i + 1
                        break
                    i += 1
                tofile.write(">", output, args[index])
        else:
            # If not told to send output to a file, print to screen.
            print(output)
