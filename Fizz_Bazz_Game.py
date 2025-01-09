
# Take the numbers from 1 to 100

for number in range(1, 101):

    # If the number divisible by 3 and 5

    if ((number % 3) == 0) & ((number % 5) == 0):
        print("FizzBuzz")

    # If the number divisible by 3

    elif (number % 3) == 0:
        print("Fizz")

    # If the number divisible by 5

    elif (number % 5) == 0:
        print("Buzz")

    else:
       print(number)