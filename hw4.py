# 1. FizzBuzz

for n in range(1, 100):

    if n % 35 == 0:
        print("FizzBuzz", end=",")
    elif n% 5 == 0:
        print("Fizz", end=",")
    elif n% 7 == 0:
        print("Buzz", end=",")
    else:
    print(n)

 # 2. Christmas tree

a=3
for i in range(3):
  print(" "*a,end="")
  print("*"*(2*i+1))
  a-=1


# 3. Primes Check if entered positive number is a prime number.

num = int(input("Please enter a number: "))
if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
