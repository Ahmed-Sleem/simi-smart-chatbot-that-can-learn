#to convert the dataset into usable one 
def humod_convert():
	data = open("HUMOD_Dataset.txt")
	data = data.readlines()
	
	for x in data:
		x = x.split("	")
		speaker_1 = x[1]
		speaker_1 = str(speaker_1).replace("Speaker 1:", "")
		
		
		speaker_2 = x[2]
		speaker_2 = str(speaker_2).replace("Speaker 2: ", "")
		
		
		user_reply = x[8]
		user_reply = str(user_reply).replace("user_reply", "")
		
		file = open("humod_usable.txt","a")
		file.write(speaker_1)
		file.write("\n")
		file.write(speaker_2)
		file.write("\n")
		file.write("user_reply")
		
		
	
	
	return "done"


print(humod_convert())