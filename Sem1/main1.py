# a*x² + b*x + c

"""
Raiz de uma equação quadrática
"""

import math

from math import sqrt

def raizes(a, b, c):
    delta = b*b - 4*a*c

    if a == 0:
        return -c/b
    elif delta < 0:
        return None
    elif delta == 0:
        return -b/(2*a)
    else:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + delta**0.5)/(2*a)
        return x1, x2

def main():
    x = raizes(1, -6, 5)
    print(x)

if __name__ == "__main__":
    main()
