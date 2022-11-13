from src.Coding.Encode import encode
from src.Math.FiniteField import MESSAGE_SIZE
from  matplotlib.image import imread
import numpy as np

def Memoize(f):
    cache = {}
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = f(*args, **kwargs)
        return cache[args]
    return wrapper

@Memoize
def hexa(i : int):
    return i//16, i%16

class Image(list):
    
    """Array of Arry of uint8"""
    
    def __init__(self, path: str):
        try :
            super().__init__(imread(path))
        except OSError:
            print("Error: Image not found")
            exit()
            
    def size(self) -> tuple[int, int]:
        """
        return wigth, height

        Returns:
            tuple[int]: width, height
        """
        return len(self[0]), len(self)
    
    def __repr__(self) -> str:
        return f"Image {self.size()}"
    
    def to_send(self):
        one_line = np.array(self).flatten()
        if len(one_line) % MESSAGE_SIZE != 0:
            one_line = np.append(one_line, np.zeros(MESSAGE_SIZE - len(one_line) % MESSAGE_SIZE, dtype=np.uint8))
        l = [x for y in list(map(hexa, one_line)) for x in y]
        return [l[k*MESSAGE_SIZE:(k+1)*MESSAGE_SIZE] for k in range(len(l)//MESSAGE_SIZE)]
        
    def encode(self):
        return [encode(_) for _ in self.to_send()]