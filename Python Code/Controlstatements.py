# If statement
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Nested loops
for i in range(3):
    for j in range(2):
        print(i, j)

# Pass statement
for i in range(3):
    if i == 1:
        pass
    else:
        print(i)
