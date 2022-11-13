from src.Math.FiniteField import CARDINAL, NUMBER_OF_ERRORS
from random import randrange

def error(l: list, r=CARDINAL, n=NUMBER_OF_ERRORS) -> list:
    TAILLE = len(l)
    for t in range(n):
        rdm = randrange(0, TAILLE)
        l[rdm] = randrange(0, r)
    return l
