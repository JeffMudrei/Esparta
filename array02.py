def solution(lista):
    '''Função Solution
    retorna o elemento sem par e seu índice em uma lista de N elementos (sendo N ímpar)'''
    # lista repetidos armazena a frequencia dos elementos
    repetidos = [None] * len(lista)
    check = -1
    if len(lista) % 2 == 0:
        return ('Número de elementos é par!')

    else:
        pass
    for i in range(0, len(
            lista)):  # percorre  a lista com i, só avança para o proximo index depois de concluir o for aninhado
        cont = 1
        for j in range(i + 1, len(lista)):  # percorre a lista com j, começando uma posição a frente de i
            if (lista[i] == lista[j]):  # quando encontra dois elementos iguais incrementa o contador
                cont += 1
                # Para não contar o mesmo elemento mais de uma vez
                repetidos[j] = check

        if (repetidos[i] != check):
            repetidos[i] = cont

    for i in range(0, len(repetidos)):  # percorre a lista para encontrar o elemento que aparece somente uma vez
        if (repetidos[i] != check):
            if repetidos[i] == 1:
                return lista[i]


lista = [1, 1, 2, 2, 2, 3, 3, 3, 16]

solution(lista)