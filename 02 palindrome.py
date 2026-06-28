#  03 Palindrome check
N = int(input("enter :- "))

dup = 0
rev_num = 0
while N > 0:
    last_digit = N % 10

    N = N // 10
   

    rev_num = rev_num * 10 + last_digit


print("Reverse order of your input number is :- ", rev_num)

if dup == N:
    print("the input number is the palindrome !")

else:
    print(" the input number is not the palindrome")
