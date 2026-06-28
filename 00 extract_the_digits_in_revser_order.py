#  Extract the number in the reverse order and print the total counts of the number as well 

N = int(input(' num :- '))

count = 0
while N > 0:
    last_digit = N % 10
    print(last_digit)
    N = N // 10
    count = count + 1
    
print("the count is :- ", count)
