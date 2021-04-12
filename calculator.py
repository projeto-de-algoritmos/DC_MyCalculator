class Karatsuba:
    def normalize_size(self, a, b):
        size_a = len(a)
        size_b = len(b)

        # Padronizar para que a menor string seja a string 'a'
        if size_a > size_b:
            a, b = b, a
            size_a, size_b = size_b, size_a
        
        # Igualando os tamanhos
        while size_a < size_b:
            a = '0' + a
            size_a += 1
        
        power = 1

        while power < size_a:
            power *= 2
        
        a = '0'*(power - size_a) + a
        b = '0'*(power - size_b) + b
    
    def multiply(self, a, b):
        # Para facilitar podemos deixar as duas strings com tamanho em potência de 2
        a, b = normalize_size(str(a), str(b))