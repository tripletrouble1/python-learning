n=int(input("enter a number"))
sum=0
b=n
while(b>0):
    a=b%10
    sum+=a**3
    b//=10
if n==sum:
    print("is a amstrong number")
else:
    print("is not a amstrong number")
      
      

      
      
