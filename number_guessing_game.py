print("\n\t\t\t\tNUMBER GUESSING GAME\t\t\t\t\n\t\t\t\t********************\t\t\t\t\t")
import random
name=input("ENTER YOUR NAME:")
a=int(input("Enter the starting point"))
b=int(input("Enter the ending point"))
hello =(f"\n                In this game you have to guess a no between {a} to {b} \n\t\t\tlets start the game")
print(hello.upper())
winning_numb=random.randint(a,b)
i=1
game_over=False
while not game_over:
    guess_numb=int(input("Guess the no:"))
    if winning_numb==guess_numb:
        print("\n\t\tYOU WIN")
        game_over=True
    elif guess_numb>winning_numb:
        print("Sorry,You guess too high")
        i+=1
    elif guess_numb<winning_numb:
        print("Sorry, You guess too low")
        i+=1
print(f"Congratulations, {name} You guessed the right no in {i} attempt")
