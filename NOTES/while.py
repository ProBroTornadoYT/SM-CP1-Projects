# SM, While Loops

import random
import time

goose = random.randint(1,20)
duck = 1

while goose > duck:
    print("duck. . .")
    time.sleep(1.0)
    duck += 1

print("GOOSE!")

count = 1
while count < 30:
    print(count)
    time.sleep(.1)
    count += 1