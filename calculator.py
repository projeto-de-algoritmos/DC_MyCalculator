from math import ceil, floor

class Karatsuba:
    
    def multiply(self, x, y):

        # Caso base
        if x < 10 and y < 10:
            return x*y
        
        size = max(len(str(x)), len(str(y)))

        # x = a*10**(size/2) + b
        # y = c*10**(size/2) + d

        n_size = ceil(size // 2)
        power = 10**n_size
        a = floor(x // power)
        b = x % power
        c = floor(y // power)
        d = y % power

        ac = self.multiply(a, c)
        bd = self.multiply(b, d)
        e = self.multiply(a+b, c+d)

        return int(10 ** (2 * n_size) * ac + (10 ** n_size) * e + bd)