maxNumber = 10

def fibonacci_recursion(n):
    if n == 0:
        return 0
    elif n == 1 or n ==2:
        return 1

    return fibonacci_recursion(n-2)+ fibonacci_recursion(n-1)

for i in range(maxNumber):
    print(fibonacci_recursion(i))
