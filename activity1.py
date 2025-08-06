import random
playing = True
number = str(random.randint(10,20))

print("i will guess a number from one to 20 and you need to guess it")

while playing:
    guess = (input("give me your best guess!\n"))
    if number == guess:
        print("you win")
        print("the number was ", number)
        break
    else:
        print("that wasnt right")