def my_function(x):
    try:
        if x == 0:
            return 0
        else:
            return 1 / x
    except ZeroDivisionError:
        return float('inf') #Or handle the error as you see fit

print(my_function(0)) #returns infinity
print(my_function(1))