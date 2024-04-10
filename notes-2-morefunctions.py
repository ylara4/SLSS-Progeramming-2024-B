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




print(stars(10)) #"**********"
print(stars(1000)) #"**********"
print(stars(0))







    

