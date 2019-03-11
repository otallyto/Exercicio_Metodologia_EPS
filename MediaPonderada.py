"""
2. Um algoritmo que leia as 3 notas de um aluno
e calcule a média ponderada finaldeste aluno.
Considerar os pesos: 2, 3 e 5, respectivamente;
"""

media1 = int(input("Digite a primeira média: "))
media2 = int(input("Digite a segunda média: "))
media3 = int(input("Digite a terceira média: "))

resultado = (media1 * 2 + media2 * 3 + media3 * 5) / 10

print(f"Média = {resultado}")

""" 
Entrada de dados
1 - Ler media1
2 - Ler media2
3 - Ler media3

Processamento
1 - Multiplicar media1 por 2
2 - Multiplicar media2 por 3
3 - Multiplicar media3 por 5
4 - Somar media1 + media 2 + media3
5 - Dividir a soma das medias pela soma dos pesos 2 + 3 + 5 = 10

Saída
1 - Mostrar o resultado
"""
