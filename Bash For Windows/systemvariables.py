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
# systemvariables holds all variables open to all parts of the system who import them. The variables can be set, modified,
# and read depending on what a script may need to do with them. The end user may only see what are in the variables through
# means of the lsvars and echo commands.

# Put any arrays seperately, we cannot handle arrays in the dynamic format of variables.
directorystack = ["","","","","","","",""]

varsNames = []
varConts = []

def init(name, conts):
    #print("New Init! Name:", name, "Value:", conts)
    varsNames.append(name)
    varConts.append(conts)

def lookupIndex(name):
    j = 0
    for i in varsNames:
        if(i == name):
            return j
        j += 1
    return -1

def read(name):
    i = lookupIndex(name)
    if(i == -1):
        return -1
    else:
        return varConts[i]

def modify(name, conts):
    i = lookupIndex(name)
    if(i == -1):
        return -1
    else:
        varConts[i] = conts
        return 0

def modifyVoid(name, conts):
    if(modify(name, conts) == -1):
        init(name, conts)