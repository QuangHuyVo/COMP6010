#Question 1: 
#Write a condition that:
#print out "this statement is less than 5" if a variable x is less than 5,
#otherwise, print out "this statement is NOT less than 5"

x = 7
if (x < 5):
    print("this statement is less than 5")
else:
    print("this statement is NOT less than 5")

#Question 2: 
#Alter the above condition to:
#print out "this statement is less than 5" if a variable x is less than 5,
#print out "x is equal to 5", if the variable x is equal to 5,
#otherwise, print out "x is greater than 5"

x = 5
if type(x) is int:   
    if (x < 5):
        print("this statement is less than 5")
    elif (x == 5):
        print("x is equal to 5")
    else:
        print("this statement is NOT less than 5")

#Question 3: 
x = "abc"
if type(x) is int:   
    if (x < 5):
        print("this statement is less than 5")
    elif (x == 5):
        print("x is equal to 5")
    else:
        print("this statement is NOT less than 5")
else: 
    print("x is not a number")

#Question 4: 

assignmentMark = 6.5
assignmentMarkedOutOf = 9
grade = (assignmentMark / assignmentMarkedOutOf) * 100
percentage = (round(grade,2))
print(percentage,"%")

if (0 < grade < 100):
    if (grade <50):
        print ("F")
    elif (50 <= grade <65):
        print ("Pass")
    elif (65 <= grade <75):
        print ("Credit")
    elif (75 <= grade <85):
        print ("Distinction")
    elif (85 <= grade <= 100):
        print ("High Distinction")
else: 
    print ("error")