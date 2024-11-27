import random
num=random.randint(1,10)
while True :
    guess= int(input("Give me your best guess: "))
    if num==guess :
        print("wow! you guessed it right!")
        break
    else :
        print("that's not quite right lol, try again")