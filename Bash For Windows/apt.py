'''
This file is under the MIT License.

Copyright 2019 Jeremiah Haven

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
# Apt tries to get a file from the internet but does not work yet

# Libraries
import os
import systemvariables
import urllib

# Main function
def install(go):
    print("\nMoving to Downloads Directory...")
    os.chdir(systemvariables.HOME + "\\" + systemvariables.usrsession + "\\Downloads")
    # Commented out lines are for debugging purposes only
    #print(os.getcwd())
    print("Getting Executable from selected source...")
    file = input("What do you want to name this new file? ")
    
    # Attempt to retrieve the file
    urllib.request.urlretrieve(go, file)
    
    # Ask the user if they want to execute the downloaded file
    confirm = input("Do you want to execute this file[Y,n]? ")
    if((confirm == "Y") or (confirm == "y")):
        os.system(file)
    else:
        print("The file was downloaded into the Downloads folder.")
