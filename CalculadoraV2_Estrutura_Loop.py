unidades = ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]

def converter_medidas(valor, unidade_entrada, unidade_saida):
    indice_origem = unidades.index(unidade_entrada)
    indice_destino = unidades.index(unidade_saida)
    fator = 1024**(indice_destino - indice_origem)
    return valor * fator

quantidade = int(input("Digite a quantidade de armazenamento em números naturais a ser convertida: "))

unidade_entrada = input("Digite a unidade a ser convertida: ")

while unidade_entrada not in unidades :
    print("Unidade não reconhecida, digite a unidade de conversão correta: ")
    unidade_entrada = input()

unidade_saida = input("Digite a unidade para converter em: ")

while unidade_saida not in unidades :
    print("Unidade não reconhecida, digite a unidade de conversão correta: ")
    unidade_saida = input()
    
while unidades.index(unidade_entrada) < unidades.index(unidade_saida):
    nova_unidade = unidades[unidades.index(unidade_entrada) + 1]
    quantidade = converter_medidas(quantidade, unidade_entrada, nova_unidade)
    unidade_origem = nova_unidade

print("O resultado da conversão é:", quantidade, unidade_entrada)
