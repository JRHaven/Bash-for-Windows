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
def write(args, contents):
    arrlen = len(args) - 1
    if(args[0] == ">"):
        if(1 > arrlen):
            print("bash: syntax error near unexpected token `newline'")
        else:
            # If told to overwrite, overwrite a file and put given text in file.
            fileWrite = open(args[1], "w")
            fileWrite.write(contents)
            fileWrite.close()
    elif(args[0] == ">>"):
        if(1 > arrlen):
            print("bash: syntax error near unexpected token `newline'")
        else:
            # If told to append, append given text to file.
            file = open(args[1], "a")
            file.write("\n" + contents)
            file.close()
    else:
        flag = 0
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
            
            # Make sure the information exists
            if(index > arrlen):
                print("bash: syntax error near unexpected token `newline'")
            else:
                # If told to append, append given text to file.
                file = open(args[index], "a")
                file.write("\n" + contents)
                file.close()
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
                # Make sure the information exists
                if(index > arrlen):
                    print("bash: syntax error near unexpected token `newline'")
                else:
                    # If told to overwrite, overwrite a file and put given text in file.
                    fileWrite = open(args[index], "w")
                    fileWrite.write(contents)
                    fileWrite.close()
        else:
            # If not told to send output to a file, print to screen.
            print(contents)
