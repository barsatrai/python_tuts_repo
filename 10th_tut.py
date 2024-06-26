# Loops in pytthon

#For loop
name = "barsat"
for i in name:
    print(i)
    if(i=="s"):
        print(":S in barsat mean Superior!!")

list = ['apple','mango','litchi','banana']
for i in list:
    print(i)

for n in range(5,10): #(start,end)
   print(n)

for k in range(5):   #(0,end)
   print(k," ")

for l in range(0,10,2): #(start,end,stepsize)
   print(l)

## while loops-----------------

i = int(input("Enter i:"))
while(i<=10):
    i = int(input("Enter i:"))
print(i,'out of loop')

count = 10
while(count>0):
    print(count)
    count -= 1
else:
    print("out of loop!")

#do-while loop

counter = 0

while True:
    counter += 1
    print(f"Counter is {counter}")

    if counter >= 5:
        break
##examples__________________
#sum of all numbers from 1to 100
sum = 0
for i in range(1,100):
    sum = sum+i
    print(sum)

#even numbers  from 1-50
for j in range(1,50):
    if(j%2 == 0):
        print(j)
    
#Multiplication table
n = int(input("Enter the number u want to multiplication table:"))
for i in range(1,11):
    r = i*n
    print(f"{i}*{n}={r}\n")


