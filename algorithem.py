#import input taking file 
import taking_input as input 

#import math engine 
import extract_solve_math as math

#to choise random reply
import random



#do not understand
do_not_understand = ["i do not fully understand what you say"," can you please explain","sorry i don't understand","explain more","i am trying to understand","more details","more details please","mmm... trying to understand","hhhm.... tell me more please , i am trying to understand"]




#grab the suitable replay
def search_database (user_input):
	
	#grab cleaned input
	inp = input.taking_input(user_input)
	
	#open database 
	with open("database.txt","r") as database:
		data = database.readlines()

	#organize in list of lists
	list = []
	for line in data :
		newline = str(line).replace("\n", "")
		newline = newline.split(" ")
		list.append(newline)
		
	
	
	#choise min match percentage 
	min_match_ratio = 40.0
	
	accepted_replys = []
	ratios = []
	
	#get match percentage and accepted replyes
	for l,index in zip(list[0::1],range(0,len(list)))  :
		match_percent = (len(set(l).intersection(set(inp))))/len(l)*100
		if match_percent > min_match_ratio :
			try:
				accepted_replys.append(list[index + 1])
				accepted_replys.append(list[index - 1])
				ratios.append(match_percent)
			except IndexError :
				false = 0
	
	#do not understand
	do_not_understand = ["i do not fully understand what you say"," can you please explain","sorry i don't understand","explain more","i am trying to understand","more details","more details please","mmm... trying to understand","hhhm.... tell me more please , i am trying to understand"]
	
	
	#if there isnt enought data in database 
	if len(accepted_replys) < 2 :
		fail_reply = random.choice(do_not_understand)
		accepted_replys.append(fail_reply)
	
		
	
	
	
	
	#best reply 
	try :
		best_reply = max(ratios)
		best_reply = ratios.index(best_reply)
		best_reply = accepted_replys[best_reply]
	except : 
		false = 0
		
	
		#top replys
	top_replys = accepted_replys
	
	
	
				
				
			
	try :
		reply = random.choice(top_replys)
	except :
		false = 0
		
		
	#cleaning reply
	clened_reply = str(reply)
	clened_reply = clened_reply.replace('"', "")
	clened_reply = clened_reply.replace("'", "")
	clened_reply = clened_reply.replace(",", "")
	clened_reply = clened_reply.replace("[", "")
	clened_reply = clened_reply.replace("]", "")
	
	
	#math engine
	if_math_result = math.outputing(input.taking_input(user_input))
	if if_math_result :
		
		#clean from dont know
		for x in do_not_understand:
			
			#clean x
			x = str(x)
			x=x.replace("'", "")
			x=x.replace('"', "")
			x=x.replace(',', "")
			
			
			clened_reply = clened_reply.replace(x, "")
		
		#form weird input statment
		if clened_reply:
			pass
		else:
			weird_input_statment = ["you high ?, ","the math problem is the only thing i see in your message , ","really ... math !","just math !  ","why this ! , ","only numbers ! , ","extracting math ! , ","i see the math problem , ",]
			weird_input_statment_choise = random.choice(weird_input_statment)
			clened_reply = weird_input_statment_choise
			
			
		#form math reply
		math_statments = [" i think the result = "," the result must be "," i think it's "," my answer is "," it can be "]
		math_full_result = [random.choice(math_statments) , if_math_result]
		math_full_result = str(math_full_result)
		math_full_result = math_full_result.replace("[", "")
		math_full_result = math_full_result.replace("]", "")
		math_full_result = math_full_result.replace(",", "")
		math_full_result = math_full_result.replace("'", "")
		math_full_result = math_full_result.replace('"', "")
	else:
		math_full_result = ""
	
	return clened_reply + math_full_result

	

