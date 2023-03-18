#for random picking
import random

#to convert the dataset into usable one 
def humod_convert():
	data = open("jokestext..txt")
	data = data.readlines()
	
	for x in data:
		file = open("jokes_usable.txt","a")
		statment = ["tell a joke","tell me a joke","can you tell me a joke?","do you have any jokes?","tell me another joke","please tell me another joke","tell me something to laugh","make me smile","make me laugh if you can","can you make me laugh ?","do you have any jokes",]
		
		file.write(random.choice(statment))
		file.write("\n")
		file.write(x)
		
	
	
		
		
	
	
	return "done"


print(humod_convert())