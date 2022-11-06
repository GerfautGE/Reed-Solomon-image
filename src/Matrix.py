import pyfinite.genericmatrix as pmat
from src.FiniteField import F, power, X, CARDINAL, MESSAGE_SIZE

def adn(x, y): 
    return F.Add(x, y)

def subn(x, y): 
    return F.Subtract(x,y)

def multn(x, y):
    return F.Multiply(x, y)

def divn(x, y):
    if x == 0:
        return 0
    else:
        return F.Divide(x, y)
    
ENCODE_MATRIX = pmat.GenericMatrix((CARDINAL, MESSAGE_SIZE), zeroElement=0, identityElement=1, add=adn, sub=subn, mul=multn, div=divn)
PARTIAL_ENCODE_MATRIX = pmat.GenericMatrix((MESSAGE_SIZE, MESSAGE_SIZE), zeroElement=0, identityElement=1, add=adn, sub=subn, mul=multn, div=divn)
for i in range(1, CARDINAL + 1):
    ligne = []
    for j in range(0, MESSAGE_SIZE):
        ligne.append(power(X[i], j))
    if i <= MESSAGE_SIZE: PARTIAL_ENCODE_MATRIX.SetRow(i - 1, ligne)
    ENCODE_MATRIX.SetRow(i - 1, ligne)    
ENCODE_MATRIX_INVERSE = PARTIAL_ENCODE_MATRIX.Inverse()

CONTROL_MATRIX = pmat.GenericMatrix((CARDINAL - MESSAGE_SIZE, CARDINAL), zeroElement=0, identityElement=1, add=adn, sub=adn, mul=multn, div=divn)
for i in range(CARDINAL - MESSAGE_SIZE):
    ligne = []
    for j in range(CARDINAL):
        ligne.append(power(X[j + 1], i + 1))
    CONTROL_MATRIX.SetRow(i, ligne)