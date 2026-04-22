import random
import json
import os
def save_data(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data(filename, default=None):
    if default is None:
        default = {}
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

DATA_FILE = "bot_data.json"
data = load_data(DATA_FILE, {"name": None, "count": 0})

user_name = data.get("name")
count = data.get("count", 0)
print("This is a random ai answers:) write Help to understand what's going on here, or write exit")
user_name = input("Your name is:")
print(f"Hello {user_name}")
count = 0
while True:
    question = input("You:").lower()
    count += 1
    if count == 25:
        print("What do you doing here??!?!?!?!:")
    if count == 45:
        print("YOU CRAZY??!?!?!?!:")
    if count == 50:
        print("What do you doing here??!?!?!?!:")
        break
    elif "help" in question:
        print("Nothing:)")
    elif "exit" in question:
        print("Bye")
        break
    else:
        Answers = ["Hi", "Hello", "How are you?", "I'm fine", "Good", "Bad", "What's your name?", "My name is AI", "I'm AI", "earth is planet", f"{user_name}", "siuuuuu", "mykha", f"{count} messages", f"{count} messages???!?!!?!? What do you doing?!?!? why??!", "Why??!?!?!?!", f"{user_name}! What do you doing here?!", f"{user_name}! {count} messages!!! You a crazy?!?!"]
        print("Ai:", random.choice(Answers))

