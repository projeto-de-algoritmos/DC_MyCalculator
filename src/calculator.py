from math import ceil, floor

class Multiply:
    def __init__(self):
        pass
    
    def karatsuba(self, x, y):

        # Caso base
        if x < 100 and y < 100:
            return x*y
        
        size = max(len(str(x)), len(str(y)))

        n_size = ceil(size // 2)
        power = 10**n_size

        a = x // power
        b = x % power
        c = y // power
        d = y % power

        ac = self.karatsuba(a, c)
        bd = self.karatsuba(b, d)
        e = self.karatsuba(a+b, c+d) - ac - bd


        response = int(10 ** (n_size*2) * ac + (10 ** n_size) * e + bd)
        return response
    
    def naive(self, x, y):
        result = 0
        power = 1
        while y > 0:
            digit = (y % 10)*power
            tmp_x = x

            while tmp_x > 0:
                result += digit * (tmp_x % 10)
                tmp_x = tmp_x // 10
                digit *= 10
            
            y = y // 10
            power *= 10

        return result

class Input:
    def int_input(self, message):
        print(message + ':')
        num = input()

        while not num.isdigit():
            print("Insira apenas numeros (sem espaços):")
            num = input()
        return int(num)