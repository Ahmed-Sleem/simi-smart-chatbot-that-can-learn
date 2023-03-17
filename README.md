# simi-smart-chatbot-that-can-learn
a simple chatbot programed with python that can solve simple math problems, talk about anything and even learn new things

the txt files : 
  - database.txt : it is the main file that work as a database for the bot all the outputs are grabbed from here and all the new outputs will be written automatically in here 
  - log.txt : in this file the bot will log all the inputs and outputs, it will contain the new lines that the bot will learn aka put in the database file but not all the log will consedered as new lines in the database, there is a filter for that 
  - savedline.txt : in this file the but will log the number of the line that finshed learning at to continue the next time from where it finished not from the start point 

the py files :
  - learn.py : in this file is the code that coresponding for filtering the lines from the log then write it back into the database file so the bot will have new lines every time you use it 
  - taking_input.py : the rule of this file is to take input and filter it,split it and make it ready to the next stage which is searching the database for at least one match 
  - outputing.py : this is the file that will be used by the user to interact with the bot , in this file the chat between the user and the bot will happend
  - extract_solve_math.py : in this file the bot will extract the integers and the mathematical openrations (+,-,*,\) from the input (str) then will evaluate it and return with the result in usable form of sentence 
  - algorithem.py : in this file the bot takes the cleaned input and search in the database and return with the output then put it in usable form 
  
**** notes :
  - the database.txt file in the package contains some random jokes,data about movies,music and some explitic weird responses grabed from random datasets
  - all the datasets that used is in dataset folder with py file that cleaned the data and convert it to the simple form used in database file
    
**** quick start :
  simply go to the outputing.py file and run it 
  
  
**** the simple idea behind how this bot work :


