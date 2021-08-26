bill=0
x=str(input("which size pizza do you want type 'small','medium','large'."))
if x == "small":
    bill+=20
elif x == "medium":
    bill+=30
elif x == "large":
    bill+=40
y=str(input("if you want pepper onion type 'yes' or 'no'."))
if y == "yes":
    
    if x == "small":
        bill+=5
    elif x == "medium":
        bill+=10
    elif x == "large":
        bill+=15
else:
    print(bill)
z=str(input("if you want cheese type 'yes' or 'no'."))
if z == "yes":
    print("proceed")
    if x == "small":
        bill+=10
    elif x == "medium":
        bill+=15
    elif x=="large":
        bill+=20
else:
    print(bill)
print(bill)
    
    
    
