import json
import os
file_path = os.path.join(os.path.dirname(__file__), "knowledge_base.json")
knowledge = {}
def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            else:
                return {}
    except (FileNotFoundError, json.JSONDecodeError):
        # Create a new file with empty dict
        with open(file_path, "w") as file:
            json.dump({}, file, indent=4)
        return {}
    
def save_knowledge(file_path, knowledge):
    try:
        with open(file_path, "w") as file:
            print("CHAT BOT: UPDATING THE KNOWLEDGE....")
            json.dump(knowledge, file, indent=4)
    except FileExistsError:
        print("UPDATING THE KNOWLEGDE FAILED.....")
        
def chat_bot(file_path, knowledge):
    print ("WELCOME TO THE SIMPLE CHAT_BOT ^_____^")
    print("CHAT BOT :please ask me any thing : )")
    while True:
        user_message = input("YOU : ").lower()
        response = load_json(file_path)
        if isinstance(response, dict):
            if user_message in response:
                responses = response[user_message]
                print(f"CHAT BOT: {responses}")
            else:
                print("CHAT BOT: I don't know the answer to that question.")
                print("So, could you tell me what will be the proper response of this question")
                user_response = input("YOU : ").lower()
                response[user_message] = user_response
                save_knowledge(file_path, response)
        else:
            print("CHAT BOT: Error - knowledge base is not in the expected format.")
        if user_message == "bye":
            print("CHAT_BOT: BYE....")
            print("X_X")
            break   

chat_bot(file_path, knowledge)




    

        
