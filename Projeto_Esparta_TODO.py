def titulo():
    print('\033[34m_'*30,'SUAS TAREFAS','_'*30)

def rodape():
    print('\033[34m_'*74)


def opcao(op):
    op = str(input('''
         \033[34mO QUE DESEJA FAZER?      
         [ 1 ] - CADASTRAR NOVA TAREFA [ 2 ] - MARCAR TAREFA COMO CONCLUÍDA  [ 3 ] - CONSULTAR CONCLUIDA/EXCLUÍDAS
         [ 4 ] - EXCLUIR TAREFA        [ 5 ] - RECUPERAR  EXCLUÍDA/CONCLUÍDA [ 6 ] - SAIR
          OPÇÃO >>> '''))

    return op

def concluindo(tarefas, concluidas):
    '''Função concluindo:
    Implementa as tarefas concluídas em uma lista separada e marca na lista principal como 'concluída' '''
    titulo()
    mostra_tarefas(tarefas)
    op = int(input('\033[34mInforme qual o numero da tarefa a excuir: '))
    concluida = str(tarefas[op-1])
    tarefas[op-1] = (f'{concluida} --> Concluída')
    concluidas.append(concluida)
    rodape()
    return (tarefas, concluidas)

def excuir(fazer, excluidas):
    '''Funçãoi excluir:
    Exclui as tarefas selecionadas e guarda em uma lista separada'''
    titulo()
    mostra_tarefas(fazer)
    rodape()
    op = int(input('\033[34mInforme qual o numero da tarefa a excuir: '))
    confirma = 0
    while confirma != 'n' or confirma != 's':
        confirma = str(input("""
                Confirma a exclusão da tarefa?
                [ S ] - SIM
                [ N } - NAO
                Opção >>> """)).lower()
        if confirma == 's':
            excluidas.append(fazer[op - 1])
            del(fazer[op-1])
            break
        if confirma == 'n':
            break
        else:
            print("!!!!!!!!!!!!Opção inválida!!!!!!!!!!!!")

def tarefas():
    a = input("Digite a tarefa: ")
    return a

def mostra_tarefas(lista):
    '''Percorre a lista mostrando o indice 'index(i)' e o elemento 'i' '''
    for i in lista:
        print((lista.index(i)+1),i)

def restaura(fazer, restaurar):
    '''Restaura um ítem para a lista de tarefas não concluídas'''
    mostra_tarefas(restaurar)
    volta = int(input("Informe o número da tarefa: "))
    recupera = restaurar[volta - 1]
    del (restaurar[volta - 1])
    fazer.append(recupera)


def recuperar(fazer, concluidas, excluidas):
    '''Faz interação com o usuário fornecendo opções para recuperar uma tarefa'''
    op = 0
    while op != 1 or op !=2 or op !=3:
        op = str(input("""Desja recuperar uma tarefa:
                        [ 1 ] - CONCLUÍDA
                        [ 2 ] - EXCLUIDA
                        [ 3 ] - VOLTAR
                                Opção >>> """))
        if op == '1':
            return restaura(fazer, concluidas)
            break
        elif op == '2':
            return restaura(fazer, excluidas)
            break
        elif op == '3':
            break
        else:
            print("!!!!!!OPÇÃO INVÁLIDA!!!!!!")

def consultar(concluidas, excluidas):
    print('\033[34m_'*30,'CONCLUIDAS','_'*30)
    mostra_tarefas(concluidas)
    rodape()

    print('\033[34m_'*30,'EXCLUIDAS','_'*30)
    mostra_tarefas(excluidas)
    rodape()

    op = 0
    while op != '1':
        op = str(input("Para voltar pressione '1' >>> "))
        if op == '1':
            break
        else:
            print('!!!!!!OPÇÃO INVÁLIDA!!!!!!')

op = 0
fazer = ['Enviar e-mail para Mark', 'Escrever uma canção', 'Tomar água']
concluidas = []
excluidas = []
while op != 4:
    titulo()
    mostra_tarefas(fazer)
    rodape()
    op = opcao(op)
    if op == '1':
        fazer.append(tarefas())
    elif op == '2':
        concluindo(fazer, concluidas)
    elif op == '4':
        excuir(fazer, excluidas)
    elif op == '5':
        recuperar(fazer, concluidas, excluidas)
    elif op == '3':
        consultar(concluidas, excluidas)

    elif op == '6':
        break

    else:
        print('!!!!!!!!Opção Inválida!!!!!!!!')