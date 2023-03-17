#conv music to usable one 
#for random picking 
import random


file = open("Streams.csv")
file = file.readlines()


question_artist = ["do you know ","tell me a song by ","what do you know about ","what is your favorite song by ","the song by","the music by ","music by ","music made by ","song made by "]

question_song = ["do you know ","do you hear ","what do you know about ","the music song ","the song ","the music ","the hit "," music clip ","music track ","sound track ","track ","song ", "music ","sound like "]

answer_artist = ["yeh yeh , ","yes i really like ","of course do you listen to ","my favorite one is ","i really enjoyed "]

answer_song = ["i know ","i love the work of ","usually listen to ","big fan of ","my favorite artist is ","the good work is always by "]


for x in file :
	x = x.split(",")
	name = x[0]
	artist = x[1]
	
	#for artist
	for q in question_artist:
		file_usable = open("usable_stream.txt","a")
		
		
		
		file_usable.write(q)
		file_usable.write(artist)
		file_usable.write("?")
		
		
		file_usable.write("\n")
		
		answer_artist_random = random.choice(answer_artist)
		file_usable.write(answer_artist_random)
		file_usable.write(name)
		
		file_usable.write("\n")
		
		
	for qq in question_song :
		
		file_usable = open("usable_stream.txt","a")
		
		
		
		file_usable.write(qq)
		file_usable.write(name)
		file_usable.write("?")
		
		
		file_usable.write("\n")
		
		answer_song_random = random.choice(answer_song)
		file_usable.write(answer_song_random)
		file_usable.write(artist)
		
		file_usable.write("\n")
		
		

