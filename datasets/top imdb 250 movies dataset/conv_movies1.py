#for random picking
import random
#for csv
#from pandas import *

def movies():
	movies = open("IMDB Top 250 Movies.csv")
	movies = movies.readlines()
	
	for x in movies:
		x = x.split(",")
		rank = x[0]#done
		name = x[1]#done 
		year = x[2]#done
		rating = x[3]#done
		genre = x[4]#done 
		#cast = x[10]#done
		#director = x[11]#done
		#writer = x[12]#done
		
		file = open("usabletopmoviesfinal.txt","a")
		
		#rank
		file.write("what is the rank of ")
		file.write(name)
		file.write(" movie ?")
		file.write("\n")
		
		file.write(name)
		file.write(" ranked as #")
		file.write(rank)
		file.write(" in IMDB list with rating about ")
		file.write(rating)
		file.write("\n")
		
		#name
		file.write("what is the name of the movie with # ")
		file.write(rank)
		file.write(" ?")
		file.write("\n")
		
		file.write(name)
		file.write(" ranked as #")
		file.write(rank)
		file.write(" in IMDB list with rating about ")
		file.write(rating)
		file.write("\n")
		
		#year 
		file.write("when did ")
		file.write(name)
		file.write(" movie released ?")
		file.write("\n")
		
		file.write(name)
		file.write(" released in ")
		file.write(year)
		file.write(" with rating about ")
		file.write(rating)
		file.write("\n")
		
		#rating
		file.write("what is the rating of  ")
		file.write(name)
		file.write(" movie ?")
		file.write("\n")
		
		file.write(name)
		file.write(" ranked as #")
		file.write(rank)
		file.write(" in IMDB list with rating about ")
		file.write(rating)
		file.write("\n")
		
		#genre
		file.write("what is the genre of ")
		file.write(name)
		file.write(" movie ?")
		file.write("\n")
		
		file.write(name)
		file.write(" classified as ")
		file.write(genre)
		file.write(" in IMDB list with rating about ")
		file.write(rating)
		file.write("\n")
		
		#cast
		#file.write("tell me about the cast of ")
		#file.write(name)
		#file.write(" movie")
		#file.write("\n")
		
		#file.write(name)
		#file.write(" ranked as #")
		#file.write(rank)
		#file.write(" in IMDB list with rating about ")
		#file.write(rating)
		#file.write(" and the cast was : ")
		#file.write(cast)
		#file.write(" with ")
		#file.write(director)
		#file.write(" as a director and ")
		#file.write(writer)
		#file.write(" as a writer")
		#file.write("\n")
		
		#direcore
		#file.write("tell me about the director of ")
		#file.write(name)
		#file.write(" movie")
		#file.write("\n")
		
		#file.write(name)
		#file.write(" ranked as #")
		#file.write(rank)
		#file.write(" in IMDB list with rating about ")
		#file.write(rating)
		#file.write(" the director was ")
		#file.write(director)
		#file.write(" with ")
		#file.write(writer)
		#file.write(" as a writer and the rest of the cast : ")
		#file.write(cast)
		#file.write("\n")
		
		#writer
		#file.write("tell me about the writer of ")
		#file.write(name)
		#file.write(" movie")
		#file.write("\n")
		
		#file.write(name)
		#file.write(" ranked as #")
		#file.write(rank)
		#file.write(" in IMDB list with rating about ")
		#file.write(rating)
		#file.write(" the writer was ")
		#file.write(writer)
		#file.write(" with ")
		#file.write(director)
		#file.write(" as a director and the rest of the cast : ")
		#file.write(cast)
		#file.write("\n")
		
		
		
		#movie card
		question = ["tell me about the movie ","what do you think about the movie ","what do you know about the film ","the movie ","the film ","suggest a movie like ","do you suggest ","suggest something to watch like ","movie ","film "]
		
		for q in question:
			
			file.write(q)
			file.write(name)
			file.write("\n")
			
			file.write(name)
			file.write(" ranked as #")
			file.write(rank)
			file.write(" in IMDB list and got about ")
			file.write(rating)
			file.write(" as a rating ")
			file.write("in ")
			file.write(year)
			#file.write("the director was ")
			#file.write(director)
			#file.write(" with ")
			#file.write(writer)
			#file.write(" as a writer ")
			#file.write(",")
			#file.write("the cast : ")
			#file.write(cast)
			file.write("\n")
		
		
		
		
		
		
		
		
		
		
	
	return "done"

print(movies())
