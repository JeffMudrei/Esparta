def solution(lista):
    '''Função Solution
    retorna o elemento sem par e seu índice em uma lista de N elementos (sendo N ímpar)'''
    #Se o número de elementos da lista não for ímpar retorna a mensagem
    if len(lista) % 2 == 0:
        return ('Number of elements is Odd')
    else:
        pass

    #Percorre com 'i' os itens da lista, conta quantas vezes cada elemento está na lista
    for i in lista:
        a = lista.count(i)
        #caso o elemento seja único retorna a posição e o elemento
        if a == 1:
            return print(f"Index:[{lista.index(i)}]\nElement:{i}")