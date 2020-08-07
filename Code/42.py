# Write a function to compute 5/0 and use try/except to catch the exceptions.

def devision_by_zero():
    return 15/0

try:
    devision_by_zero()
except ZeroDivisionError:
    print("Division by 0")
finally:
    print("Division bt 0, over")