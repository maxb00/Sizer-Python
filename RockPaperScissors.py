print("Welcome to Rock, Paper, Scissors! Start thinking of your choice... (Default is scissors, so type right!")
PlayerOne = input("Enter player one's choice:")
PlayerTwo = input("Enter player two's choice:")

def checkRPS(x,y):
    if x == "Rock" or x == "rock":
        first = 1
    elif x == "Paper" or x == "paper":
        first = 2
    else:
        first = 3

    if y == "Rock" or y == "rock":
        second = 1
    elif y == "Paper" or y == "paper":
        second = 2
    else:
        second = 3

    if first == 1 and second == 2:
        result = "Player two wins!"
    elif first == 2 and second == 3:
        result = "Player two wins!"
    elif first == 3 and second == 1:
        result = "Player two wins!"
    elif second == 1 and first == 2:
        result = "Player one wins!"
    elif second == 2 and first == 3:
        result = "Player one wins!"
    elif second == 3 and first == 1:
        result = "Player one wins!"
    else :
        result = "Tie!"

    return result

print(checkRPS(PlayerOne, PlayerTwo))
#end