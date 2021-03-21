#!/bin/bash/env python3
def addint(number1,number2):
    result = number1 + number2
    return result

def main():
	import sys
	print (sys.argv)
	i=(len(sys.argv)-1)
	print ("the number of arguments : ",i)

	if (i==2):
		x = int (sys.argv[1])
		y = int (sys.argv[2])
		print(addint(number1,number2))
	else:
		print("error : please insert only 2 arguments")
	
main()
