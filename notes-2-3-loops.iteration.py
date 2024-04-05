# Loops and Iteration
# Yeshua Lara
# April 5 

# print something, repeat 10x
for _ in range(10): 
    print("LOL")

# print out every item in my grocery list
    grocery_list = [
    "dishwasher tabs"
    "aluminium foil"
    "blueberry muffins"
    "RTX 4070 Super"
    ] 

    # stop if we reach blueberry muffins

    for item in grocery_list:
        print("----")
        print(item)
        print(f"*{item}")

        if item == "blueberry muffins":
            break

        # count to 0 to 9
        for i in range(10):
            if i % 2 == 0:
                print(f"{i} is an even number")


# rewrite the above for loop as a while loop
    counter = 0 

    while counter < 1000: 
        print(counter)

        if counter % 2 == 0:
            print(f"{counter} is an even number.")

        counter += 1 

        