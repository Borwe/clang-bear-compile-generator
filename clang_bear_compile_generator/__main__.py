import runner
import sys

if __name__ == "__main__":
	if(len(sys.argv)<2):
		print("Sorry no make build command found")
		exit(-1)
	launch=runner.LaunchIT(sys.argv[1:])
	launch.execute()
