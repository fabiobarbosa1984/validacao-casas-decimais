import random
from decimal import *

def encontrar_resto(pu,valor_disponivel,limite,precisao):
    """
        Calcula se para um determinado valor, todos os valores disponíveis entre "valor_disponível" e "limite" podem acarretar na geração de resto, dada uma determinada precisão
        A partir do valor_disponivel, o código irá percorrer todos os valores disponíveis até o valor limite, incrementando-o de um em um centavo. 
        Args:
            pu (Decimal): Preço unitário a ser validado. 
            valor_disponivel: Valor inicialmente disponível para investimento pelo investidor
            limite: valor máximo a ser investido. 
            precisao: precisão desejada, no formato '0.01', por exemplo, para 2 casas decimais

    """    
    while valor_disponivel <=limite:    
        quantidade_piso = Decimal(valor_disponivel/pu).quantize(precisao, rounding=ROUND_FLOOR)
        quantidade_teto = Decimal(valor_disponivel/pu).quantize(precisao, rounding=ROUND_CEILING)

        if(Decimal(quantidade_teto*pu).quantize(Decimal('0.01'),rounding=ROUND_FLOOR) > valor_disponivel):
            quantidade = quantidade_piso
        else:
            quantidade = quantidade_teto

        valor_investido = Decimal(quantidade*pu).quantize(Decimal('0.01'),rounding=ROUND_DOWN)
        resto = Decimal(valor_disponivel - valor_investido).quantize(Decimal('0.01'),rounding=ROUND_DOWN)
    
        valor_disponivel += Decimal('0.01')

        if (resto!=0):
            print(f'Falha encontrada para a precisão {precisao}')
            print(f'Quantidade: {quantidade}')
            print(f'Valor disponível: {valor_disponivel}')    
            print(f'Resto: {resto}\n\n')
            
            return
    print(f'Precisão {precisao} não apresentou resto para o pu {pu}.')
    
print('teste #1 - Verificação de existência de resto para investimentos entre 1.00 e 5000 para 2 casas decimais')
encontrar_resto(Decimal('15394.91'),Decimal('1.00'),Decimal('5000.00'),Decimal('0.01'))

print('\n#teste #2 - Verificação de existência de resto para investimentos entre 1.00 e 5000 para 4 casas decimais')
encontrar_resto(Decimal('15394.91'),Decimal('1.00'),Decimal('5000.00'),Decimal('0.0001'))

print('\n#teste #3 - Verificação de existência de resto para investimentos entre 1.00 e 5000 para 6 casas decimais')
encontrar_resto(Decimal('15394.91'),Decimal('1.00'),Decimal('5000.00'),Decimal('0.000001'))

print('\n#teste #4 - Verificação de existência de resto para investimentos entre 1.00 e 5000 para 8 casas decimais')
encontrar_resto(Decimal('15394.91'),Decimal('1.00'),Decimal('5000.00'),Decimal('0.00000001'))

print('\n#teste #5 - Verificação de existência de resto para investimentos entre 1.00 e 5000 para 8 casas decimais com 25 PUs aleatórios')
for i in range(0,25):
    pu_r = random.randrange(3000,3000000)/100
    encontrar_resto(Decimal(pu_r).quantize(Decimal('0.01'), rounding=ROUND_FLOOR),Decimal('1.00'),Decimal('5000.00'),Decimal('0.00000001'))

print('\n#teste #6 - Verificação de existência de resto para investimentos entre 1.00 e 2m para 8 casas decimais para um PU de 3 casas inteiras (LTN, NTN-F, NTN-B1)')
encontrar_resto(Decimal('457.33').quantize(Decimal('0.01'), rounding=ROUND_FLOOR),Decimal('1.00'),Decimal('2000000.00'),Decimal('0.00000001'))

print('\n#teste #7 - Verificação de existência de resto para investimentos entre 1.00 e 2m para 8 casas decimais para um PU de 4 casas inteiras (NTN-B)')
encontrar_resto(Decimal('2832.69').quantize(Decimal('0.01'), rounding=ROUND_FLOOR),Decimal('1.00'),Decimal('2000000.00'),Decimal('0.00000001'))

print('\n#teste #8 - Verificação de existência de resto para investimentos entre 1.00 e 2m para 8 casas decimais para um PU de 5 casas inteiras (LFT)')
encontrar_resto(Decimal('15832.69').quantize(Decimal('0.01'), rounding=ROUND_FLOOR),Decimal('1.00'),Decimal('2000000.00'),Decimal('0.00000001'))

print('\n#teste #9 - Verificação de existência de resto para investimentos entre 1.00 e 2m para 8 casas decimais para um PU de 5 casas inteiras - caso extremo (99.9999,99) (LFT)')
encontrar_resto(Decimal('99999.99').quantize(Decimal('0.01'), rounding=ROUND_FLOOR),Decimal('1.00'),Decimal('2000000.00'),Decimal('0.00000001'))

print('concluído')