try:
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    
    

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("division = ",n/m)

finally:
    print("program executed")    