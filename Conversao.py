"""
3. Um algoritmo que leia um valor a ser pago em bolívar venezuelano,
e calcule a conversão deste valor para real, sabendo que
o câmbio do dia é 1(um) real para 210(duzentos e dez ) bolívares.
"""
bolivar = int(input("Digite o valor em bolivar para converter em real: "))

conversao = bolivar / 210

print(f"{bolivar} bolivares é igual a {conversao:.4f}  R$ reais")

"""
Entrada
1 - Ler valor em bolivar

Processamento
1 - Dividir bolivar por 210

Saida
1 - Mostrar o resultado de conversao
"""
