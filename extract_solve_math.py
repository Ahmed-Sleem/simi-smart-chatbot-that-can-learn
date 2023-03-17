#extract math problems from user input 
def extract_math (user_input):
	
	#split input 
	try:
		user_input  = user_input.split(" ")
	except :
		pass
		
	#problem 
	math = []
	
	#extract math
	for word in user_input :
		
		#char list
		word = list(word)
		
		#extract float
		for x in word:
			try:
				
				#for numbers
				y = float(x)
				math.append(y)
				
				
			except ValueError:
				
				#extract operations
				operations = ["-","+","*","/"]
				
				for op in operations:
					if x == op :
						math.append(x)
					else:
						pass
	
	return math

#solve problems
def solve(math_problem):
	
	#clean problem
	math_problem = str(math_problem).replace("'", "")
	math_problem = math_problem.replace("[", "")
	math_problem = math_problem.replace("]", "")
	math_problem = math_problem.replace(",", "")
	
	
	
	
	#check its a problem 
	op_for_check = ["-","+","*","/"]
	if_op = []
	for op in op_for_check:
		if op in math_problem:
			if_op.append(op)
		else:
			pass
			
	if len(if_op) < 1 :
		math_problem = ""
	else:
		pass
		
	
	
	
	
	#solve problem
	try :
		result = eval(math_problem)
	except:
		result=""
	
	
	return result


def outputing(user_input):
	output = solve(extract_math(user_input))
	
	return output


	