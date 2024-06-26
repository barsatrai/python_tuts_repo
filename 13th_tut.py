#-----Functions arguments--------

#Default arguments

def avg(a=4, b=6):
    print("avg is:",(a+b)/2)
avg()
avg(b=2,a=2)  # keyword arguments

#variable name arguments
def name(*name):
    print("hello",name[0],name[1])
name("barsat", "hate")

def average(*num):
    sum = 0
    for i in num:
        sum = sum + 1
    print("ave is:",sum/len(num))
average(2,3,4,5,6)
