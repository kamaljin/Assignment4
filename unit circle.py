import random
i = 1
noInsideCircle = 0
number = int(input("Enter number of random points: "))

while i <= number:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x * x + y * y < 1:
        noInsideCircle += 1
    i += 1
pi = 4 * noInsideCircle / number
print("Approximate value of pi(π) is: ", pi)