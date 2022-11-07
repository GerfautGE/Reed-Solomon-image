from src.Math.FiniteField import CARDINAL, NUMBER_OF_ERRORS
from random import randrange

def error(l: list, r=CARDINAL, n=NUMBER_OF_ERRORS) -> list:
    list_copy = l.copy()
    TAILLE = len(list_copy)
    for t in range(n):
        rdm = randrange(0, TAILLE)
        list_copy[rdm] = randrange(0, r)
    return list_copy
