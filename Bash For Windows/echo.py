'''
This file is under the MIT License.

Copyright 2019-2021 Jeremiah Haven

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
# echo is a basic script the either echos text given or outputs a variable

# Import the system variables (to output if asked to), and tofile to process output
import systemvariables, tofile

# Main Function. Commented lines are for debugging purposes only. First set a couple of variables
def reg(args):
    string = args[0]
    stringprt = string
    ifvar = False
    i = 0
    endstring = ""
    #print(stringprt.find("$", 0, 1))
    
    # See if the first character of a string is a dollar sign, the symbol that declares the want of a
    # system variable, but ONLY if system variable varTrans is false.
    if(systemvariables.read("varTrans") == False):
        if(stringprt.find("$", 0, 1) == 0):
            ifvar = True
        else:
            ifvar = False
    else:
        ifvar = False
    
    # If there is a dollar sign, find out what variable we want and print it out. If not, print out
    # inputted text
    for j in args:
        if((args[i] == ">") or (args[i] == ">>")):
            break
        if(ifvar == True):
            newstr = stringprt[1:]
            #print(newstr)
            if(systemvariables.lookupIndex(newstr) == -1):
                if(endstring != ""):
                    endstring = endstring + " " + args[i]
                else:
                    endstring = args[i]
            else:
                if(endstring != ""):
                    endstring = endstring + " " + systemvariables.read(newstr)
                else:
                    endstring = systemvariables.read(newstr)
        else:
            if(endstring != ""):
                endstring = endstring + " " + args[i]
            else:
                endstring = args[i]
        i += 1
    flag = 0
    tofile.write(args, endstring)