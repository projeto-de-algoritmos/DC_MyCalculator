from src import calculator

a, b = map(int, input().split())
calculator = calculator.Karatsuba()
print(calculator.multiply(a, b))