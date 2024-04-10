# Unit Activity 2
# Yeshua Lara
# April 8 

# print the names of the students in class
student_list = [
    "Alex"
    "Felix"
    "Madison"
    "Amanda"
    "Clara"
    "Connor"
    ] 
for item in student_list:
        print("----")
        print(item) 


# implement students function
def stars(num):
    """returns specified stars according to the number of students"""
    value = ""  # placeholder for return value
    # if student num is 6, return 1 stars
    # if student num is 3, return 1 stars
# elif student number is greater than 6, return that num * star
    # else return "No students in this class 🤖"
  
  
    if num == 6 or num == 3:
      
        value = "*"
    
    elif num > 6:
       
        value = "*" * num
   
    else:
        value = "No students in this class 🤖"

    return value

print(stars(6)) 
print(stars(3)) 
print(stars(100))
print(stars(0))

# Ask the user how many boys are in this class
student_boys = input("How many boys are in this class?👨🏻‍🎓")
if student_boys == "3": 
     print("That's correct!😃")
elif student_boys == "6":
          print("That's the total amount of students, not boys.🫤")

# Ask the user how many girls are in this class
student_girls = input("How many girls are in this class?👩🏻‍🎓")
if student_girls == "10":
     print("7 digits less and you're correct!🤖")
     if student_girls == "3":
          print("That's correct!😁")

# say goodbye
          print("You passed the counting test, Congrats!!🎉")
          print("Now I have to attend to important things, goodbye!😎")

       


   

        

     


