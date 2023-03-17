#for cleaning 
import algorithem as algo 

def learn ():
	log = open("log.txt","r")
	log_lines = log.readlines()
	
			
	savedline = open("savedline.txt","r")
	y = savedline.readlines()
	yy = y[0]
	yyy = int(yy)
	
	
	for x in log_lines[yyy::1] :
		
				
		
		cleanedlog = str(x)
		cleanedlog = cleanedlog.replace("'", "")
		cleanedlog = cleanedlog.replace("[", "")
		cleanedlog = cleanedlog.replace("]", "")
		cleanedlog = cleanedlog.replace("output:", "")
		cleanedlog = cleanedlog.replace("input:", "")
		
		
		for x in algo.do_not_understand:
			cleanedlog = cleanedlog.replace(x, "")
			
			
		
		database = open("database.txt" , "a")
		database.write(str(cleanedlog))
		savedline = open("savedline.txt","w")
		yyyy = str(yyy+1)
		savedline.writelines(yyyy)
		
	return 0



