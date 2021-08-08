def fibonacci_rec(n):
    if type(n)!=int:
        return "Input is not valid"
    if n < 0 :
        return "Input is not valid"
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
       return fibonacci_rec(n-1)+fibonacci_rec(n-2)
def fibonacci_loop(n):
    if type(n)!=int:
        return "Input is not valid"
    if n < 0 :
        return "Input is not valid"
    if n==0:
        return 0
    elif n==1:
        return 1
    x=0
    y=1
    for i in range(2,n+1):
        z=x+y
        x=y
        y=z
    return y
print(fibonacci_rec(5))
print(fibonacci_loop(7))
