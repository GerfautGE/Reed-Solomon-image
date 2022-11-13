# Reed-Solomon-image

this is a simple program to encode and decode images using Reed-Solomon codes.

it is written in Python 3.x and uses the [Pyfinite Module](https://github.com/emin63/pyfinite) from [@Emin63](https://github.com/emin63/pyfinite).

---

## Usage

### Encoding

```Python
from src.Coding.Encode import encode
from src.Math.FiniteField import CARDINAL,  MESSAGE_SIZE
from random import randrange()

message = [randrange(0, CARDINAL) for _ in range(MESSAGE_SIZE)]

encoded = encode(message)
```

### Error generation

```Python
from src.Error import error

error(encoded) # errors are generated in place
```

### Decoding

#### Using Polynomial Algorithm

```Python
from src.Coding.DecodePolynomial import decode_polynomial

decoded = decode_polynomial(encoded)
```

#### Using Syndrome Algorithm

```Python
from src.Coding.DecodeSyndrome import decode_syndrome

decoded = decode_syndrome(encoded)
```
