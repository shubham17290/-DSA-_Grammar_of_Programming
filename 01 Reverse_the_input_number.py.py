"""
N = int(input("enter the digits :- "))
print(" The input order of your number is:- ", N)
count = 0
rev_num = 0
while N > 0:
    last_digit = N % 10

    N = N // 10
    print("The lastly extracted digit is :- ", last_digit)
    rev_num = rev_num * 10 + last_digit
    print("Now your reverse number is:- ", rev_num)
    count = count + 1

print("Reverse order of your input number is :- ", rev_num)
print("the count of the digits is :- ", count)
"""
