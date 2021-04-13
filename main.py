from src import calculator
import time

calc = calculator.Karatsuba()
reader = calculator.Input()

a = reader.int_input("Insira o primeiro numero a ser multiplicado")
b = reader.int_input("Insira o segundo numero a ser multiplicado")

time_karatsuba = time.time()
response_karatsuba = calc.multiply(a, b)
time_karatsuba = time.time() - time_karatsuba

time_naive = time.time()
response_naive = a*b
time_naive = time.time() - time_naive

print(f'O algoritmo de Karatsuba demorou {time_karatsuba} aprensentando o resultado {response_karatsuba}')
print(f'O algoritmo de padrão demorou {time_naive} aprensentando o resultado {response_naive}')
print(f'Apresentou diferença de {response_karatsuba - response_naive}')