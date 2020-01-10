def solution(n,m):
    '''Função solution
    dados dois numeros N e M checa o numero de vezes que para em locais diferentes Ex:
    N = 10 e M = 4 vai parar em 0, 4, 8, 2, 6. Nesse exemplo vai retornar 5'''
    inicio = 0
    resto = 0
    cont = 1
    while ((inicio + m) % n != 0):
        resto = (inicio + m) % n
        inicio = resto
        cont += 1
    return (cont)
