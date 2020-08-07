#/usr/bin/env python3

import sys
import os
import platform
import subprocess
import shutil

class LaunchIT():
    #setup the command to be used with bear
    def __init__(self,command:iter):
            self.command=command
            
    #for validating if the bear cmd exists
    # and if the command is actually doable
    def validate(self):
            #to know if we use which or where depeneding on OS
            cmd= ""
            if platform.system()=="Windows":
                    cmd="where"
            else:
                    cmd="which"	
                    
            try:
                    subprocess.call([cmd, "bear"])
                    print("Found bear in your system")
                    return True
            except EnvironmentError as err:
                    print("Sorry, please install or make sure bear is in your system path before continuing")
                    return False
            
            try:
                    subprocess.call([cmd, self.command[0]])
                    print("Found "+self.command[0]+" in your system")
                    return True
            except EnvironmentError as err:
                    print("Sorry, please install or makre sure "+self.command[0]+" is in your system path before continuing")
                    return False
	
    def execute(self):
        if(self.validate()==False):
                #stop here and prompt user to fix problem
                print("Please fix the problems")
                return False

        #if we reach here means we are actually okay to keep on moving
        self.command.insert(0,"-a")
        self.command.insert(0,"bear")

        output=subprocess.Popen(self.command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        self.printOutput(output)

        # check if compile_commands.json exists, if so, then prompt
        # user to copy file into ../ or ask them to provide a path to use
        compile_file=os.getcwd()+os.sep+'compile_commands.json'
        if(os.path.exists(compile_file)):
            #if it exists, then prompt user where they want to save it
            result=self.promptCopyLocation(compile_file)
            if(result==0):
                return True
            else:
                return False
        else:
            #we reach here if the file was never created
            print("File compile_commands.json wasn't created")
            print("Please retry again")
            return False

    #used to prompt user where they want to copy the file to
    #return 0 if success, -1 if an error occured
    def promptCopyLocation(self,compile_file):
        print("Please select where to place the compile_commands.json file")
        print("1. .."+os.sep+" (AKA: Parent directory)")
        print("2. Your own location")
        print("3. Exit")
        decisition=input("Enter here: ")
        try:
            decisition=int(decisition)
            if(decisition >3 or decisition <=0):
                #meaning user chose bad option 
                print("Please choose a valid option")
                return self.promptCopyLocation(compile_file)

            #if chooses 1, meaning copy to parent directory
            if(decisition==1):
                shutil.copyfile(compile_file,os.getcwd()+os.sep+".."+os.sep+"compile_commands.json")
                return 0

            #if chooses 2, meaning copy to a specific directory
            if(decisition==2):
                dirToCopy=input('Please give directory to copy file to: ')
                if(os.path.exists(dirToCopy)==False):
                    print("Sorry the directory passed does not exist")
                    return self.promptCopyLocation(compile_file)

                # otherwise go ahead and copy the file
                shutil.copyfile(compile_file,dirToCopy+os.sep+"compile_commands.json")
                return 0
        except ValueError:
            return -1

		
    def printOutput(self,output:subprocess.Popen):
            stdout,stderr=output.communicate()
            if(stdout != None):
                    sys.stdout.buffer.write(stdout)
            
            if(stderr !=None):
                    sys.stderr.buffer.write(stderr)


if __name__ == "__main__":
	#check that all args are more than one atleast passed
	if(len(sys.argv)<2):
		print("Sorry no make build command found")
		exit(-1)
	launch=LaunchIT(sys.argv[1:])
	launch.execute()
