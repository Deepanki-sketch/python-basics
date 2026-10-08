def GCD(a, b):
    if(a==0 and b==0):
        return "Invalid result"
    elif(a==0 or b==0):
        return a if b==0 else b
    elif(a==b):
        return a
    if(a>b):
        return GCD(a%b,b)
    else:
        return GCD(a,b%a)
print(GCD(10, 15))    