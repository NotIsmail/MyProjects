# SNAKE WATER GUN PROJECT
# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.
# In situations where both players choose the same object, the result will be a draw
import random


def swg(comp, mine):
    if comp == "s" and mine == "g":
        return True
    elif comp == "w" and mine == "s":
        return True
    elif comp == "g" and mine == "w":
        return True
    else:
        return False


choice = ["s", "w", "g"]
comp = random.randint(0, 2)
comp = choice[comp]
mine = input("Enter 's' for snake or 'w' for water or 'g' for gun:")
win = swg(comp, mine)
if win:
    print("You Won")
else:
    print("You Lost")
print("The Computer Chose ", comp, " and you chose ", mine)
