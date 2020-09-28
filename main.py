#fizzbuzz exercise

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0: #if a number is both divisible by 5 and 3
       print("fizzbuzz")
       continue
    elif num % 3 == 0:
        print("fizz")
        continue
    elif num % 5 == 0:
        print("buzz")
        continue
    print(num)

