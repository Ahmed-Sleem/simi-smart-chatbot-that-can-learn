#taking input 
def taking_input(user_input):
	
	#ignored characters 
	ignore = ['"',"'",'(',')','>','<','?','/','\\','}','{','[',']','-','_','&','^','%','$','#','@','!','~','`']
	
	#make lower case 
	inp = user_input.lower()
	
	#clean input 
	for char in ignore :
		inp = str(inp).replace(char, "")
			
	#split input 
	inp = inp.split(" ")
	
	#log input 
	with open("log.txt","a") as log :
		log.write("input: ")
		newinput = str(inp)
		newinput = newinput.replace("'", "")
		newinput = newinput.replace("[", "")
		newinput = newinput.replace("]", "")
		log.write(newinput)
		log.write("\n")
	
			
	return inp 

