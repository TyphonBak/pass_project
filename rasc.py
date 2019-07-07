from itertools import combinations
# Botão Chutar
    #Registra Chute
    #Retorna Jogo Atualizado + status

'''
    3 campos
    4 pontos
'''
campo1 = [0, 1, 2, 3, 4]
campo2 = [0, 1, 2, 3, 4]
campo3 = [0, 1, 2, 3, 4]

possibilidade = []

teste = [[x, y, z] for x in campo1 for y in campo2 for z in campo3 if x+y+z==4]

resultado = { 'otimo': 0, 'bom': 0, 'ruim': 0 }

print(''.join([str(item) for item in resultado.values()]))