# Lists and Modules
# Yeshua Lara
# March 8

import random
import time


# 1. Greet the user
print("Hello!")
time.sleep(1.5)

# 2. Ask them,"how are you?"
print("How are you?")
user_feeling = input().strip(",.?!").lower()
time.sleep(1.5)
# 3. Respond with a general statement
# thats is randomly chosen
#       - list of possible responses
#       - choose a response
#       - print

good_possible_resp = {"Im really happy for you!", "Thats really good news!!", "Wowwwww!!!"}

if user_feeling == "good" or user_feeling == "great":
    chosen_response = random.choice(good_possible_resp)
    
    print(chosen_response)
time.sleep(1.5)
bad_possible_resp = {"I dont care.", "Sorry.", "Wow thats really bad."}
elif user_feeling == "bad" or user_feeling == "not too good":
chosen_response = random.choice(bad_possible_resp)

print(chosen_response)
time.sleep(1.5)

else:
print("Go to therapy, you really need it...")
time.sleep(1.5)
# 4. say goodbye
print("Byeeee!")

