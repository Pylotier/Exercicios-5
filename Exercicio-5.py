#Declaração de variáveis
A: int = 0
B: int = 0
C: int = 0
delta: float = 0
resPositivo: float = 0.0
resNegativo: float = 0.0
#Início
A = int(input("Digite o valor do coeficiente A:"))
B = int(input("Digite o valor do coeficiente B:"))
C = int(input("Digite o valor do coeficiente C:"))

delta = B**2 - 4*A*C
delta = delta**0.5
resPositivo = (-B+delta)/ (2*A)
resNegativo = (-B-delta)/ (2*A)
print("Resultado do x1 (positivo):", resPositivo)
print("Resultado do x2 (negativo):", resNegativo)
#Fim
