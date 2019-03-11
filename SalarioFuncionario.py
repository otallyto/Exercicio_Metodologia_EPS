"""
4. Um algoritmo para calcular o novo salário de um funcionário. Sabe-se que o
funcionário terá aumento de 20%.
"""

salario = int(input("Digite o valor do salário recebido pelo funcionario: "))

aumento = (salario / 100 ) * 20
salarioAumento = salario + aumento

print(f"Salário : {salario} R$")
print(f"Salário com aumento: {salarioAumento} R$")

"""
Entrada
1 - Ler salario

Processamento
1 - Dividir salario por 100 e multiplicar por 20
2 - Somar salario + aumento

Saida
1 - Mostrar o resultado salarioAumento
"""
