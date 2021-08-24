a=int(input("enter  a weight in kg"))
b=int(input("enter a height in m"))
c=a/b
if (c<18.5):
    print('thin')
elif(c>18.5 and c<24.9):
    print('healthy')
