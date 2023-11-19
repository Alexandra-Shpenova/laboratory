# x^3 + 4x - 6 = 0
def first_func(e,a,b,n):
    while True:
        x = (a + b)/2
        f1 = (a ** 3) + (4 * a) - 6 # <- f(a)
        f2 = (x ** 3) + (4 * x) - 6 # <- f(x)
        if f1 * f2 > 0:
            a = x
        else:
            b = x
        n += 1
        if abs(b - a) < e  :
            break
    return(x, f2, n)

print(first_func(0.0001,-5,5,0))

