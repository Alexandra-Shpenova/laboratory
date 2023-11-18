# x^3 + 4x - 6 = 0

e = 0.0001
a = -5
b = 5
n = 0

while True:
    x = (a + b)/2
    f1 = (a ** 3) + (4 * a) - 6 # <- f(a)
    f2 = (x ** 3) + (4 * x) - 6 # <- f(x)
    if f1 * f2 > 0:
        a = x
    else:
        b = x
    n += 1
    print(x, f2, n)
    if abs(b - a) < e  :
        break

