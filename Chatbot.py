# This is i simple cheatbot which is based on predefine responces 

def chatbot():
    print("Chatbot: Hello! I am a Chatbot ,what you want to ask? ,If you want  to exit you simply type  'bye'.")

    while True:
        user_input = input("You: ").lower() 

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How about you?")
        elif user_input == "i am fine":
            print("Chatbot: That's great to hear!")
        elif user_input == "what is your name":
            print("Chatbot: I'm your friendly chatbot.")
        elif user_input == "what can you do":
            print("Chatbot: I can chat with you and make you smile.")
        elif user_input == "who created you":
            print("Chatbot: I was created by Kartik kasana , Who is a B.Tech(AI) student.")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: Sorry, I don't understand that yet.")

# Now Run the chatbot Function

chatbot()