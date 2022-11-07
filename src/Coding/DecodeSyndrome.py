from src.Math.FiniteField import CARDINAL, MESSAGE_SIZE, F, DEGREE_POLYNOME_Q0, DEGREE_POLYNOME_Q1, power, X
from src.Math.Matrix import CONTROL_MATRIX, ENCODE_MATRIX_INVERSE, syndrome_extracted, control_extracted


def decode_syndrome(message: list)->list:
    assert (CARDINAL-MESSAGE_SIZE) % 2 == 0 # CARDINAL-MESSAGE_SIZE = 2 * DEGREE_POLYNOME_Q1
    
    "syndrome decoding"
    syndrome = CONTROL_MATRIX.LeftMulColumnVec(message)
    if all([x == 0 for x in syndrome]): # if syndrome == 0
        return ENCODE_MATRIX_INVERSE.LeftMulColumnVec(message[:9]) # No error
    
    "find the index of the error"
    SYNDROME_EXTRACTED_MATRIX = syndrome_extracted(syndrome)
    UPPER = SYNDROME_EXTRACTED_MATRIX.LUP()[1]  # Upper triangular matrix
    
    "Gauss-Jordan elimination"
    coef = [X[1]]  # give a value for Cauchy system
    TAILLE = DEGREE_POLYNOME_Q1 + 1
    for element in range(1, TAILLE):
        a = 0
        for colonne_j in range(1, len(coef) + 1):
            a = F.Add(a, F.Multiply(UPPER[TAILLE - element - 1, TAILLE - colonne_j], coef[-colonne_j]))
        if a == 0:
            coef = [a] + coef
        else:
            a = F.Divide(a, UPPER[TAILLE - element - 1, TAILLE - element - 1])
            coef = [a] + coef
        print(coef)
    indice = []
    
    coef.reverse()
    for element in range(0, 16):  # on test pour chaque élément non nul du corps
        evaluation_q1 = 0
        for l in range(DEGREE_POLYNOME_Q1+1):  # On somme chaque monome pour reformer Q1(element)
            e = evaluation_q1
            evaluation_q1 = F.Add(e, F.Multiply(coef[l], power(X[element], DEGREE_POLYNOME_Q1-l)))
        if evaluation_q1 == 0:
            indice.append(element-1)
    CONTROL_EXTRACTED_MATRIX = control_extracted(indice)
    s_sol = [syndrome[i] for i in range(len(indice))]
    I = CONTROL_EXTRACTED_MATRIX.Solve(s_sol)
    E = [0]*15
    for element in range(len(s_sol)):
        E[indice[element]] = I[element]
    C = [F.Add(message[i], E[i]) for i in range(9)]
    
    return ENCODE_MATRIX_INVERSE.LeftMulColumnVec(C)
