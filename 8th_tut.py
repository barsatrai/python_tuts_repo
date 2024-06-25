# Else-if statement
age = int(input("Enter your age:"))
print("your age is:",age)
if age >= 18:
    print("you can vote!!")
else:
    print("you can't vote!!")

#Conditional operators
# > = greatr than
# < = less than
# >= = greater and equal
# <= = less than and equal
# != = not equal
# Else-if ladder example
num = int(input("Enter the number from 1 to 7:"))
if(num==1):
    print("Sunday")
elif(num==2):
    print("Monday")
elif(num==3):
    print("tuesday")
elif(num==4):
    print("Wednesday")
elif(num==5):
    print("Thursday")
elif(num==6):
    print("Friday")
elif(num==7):
    print("Saturday")
else:
    print("Enter valid number!")

# Nested if(if within if)

print("Is it going to rain today??")
h = float(input("Enter the humidity:"))
if(h>0.9):
    print("Probly tor rain")
elif(h==0.9):
    ppt = float(input("Enter the precipitaion:"))
    if(ppt>0.8):
        print("It is going to rain")
    elif(ppt==0.8):
        print("Might be rain today;")
    else:
        print("Might not be rain")
else:
    print("Can't be rain")
