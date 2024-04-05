# More Functions
# Yeshua Lara
# April 3 

# implement stars function

def stars(num):
    """returns specified numbers of stars"""
    value = ""  # placeholder for return value
    # if num is 0, return 1 star
    # if num is 1, return 1 star

    # elif number is greater than 1, return that num * star
    

    # else return error saying negative nums arent allowed
    if num == 0 or num == 1:
        value = "*"
    elif num > 1:
        value = "*" * num
    else:
        value = "sorry, cant take negative numbers"

    return value


# Multiply strings 
greeting = "hello"
print(greeting * 100)

print("the quick brown fox jumps over the lazy dog" * 2)

print(stars(10)) #"**********"
print(stars(1000)) #"**********"
print(stars(0))


print(stars(0))
print(stars(1))
print(stars(1000))
print(stars(-1))

def biggest_of_three(num):
    if num == 10 or num = 100:
        value = "Smallest"
    
    elif num > 1000:
        value = "Biggest"

    else: 
        value = "Nope"

    return value

    

