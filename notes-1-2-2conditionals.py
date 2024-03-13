# Conditionals 
# Author: Yeshua Lara
# 14 February 2024

# Implement the flowchart from the notes

# Create two variables, x and y
x = 1_000_000
y = -5.2 


# If x is less than y, print that

if x < y:
    print("x is less than y")


# If x is greater than y, print that
    
if x > y:
    print("x is greater than y")




# If x is equal, print that
    
if x == y:
    print("x is equal to y")


if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x==y:
    print("x is equal to y")
else: 
    print("x is equal to y")
    

# Ask the user what their favorite fruit is
fave_fruit = input("Whats your favourite fruit?") 

# Ask the user how old they are
user_age = input("how old are you")

# If they answer banana and theyre 2 years old
if fave_fruit == "banana" and user_age == "2":
    print("Banana's are delicous.")




# If they answer apple or orange 
if fave_fruit == "orange" or fave_fruit == "apple":
    print("Delicious choice!")




    