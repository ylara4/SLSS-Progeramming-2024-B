# Tip Calc
# Author: Yeshua Lara
# Feb. 28th 

if main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

    # Note: This is one way to round a number to two decimal places
    print(f"Leave ${round(tip, 2)}")


def dollars_to_float(d):
    return float("dollars")


    # Converts string dollars to a decimal float
    #    Returns the result
    # TODO


def percent_to_float(p):
    return percent.replace()
    # Converts percent to a decimal float
    #    Returns the result
    # TODO


main()

Background:
In the United States (and Canada), it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!
Requirements:
Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:
dollars_to_float, which should accept a str as input (formatted as ##.##, wherein each # is a decimal digit), and return the amount as a float. For instance, given 50.00 as input, it should return 50.0.
percent_to_float, which should accept a str as input (formatted as ##, wherein each # is a decimal digit),  and return the percentage as a float. For instance, given 15 as input, it should return 0.15.