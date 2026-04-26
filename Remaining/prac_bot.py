import datetime

def quiz(name):

	print (f"Welcome to quick quiz {name}.")
	
	quiz=[
			("capital of france?","paris")
			("No of legs of spider?","8")	
	]
	score=0
	
	for i in range(quiz):
		question= quiz[i][0]
		answer= quiz[i][1]
		user_ans= input(f"Q{i+1}"," {question}").strip().lower()
		
		if user_ans==answer:
			print("\nCorrect")
			score+=1
		else:
			print("\nWrong")
			print(f"\nCorrect answer is : {aswer}")
	print(f"Your score= {score}/len(quiz)")


def chatbot():
	name=input("\nWelcome whats Name? ")
	print(f"\nhi {name} type 'help' for assistance")
	
	with open("chat.txt", "a") as history:
	    history.write(f"\nChat with {name} on {datetime.datetime.now()}")
	
	    while True:
	    	user_response=input(f"{name}: ").lower()
	    	history.write(f"\n{name}: {user_response}")
	    	
	    	if user_response == "quit":
	    		bot_response=("Thank you for chatting.")
	    		print(f"bot: {bot_response}")
	    		history.write(f"\n{name}: {bot_response}")
	    		break
	    	elif user_response == "quiz":
	    		quiz(name)
	    		bot_response=("\nHope you enjoy")
	    		print(f"bot: {bot_response}")
	    	elif user_response == "help":
	    		bot_response=("\n Orders\nShipping\npayment")
	    		print(f"bot: {bot_response}")
	    	elif any(word in user_response for word in ["thanyou","nice","good"]):
	    		bot_response=("\n Glad to hear!")
	    		print(f"bot: {bot_response}")
	    	elif any(word in user_response for word in ["order","purchase","buy"]):
	    		bot_response=("\nplace order through account!")
	    		print(f"bot: {bot_response}")
	    	elif any(word in user_response for word in ["shipping","ship","track"]):
	    		bot_response=("\n Shipping takes 5-6 days")
	    		print(f"bot: {bot_response}")
	    	else:
	    		bot_response=("\n Sorry i do not understand")
	    		print(f"bot: {bot_response}")
	    	history.write(f"bot: {bot_response}")

chatbot()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
