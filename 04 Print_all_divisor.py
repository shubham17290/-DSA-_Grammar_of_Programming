n = int(input(" Yes enter you number here :- "))

large = []

for i in range(1, int(n**0.5) + 1): # this Will going to take O(sqrt(n))

    if n % i == 0:
        print(i, end=" ")

        if i != n // i:
            large.append(n // i) # TC: O(log(n))

for i in reversed(large):
    print(i, end=" ")
