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

# This is a script containing a universal function that will decide where to send command output.
# If there is a > in the arguments, send output to a new file
# If there is a >> in the arguments, append output to a new or existing file
# If not, send output to the screen
def write(args, contents):
    # Store the amount of arguments given to a variable to be used later
    arrlen = len(args) - 1

    # Check if the > or >> exists in the arguments, if not, print command to string
    if((">" in args) or (">>" in args)):
        # Find the exact index of the filename based off the index of the symbol
        if(">>" in args):
            index = args.index(">>") + 1
        else:
            index = args.index(">") + 1
        
        # Make sure the information exists
        if(index > arrlen):
            print("bash: syntax error near unexpected token `newline'")
        else:
            # Do what the user requested - (over)write or append
            if(">>" in args):
                file = open(args[index], "a")
            else:
                file = open(args[index], "w")
            file.write("\n" + contents)
            file.close()
    else:
        # If not told to send output to a file, print to screen.
        print(contents)
