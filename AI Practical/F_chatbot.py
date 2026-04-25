import datetime

def fun_quiz(name):
    print("\n🎉 Quick Fun Quiz Time!")
    score = 0

    quiz = [
        ("What is the capital of France?", "paris"),
        ("How many legs does a spider have?", "8"),
        ("What planet is known as the Red Planet?", "mars")
    ]

    for i in range(len(quiz)):
        question = quiz[i][0]
        correct_answer = quiz[i][1]
        user_answer = input(f"Q{i+1}: {question} ").strip().lower()
        if user_answer == correct_answer:
            print("✔️ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The answer is {correct_answer}.")

    print(f"\n{name}, your final score: {score}/{len(quiz)}\n")

def chatbot():
    name = input("Welcome to QuickShop Support Chatbot!\nThank you for reaching out! What's your name? ")
    print(f"Hi {name}! Type 'help' to see what I can assist you with.")
    print("Type 'exit' to end the conversation.\n")

    with open("chat_history.txt", "a") as history:
        history.write(f"\n--- Chat with {name} on {datetime.datetime.now()} ---\n")

        while True:
            user_input = input(f"{name}: ").lower()
            history.write(f"{name}: {user_input}\n")

            if user_input in ["exit","quit"]:
                bot_response = "Thank you for chatting with us. Have a great day!"
                print("Bot:", bot_response)
                history.write(f"Bot: {bot_response}\n")
                break

            elif user_input == "help":
                bot_response = (
                    "I’d love to assist you! Here are some things you can ask about:\n"
                    "- Orders\n- Refunds\n- Shipping\n- Support\n"
                    "- Payment\n- Account\n- Type 'quiz' to play a fun game!"
                )

            elif user_input in ["quiz", "play", "game"]:
                fun_quiz(name)
                bot_response = "Hope you enjoyed the quiz! How else can I assist you?"

            elif any(word in user_input for word in ["angry", "bad", "terrible", "upset", "disappointed"]):
                bot_response = "I apologize for the inconvenience. Could you please share more details so I can assist you?"
                
            elif any(word in user_input for word in ["nice", "good", "ok", "great", "awesome", "better", "thanks", "thank you"]):
                bot_response = "I'm glad to hear that!  How else can I assist you?"

            elif any(word in user_input for word in ["order", "buy", "purchase"]):
                bot_response = "You can track or place orders through your account on our website."

            elif any(word in user_input for word in ["refund", "return", "money back"]):
                bot_response = "Refunds are processed within 5-7 business days after we receive the returned item."

            elif any(word in user_input for word in ["shipping", "delivery", "track"]):
                bot_response = "Standard shipping takes 3-5 business days. Express options are available at checkout."

            elif any(word in user_input for word in ["support", "contact", "help desk"]):
                bot_response = "You can reach our support team at support@quickshop.com."

            elif any(word in user_input for word in ["payment", "pay", "checkout"]):
                bot_response = "We accept credit/debit cards, PayPal, and UPI for payments."

            elif any(word in user_input for word in ["account", "signup", "login", "register"]):
                bot_response = "You can create or manage your account from the top-right corner of our website."

            else:
                bot_response = "Oops! It seems I didn’t understand that. Could you try asking it differently or type 'help'."

            print("Bot:", bot_response)
            history.write(f"Bot: {bot_response}\n")

chatbot()
