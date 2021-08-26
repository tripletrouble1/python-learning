a=int(input("english marks"))
b=int(input("maths marks"))
c=int(input("physics mark"))
d=int(input("chemistry mark"))
e=int(input("computer mark"))
g=a+b+c+d+e//5
print(f"avg is {g}")
if(g>60):
    print(f"{g} good")
else:
    print(f"{g} slightly bad")
