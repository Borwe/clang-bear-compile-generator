#/usr/bin/env python3

import sys
import platform
import subprocess
import threading

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
		self.command.insert(0,"bear")
		
		output=subprocess.Popen(self.command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		self.printOutput(output)
		
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
