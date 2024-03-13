# McDoBot Examples
# Author: Yeshua
# Feb 21. 

# Ask the user if they want fries 
user_reply = input("Would you like fries with your meal?")

# If they say Yes, say
# here's your meal with fries

if user_reply.strip(" !,.?").lower() == "yes":
    print("Here's your meal with fries!")

# If they say No, say
# here's your meal without fries
    
if user_reply.strip(" !,.?").lower() == "no":
    print("Here's your meal without fries!")

# If they something else, say
# I don't understand the question...
    
else:
    print("I don't understand the question...")

