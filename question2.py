# Define a class with a generator which can iterate the numbers, which are divisible
# by 7, between a given range 0 and n.

#Solution


n = int(input())
result = [i for i in range (0,n) if (i%7==0)]
print(result)

def divChecker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)
divChecker(n)
