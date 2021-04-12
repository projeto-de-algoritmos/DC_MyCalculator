from math import ceil, floor

class Karatsuba:
    def __init__(self):
        pass
    
    def multiply(self, x, y):

        # Caso base
        if x < 10 and y < 10:
            return x*y
        
        size = max(len(str(x)), len(str(y)))

        n_size = ceil(size / 2)
        power = 10**n_size

        a = x // power
        b = x % power
        c = y // power
        d = y % power

        ac = self.multiply(a, c)
        bd = self.multiply(b, d)
        e = self.multiply(a+b, c+d) - ac - bd


        response = int(10 ** (size) * ac + (10 ** n_size) * e + bd)
        return response
