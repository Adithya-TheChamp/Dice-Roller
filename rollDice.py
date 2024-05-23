import random
play_again = "y"
while play_again == "y":
    val = random.randint(1,6)
    if val == 1:
        print("{0 0 0}")
        print("{0 1 0}")
        print("{0 0 0}")
    if val == 2:
        print("{1 0 0}")
        print("{0 0 0}")
        print("{0 0 1}")
    if val == 3:
        print("{1 0 0}")
        print("{0 1 0}")
        print("{0 0 1}")
    if val == 4:
        print("{1 0 1}")
        print("{0 0 0}")
        print("{1 0 1}")
    if val == 5:
        print("{1 0 1}")
        print("{0 1 0}")
        print("{1 0 1}")
    if val == 6:
        print("{1 0 1}")
        print("{1 0 1}")
        print("{1 0 1}")
    play_again = input("Do you want to play again (y/n) ")