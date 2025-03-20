##Uses random module to simulate coin flip!

import random

random_integer = random.randint(1, 10)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")