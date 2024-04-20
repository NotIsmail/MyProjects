import random


n = int(input("Enter the number of players: "))
arr = []
for i in range(n):
    name = input("Enter the name of player {}: ".format(i+1))
    arr.append((name, 0))

for name, _ in arr:
    c = 0
    x = random.randint(1, 99)
    while True:
        a = int(input("Player {}, guess the number(1-99): ".format(name)))
        c += 1
        if a > x:
            print("Lower please")
        elif a < x:
            print("Higher please")
        else:
            print("Correct number!")
            print("It took", c, "guesses for player", name)
            arr[arr.index((name, 0))] = (name, c)
            break

win = min(arr, key=lambda x: x[1])
print("The winner is:", win[0], "with", win[1], "guesses.")
