num=int(input("Please enter the number to be printed in reverse "))
rnum=0
while num>0:
    d= num%10
    rnum= rnum*10+d
    num=num//10
print("The reversed number is ", rnum)
#end