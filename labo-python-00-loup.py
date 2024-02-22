#   NAME : labo-python-00-loup.py
#   Version : 0.1
#   AUTHOR  : Loup Olivia
#   DESCRIPTION : Start to understand how to use python
from math import sqrt
import cmath
def delta (a, b, c):
    """function to create Viete formula

    Args:
        a (_type_): value from x**2
        b (_type_): value from x
        c (_type_): value from x = 0
        
    """
    return b**2-(4*a*c)

def solve(a, b, c) :
    """Function to give solution of equation in scnd degree

    Args:
        a (_type_): value from x**2
        b (_type_): value from x
        c (_type_): value from x = 0
    """
    var_delta = delta(a,b,c)
    print(var_delta)
    if var_delta < 0 :
        var_delta = var_delta.imag
    x1 = (-b + sqrt(var_delta))/(2*a)
    x2 = (-b - sqrt(var_delta))/(2*a)
    return x1, x2

x1, x2 = solve(1,2,3)
print(f"Results of euqation x**2 + 3x + 2 are : {x1:.5f} and {x2:.5f}")