a=str(input("you want to choose left or right"))
if a == "left":
    print("you are in island there is a life")
    b=str(input("wait or swim"))
    if b == "wait":
        print("you are now safe")
        c=str(input("choose one color yellow or red"))
        if c == "yellow":
            print("you won")
        else:
            print("gameover")
            
    else:
       print("gameover")  
        
else:
    print("gameover")
    
