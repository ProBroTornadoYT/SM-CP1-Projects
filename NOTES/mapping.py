import math


def times(number):
    return number *2

numbers = range(1,6)

multiplied_numbers = map(times, numbers)

print(*list(multiplied_numbers))


new_numbers = []

for number in numbers:
    new_numbers.append(number*2)

print(*new_numbers)

siblings = ["Amaia", "Kayla", "Cersei", "Mercy"]

length = list(map(len, siblings))
print(*length)


def product(complete):
    return complete * group

group = []

print(math.factorial(5))

