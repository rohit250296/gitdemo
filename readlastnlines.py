#function for reading last n lines 
def readlastnlines(filename,lines): # two parameters namelt filename and number of lines 
	# with statement in Python is used in exception handling to make the code cleaner and much more readable
	with open(filename,encoding="utf-8") as f:# file gets opened here note : encoding is important if u are using python 3 
		#here i is a counter variable which traverses over the total number of lines 
		# '-lines' indicates that the lines will be travesed from the end 
		for i in (f.readlines()[-lines:]): 
			print(i)

readlastnlines('sample2.txt',10);# finally the function is called
