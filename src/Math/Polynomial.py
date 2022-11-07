from src.Math.FiniteField import power, F

def trimseq(seq):
    if len(seq) == 0: return seq
    else: 
        for i in range(len(seq)-1, -1, -1):
            if seq[i] != 0:
                break
        return seq[:i+1]

def as_series(alist : list) -> list:
    arrays = [trimseq(a) for a in alist]
    if min([len(a) for a in arrays]) == 0:
        raise ValueError("Coefficient array is empty")
    return arrays


class Polynomial():
    
    def __init__(self,coef):
        """
        coef : array_like
        Polynomial coefficients in order of increasing degree, i.e.,
        ``(1, 2, 3)`` give ``1 + 2*x + 3*x**2``.
        """
        assert type(coef) == list 
        self.coef = trimseq(coef)
        pass
    
    def __repr__(self):
        return "".join(str(self.coef))

    def degree(self):
        if self.coef == [0] : return -1
        return len(trimseq(self.coef))

    def leading(self):
        return self.coef[-1]

    def __add__(self, other):
        if type(other) != Polynomial : raise TypeError
        [c1, c2] = as_series([self.coef, other.coef])
        l1, l2, ret = len(c1), len(c2), []
        if l1 > l2:
            for (x1, x2) in zip(c1[:l2], c2):
                ret.append(F.Add(x1, x2))
            ret += c1[l2:]
        else : 
            for (x1, x2) in zip(c2[:l1], c1):
                ret.append(F.Add(x1, x2))
            ret += c2[l1:]
        return Polynomial(ret)

    def __sub__(self, other):
        if type(other) != Polynomial : raise TypeError
        [c1, c2] = as_series([self.coef, other.coef])
        l1, l2, ret = len(c1), len(c2), []
        if l1 > l2:
            c1[:c2.size] -= c2
            ret = c1
            for (x1, x2) in zip(c1[:l2], c2):
                ret.append(F.Subtract(x1, x2))
            ret += c1[l2:]
        else :
            for (x1, x2) in zip(c1[:l1], c2):
                ret.append(F.Subtract(x1, x2))
            ret += c2[l1:]
        return Polynomial(ret)

    def __mul__(self, other):
        if type(other) != Polynomial : raise TypeError
        [c1, c2] = as_series([self.coef, other.coef])
        l1, l2, ret = len(c1), len(c2), []
        for s in range(l1+l2+1):
            r = 0
            for k in range(s+1):
                try:
                    r = F.Add(F.Multiply(c1[k], c2[s-k]), r)
                except IndexError:
                    pass
            ret.append(r)
        return Polynomial(ret)


    def __floordiv__(self, other):
        if type(other) != Polynomial : raise TypeError
        if other.degree() == 0 : raise ZeroDivisionError
        if other.degree() > self.degree() : return Polynomial([0]), self #not divisible
        else : 
            q = Polynomial([0])
            r = self
            while r.degree() >= other.degree():
                q += Polynomial([0]*(r.degree() - other.degree())+ [F.Divide(r.leading(),other.leading())])                                                                              
                r += q*other
            return q, r
    
    def __eq__(self, other):
        if type(other) != Polynomial : raise TypeError
        return self.coef == other.coef