from BaseDeCalculos import converterStringParaFloat, BitToByte, ByteToKilobyte, KilobyteToMegabyte, MegabyteToGigabyte, GigabyteToTerabyte, TerabyteToPetabyte, PetabyteToTerabyte, TerabyteToGigabyte, GigabyteToMegabyte, MegabyteToKilobyte, KilobyteToByte, ByteToBit

print(' -Type 1 to convert bit to byte \n -Type 2 to convert Byte to Kilobyte \n -Type 3 to convert Kilobyte to Megabyte \n -Type 4 to convert Megabyte to Gigabyte \n -Type 5 to convert Gigabyte to Terabyte \n -Type 6 to convert Terabyte to Petabyte \n -Type 7 to convert Petabyte to Terabyte \n -Type 8 to convert Terabyte to Gigabyte \n -Type 9 to convert Gigabyte to Megabyte \n -Type 10 to convert Megabyte to Kilobyte \n -Type 11 to convert Kilobyte to Byte \n -Type 12 to convert Byte to Bit')
choicefunc = input()


if (choicefunc == '1'):
    print ('you chose the option 1')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = BitToByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif (choicefunc == '2'):
    print ('you chose the option 2')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = ByteToKilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif (choicefunc == '3'):
    print ('you chose the option 3')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KilobyteToMegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif (choicefunc == '4'):
    print ('you chose the option 4')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MegabyteToGigabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif (choicefunc == '5'):
    print ('you chose the option 5')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GigabyteToTerabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif (choicefunc == '6'):
    print ('you chose the option 6')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TerabyteToPetabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)


elif (choicefunc == '7'):
    print ('you chose the option 7')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = PetabyteToTerabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif (choicefunc == '8'):
    print ('you chose the option 8')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TerabyteToGigabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif (choicefunc == '9'):
    print ('you chose the option 9')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GigabyteToMegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif (choicefunc == '10'):
    print ('you chose the option 10')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MegabyteToKilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif (choicefunc == '11'):
    print ('you chose the option 11')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KilobyteToByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif (choicefunc == '12'):
    print ('you chose the option 12')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = ByteToBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

else :
    print ('Invalid')