# fizzbuzz: print every integer from 1 to 100, inclusive, on a new line. =
# If the number is divisible by 3, print “Fizz” instead.
# If it is divisible by 5, print “Buzz.” =
# If it is divisible by both 3 and 5, print “FizzBuzz.”

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
