from src.Matrix import ENCODE_MATRIX

def encode(message):
    return ENCODE_MATRIX.LeftMulColumnVec(message)