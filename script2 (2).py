lower = int(input("Enter the low value:"))
higher = int(input("Enter the high value:"))
for num in range(lower, higher+1):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
