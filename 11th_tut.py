#---Break and Continue statement

for i in range(1,15):
    print('5*',i,'=',i*5)
    if(i==10):
        break   # break the loop 
print("out of loop")

#continue
for j in [1,2,3,4,5,6,7,8]:
    if(j%2 != 0):
        continue  # go for next iteration
    print(j)