import pyfinite.genericmatrix as pmat
from src.FiniteField import CARDINAL, DEGREE_POLYNOME_Q0, DEGREE_POLYNOME_Q1, power, X, F
from src.Matrix import adn, subn, multn, divn 
from src.Polynomial import Polynomial

def decode_polynomial(message : list)->list:
    # definition of M from the message 
    matrix = pmat.GenericMatrix((CARDINAL, DEGREE_POLYNOME_Q0 + DEGREE_POLYNOME_Q1 + 2), zeroElement=0, identityElement=1, add=adn, sub=subn, mul=multn, div=divn)
    for indice in range(1, CARDINAL+1):
        ligne = []
        for j in range(DEGREE_POLYNOME_Q0 + 1):
            ligne.append(power(X[indice], j))
        for k in range(DEGREE_POLYNOME_Q1 + 1):
            ligne.append(F.Multiply(message[indice-1], power(X[indice], k)))
        matrix.SetRow(indice-1, ligne)
    upper_matrix = matrix.LUP()[1]  # u is the matrix U of the LU decomposition of M
    
    # Gauss pivot
    polynome_q = [X[1]]  # Cauchy system
    TAILLE = DEGREE_POLYNOME_Q0 + DEGREE_POLYNOME_Q1 + 2
    for i in range(1, TAILLE):
        monome = 0
        for j in range(1, len(polynome_q) + 1):
            monome = F.Add(monome, F.Multiply(upper_matrix[TAILLE - i - 1, TAILLE - j], polynome_q[-j]))
        if monome == 0:
            polynome_q = [monome] + polynome_q
        else:
            monome = F.Divide(monome, upper_matrix[TAILLE - i - 1, TAILLE - i - 1])
            polynome_q = [monome] + polynome_q
    Q1 = Polynomial(polynome_q[DEGREE_POLYNOME_Q0 + 1:])  # define the polynomial Q1
    Q0 = Polynomial(polynome_q[:(len(polynome_q) - (DEGREE_POLYNOME_Q1 + 1))])  # définition de Q0
    return (Q0//Q1)[0]  # le message initialement envoyé