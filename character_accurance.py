str=input("Please enter your own word:")
char= input("Please enter your own character:")
i=0
count=0
while(i<len(str)):
    if(str[1]==char):
        count=count+1
    i=i+1

    print("The total number of times", char,"Has occured=", count)
    

