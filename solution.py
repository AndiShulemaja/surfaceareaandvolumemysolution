Count = 0
while (Count !=3) or (would_you_like_to_continue=="yes"):
        Character = input("Enter a character")
        if (Character == "C") or (Character == "B") or (Character=="c") or (Character=="b"):
            Count += 1
            Width=int(input("Enter Width"))
            Height=int(input("Enter Height"))
            Length=int(input("Enter Length"))
            Volume=(Width*Height*Length)
            Surface_Area=2*((Height*Width)+(Height*Length)+(Width*Length))
            print(Volume)
            print(Surface_Area)
            if Count==3:
                would_you_like_to_continue=input("Would you like to continue?")
                if would_you_like_to_continue=="yes":
                        Count=0
                elif would_you_like_to_continue=="no":
                  break
        elif (Character=="e"):
          break
        else:
                print("error")
    

     





        







