def FizzBuzz(x):

    if x%3 == 0:
        return "Fizz"
    if x%5 == 0:
        return "Buzz"
    if x%3 or x%5 == 0:
        return "FizzBuzz"
    else:
        return "none"

for x in range(10) :
    print(f"{FizzBuzz(x)}:{x}")