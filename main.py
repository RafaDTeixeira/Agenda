from Agenda import Contato


def menu():
    return input('1. Novo \n2. Editar\n3. Excluir\n4. Consultar\n5. Listar\n6. Encerrar\nOpção: ')


def faixa(texto):
    print('-=-' * 50)
    print(texto.upper().center(50))
    print('-=-' * 50)


def cadastrar():
    print('Entre com os dados da Pessoa: ')
    celular = input('celular: ')
    if buscar(celular) == -1:
        nome = input('nome: ')
        a = Contato(nome, celular)
        agenda.append(a)
        print('Cadastro efetuado!!')
    else:
        print('Celular já registrado!!')


def buscar(celular):
    for i, a in enumerate(agenda):
        if a.celular == celular:
            return i
    return -1

def consultar():
    celular = input('Informe o numero do celular da pessoa que deseja consultar: ')
    pos = buscar(celular)
    if pos == -1:
        print('Celular não cadastrado!!')
    else:
        print(agenda[pos])


def editar():
    celular = input('Informe o numero do celular da pessoa que deseja consultar: ')
    pos = buscar(celular)
    if pos == -1:
        print('Celular não cadastrado!!')
    else:
        novoCelular = input('Insira o novo numero de celular: ')
        novoNome = input('Insira o novo nome do contato: ')
        agenda[pos].celular = novoCelular
        agenda[pos].nome = novoNome
        print('Dados alterado com sucesso!!')


def excluir():
    celular = input('Informe o numero do celular que deseja excluir: ')
    pos = buscar(celular)
    if pos == -1:
        print('Número de celular inexistente ')
    else:
        print(agenda[pos])
        resp = input('Deseja realmente excluir? [S/N]: ').upper()[0]
        if resp == 'S':
            del agenda[pos]
            print('Número excluido!!')


def listar():
    if len(agenda) == 0:
        print('Agenda vazia!!')
    else:
        for a in agenda:
            print(a)


agenda = []
while True:
    faixa('menu de opções')
    op = menu()
    if op == '1':
        faixa('cadastro de contato')
        cadastrar()
    elif op == '2':
        editar()
    elif op == '3':
        excluir()
    elif op == '4':
        consultar()
    elif op == '5':
        faixa('lista de contatos')
        listar()
    elif op == '6':
        break
