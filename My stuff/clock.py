import time

runtime = int(input("Choose how many seconds of timer you want: "))
timer2 = int(input("Choose how many minutes: "))
timer3 = int(input("Choose how many hours: "))

minutes = timer2 * 60
hours = timer3 * 3600
total = minutes + runtime + hours

count = 1
while count <= total:
    print(count)
    time.sleep(0.001)
    count += 1
    

print("RING!!!!!!!!!!")

