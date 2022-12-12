import sys
from random import choice, randint

start = int(sys.argv[1])
end = int(sys.argv[2])

rnumber = randint(start, end)

while True:
    guessed_num = int(input("Guess the number:"))
    if guessed_num == rnumber:
        print("You won!")
        break

