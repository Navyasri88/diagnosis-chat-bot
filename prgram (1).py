import random 
import datetime as d
def wish():
	greetings = ['hey hai i am jeff ....!,i am here to help u out . by the way may i know ur name',
	'hello i am jeff ..! how can i help you and tell me yor name !']
	return random.choice(greetings)
	
def welcome(name):
	time = d.datetime.now().hour 
	if time<12:
	 	return"goodmoring " +name+ " !! enjoy your day !"
	elif time >= 12 and time <16:
	 	return "wishing you a good afternoon " +name+"!!"
	elif time >=16 and time <22:
	 	return "a very peaceful evening "+name+'!!'
	else :
	 	return 'ohh!! its too late, '+name+' anyways i ll help you'
def choices():
    #group1 =[Mpc]
    courses = ['Diploma Engineering',"Merchant Navy courses","B. Arch","B.Sc. courses. .."," B Pharmacy."]
    #group2 =  [BIpc]
    courses2 = ["MBBS (Medicine)","BDS (Dental)","Agriculture Allied Courses ","Pharmacy Courses"]
    print("1. MPC\n2. BIPC")
    print("enter the number 1 or 2 to get details :")
    print("Enter 0 to end the chat !!  :\n")
    try:
    	x = int (input ())
    	print()
    	if x==1:
    		print (courses)
    		print("Thank You!!!")
    	elif x==2:
    		print(courses2)
    		print("Thank You!!!")	
    	elif x==0:
    		quit()
    except Exception as e:
    	print("Enter Valid Input")
    	choices()
def bot_jeff():
	print(wish())
	print()
	grp = input()
	print()
	print(welcome(grp))
	print()
	choices()
def quit():
	print("Thank You!!!")
print()	
print(" ######    Welcome to chat bot ######")
print()
bot_jeff()