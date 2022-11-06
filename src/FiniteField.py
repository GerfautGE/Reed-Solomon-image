import pyfinite.ffield as pf
from math import sqrt

# number of element in the field : 
CARDINAL = 15
F = pf.FField(int(sqrt(CARDINAL + 1)))
 
MESSAGE_SIZE = 9
PRIMITIVE = 2


def power(x : int, n : int) -> int :
    if n == 0 : return 1
    if n == 1 : return x
    if (n%2 == 0) :
        return power(F.Multiply(x, x), n/2)
    if (n%2 == 1) : 
        return F.Multiply(x, power(F.Multiply(x, x), (n-1)/2))

X = [0] + [power(PRIMITIVE, p) for p in range(CARDINAL)]
