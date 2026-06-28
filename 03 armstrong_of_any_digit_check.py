#  03 Palindrome check
N = int(input("enter :- "))

dup = N
sum = 0
while N > 0:
    last_digit = N % 10

    sum = sum + last_digit * last_digit * last_digit

    N = N // 10


if sum == dup:
    print("input is Armstrong number ")

else:
    print(" input is not Armstrong number ") 
