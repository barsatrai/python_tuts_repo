# Match case statment

x= int(input("Enter x:"))
match x:
    case 0:
        print("YOu choose 0")
    case 1:
        print("you choose 1")
    case 2:
        print("you choose 2")
    case _ if x!= 5:
        print("hey")
    case _ if x!=6:
        print('love')
    case _:
        print("WTF!!!")