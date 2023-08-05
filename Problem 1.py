def factorial(x):
    factorial=1
    if x<0:
        return "Number is less than or equal to zero"
    else:
        for i in range(1,x+1):
            factorial=i*factorial

        return factorial
print(factorial(3))