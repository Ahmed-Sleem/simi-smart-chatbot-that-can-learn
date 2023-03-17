#to convert the dataset into usable one 
def humod_convert():
	data = open("dialogs_chatbot.txt")
	data = data.read()
	data = data.split("	")
	
	for x in data:
			file = open("dialogs_chatbot_usable.txt","a")
			file.write(x)
			file.write("\n")
	
			
		
	
	
	return "done"


print(humod_convert())