coin = int(input("Flip the coin by entering number: "))
import random

random_side = random.randint(0,1)

# print(random_side)
if random_side == 1:
    print("Heads")
else:
    print("Tails")