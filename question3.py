# Please write a program using a generator to print the numbers which can be
# divisible by 5 and 7 between 0 and n in comma separated form while n is
# input by console.

# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be: 0,35,70


#Solution


n = int(input())
result = [i for i in range(0,n) if (i%7 == 0) and (i %5 == 0 )]
print(result)

def divChecker(n):
    for i in range (n):
        if i % 7 == 0 and i % 5 == 0 :
            value = i
        else :
            value = " "
        print(value)
