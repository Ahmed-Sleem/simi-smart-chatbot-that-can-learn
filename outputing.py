#import alogrithem to grab replys
import algorithem as algo

#for random choise 
import random

#to learn new lines 
import learn as learn

#grabing output 
def chating (input):
	
	inp = str(input)
	
	#output
	output = algo.search_database(inp)
	
	return output 


#first greating 
first_message = ["hi","hello","hey","sup!","whats up","how are you?","heeeeey!"]
greating = random.choice(first_message)


#the chat 

print(greating)


while True :
	output = chating(input("")) 
	print(output)
	#log output 
	with open("log.txt","a") as log :
		log.write("output: ")
		log.write(str(output))
		log.write("\n")
	#to learn new lines 
	learn.learn()
		
		
	
	
	