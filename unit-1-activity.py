# Unit Activity 
# Author: Yeshua Lara
# March 4th 


# Introduce yourself to the user
print("Hello, my name is Alex.")

# Ask the user's name
user_reply = input("What's your name?")

# If their name is Arthur, say
# I have a cousin named Arthur too!
if user_reply.strip("!.?,").lower() == "arthur":
    print("I have a cousin named Arthur too!")

# If their name is Carmen, say
# Wow! I've never met someone named Carmen before. 
elif user_reply.strip("!.?,").lower() == "carmen":
    print("Wow! I've never met somoene named Carmen before.")

# If their name is Alex, say
# No way!! We have the same name!!🤯
elif user_reply.strip("!.?,").lower() == "alex":
    print("No way!! We have the same name!!🤯")
else:
    print("It's nice meeting you!")

# Ask the user what their favourite food is
user_reply = input("What's your favorite food?")

# If pizza, say
# I hate pizza. 
if user_reply.strip("!.?,").lower() == "pizza":
    print("I hate pizza...")

# If sushi, say
# I love sushi!!
elif user_reply.strip("!.?,").lower() == "sushi":
    print("I love sushi!!")

# If noodles, say
# Wow, you have really bad taste... except for the sushi.
elif user_reply.strip("!.?,").lower() == "noodles":
    print("Wow, you have really bad taste... except for the sushi.")
else:
    print("Acceptable.") 

def say_hello_params(name):
    print(f"Hello {name.capatalize()}!")
def how_big(num):
    if num < 10: 
        return "Small"
    if num < 50:
        return "Medium"
    if num < 500:
        return "Large"
    if num < 1000:
        return "Extra Large"
def adder(x: int, y: int) -> int:
    return x + y 
result = adder (1,1)
print(result)
result = how_big(1000)
print(result)

            
            
            
            
            
            
            



