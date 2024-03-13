# Methods - String Methods
# Author: Ubial
# 21 Feb.

# Ask the user what the weather is 
user_reply = input("What is the weather like?")


# If they say rainy, say 
# bring an umbrella
if user_reply.strip(" !.?,").lower() == "rainy":
    print("Bring an umbrella!")
else:
    print("Sorry I didn't understand the question.")
