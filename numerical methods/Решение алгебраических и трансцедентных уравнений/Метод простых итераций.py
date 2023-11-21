#3x - cos(x) -1 = 0
#[0:1]
"""
x = (-cos(x)+1)/3
x' = ((cos(x)+1)/3 )' < 1
"""

from math import cos
def func(x0,e,n):
    while True:
        x1 = ((cos(x0)) + 1) / 3
        c = abs(x1-x0)
        x0 = x1
        n = n + 1
        print(f'\nнач. знач - {x0}, наслед. знач {x1}\nИтерация - {n}\n')
        if c < e:
            break

func(0.5,0.0001,0)

