unidades = ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]

while True:
    try:
        quantidade = int(input("Digite a quantidade de armazenamento em números naturais a ser convertida: "))
        break
    except ValueError:
        print("Quantidade inválida. Por favor, digite um número inteiro.")

unidade_entrada = input("Digite a unidade a ser convertida: ")
while unidade_entrada not in unidades:
    print("Unidade não reconhecida, digite a unidade de conversão correta: ")
    unidade_entrada = input()

unidade_saida = input("Digite a unidade para converter em: ")
while unidade_saida not in unidades:
    print("Unidade não reconhecida, digite a unidade de conversão correta: ")
    unidade_saida = input()

def converter_medidas(valor, unidade_entrada, unidade_saida):
    indice_origem = unidades.index(unidade_entrada)
    indice_destino = unidades.index(unidade_saida)

    if unidade_entrada == 'bit':
        valor /= 8
        unidade_entrada = 'byte'
    
    if unidade_saida == 'bit':
        valor /= 8
        unidade_saida = 'byte'
    
    fator = 1024 ** (indice_destino - indice_origem)
    return valor / fator

quantidade = converter_medidas(quantidade, unidade_entrada, unidade_saida)

print("O resultado da conversão é:", quantidade, unidade_saida)
