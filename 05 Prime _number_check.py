# Divisor Counting (Brute Force) → O(n) ✅ (good for learning)

"""n = int(input("enter the number:- "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("prime number")
else:
    print("not a prime number")"""

# method 02 : Check divisibility till √N → O(√n) ⭐ (most common in interviews)

n = int(input("Enter the number: "))

count = 0

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        count += 1

        if n // i != i:
            count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")


# Sieve of Eratosthenes → O(n log log n) 🚀 (best for finding many primes)