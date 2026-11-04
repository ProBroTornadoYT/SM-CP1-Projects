import time

timer = int(input("Choose how many seconds of timer you want: "))

count = 1
while count <= timer:
    print(count)
    time.sleep(1.0)
    count += 1

print("RING!!!!!!!!!!")

