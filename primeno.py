#Program to check whether the number is prime pr not
num=int(input("Enter a number"))
c=0
if num>1:
 for i in range(2,num):
    if (num%i)==0:
        c+=1
if c==0:
 print("the number is prime")
else:
    print("the number is not a prime")