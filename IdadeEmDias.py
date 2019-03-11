"""
5. Um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e
mostre-a expressa apenas em dias. Considerar que um ano tenha 365 dias e um
mês tenha 30 dias;
"""
anos = int(input("Digite quantos anos tem: "))
meses = int(input("Digite quantos meses tem: "))
dias = int(input("Digite quantos dias tem: "))

idadeEmDias = anos * 365 + meses * 30 + dias

print(f"Sua idade em dias é: {idadeEmDias}")

"""
Entrada
1 - Ler anos
2 - Ler meses
3 - Ler dias

Processamento
1 - Multiplicar anos por 365
2 - Multiplicar meses por 30
3 - Somar anos + meses + dias

Saída
1 - Mostrar o resultado idadeEmDias
"""