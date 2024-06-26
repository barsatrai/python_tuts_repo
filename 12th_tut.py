#-----Functions in python---------
#---> Block of code which perfoms certain task when called



def calc_arith_mean(a,b):
    mean = (a+b)/2
    print(f"mean={mean}")
a = int(input("enter a:"))
b = int(input("enter b:"))
calc_arith_mean(a,b)

#calculation of factorial

n = int(input(("Enter num n:")))
def fact(n):
    if(n<0):
        return 1
    elif(n==0 or n==1):
        return 1
    else:
        return int(n*fact(n-1))     
result = fact(n)
print(f"fact:{result}")
fact(n)
#greater between a,b and c
a= int(input("Enter a:"))
b= int(input("Enter b:"))
c= int(input("Enter c:"))

def greater(a,b,c):
    if(a>b and a>c):
        great = a
        print("a is greater")
    elif(b>a and b>c):
        great = b
        print("b is greater")
    else:
        great = c
        print("c is greater",great)
great = greater(a,b,c)
print(f"greater is:{great}")
greater(a,b,c)

# Area of the tringle
b = int(input("Enter breadth:"))
h = int(input("Enter height:"))
def area(b,h):
    area = 0.5*b*h
    print("area is:",area,"m_square")
area(b,h)

#palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage:
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome")
else:
    print(f"'{input_string}' is not a palindrome")


a = "barsat"
print(a[::-1]) # reverses string

