# menu.py
from funcoes import salvar, mostrar, buscar, excluir, dic, verificar_arquivo, inicializar_contador_id

verificar_arquivo()
inicializar_contador_id()

def Opcao(opcao):
    if opcao == 1:
        usuario = input('Digite um novo usuário: ')
        dic.append(usuario)
        print(f'Usuário "{usuario}" criado com sucesso!')
        return True
    elif opcao == 2:
        try:
            id_para_alterar = int(input('Digite o ID para a alteração: '))
            buscar(id_para_alterar)
        except ValueError:
            print("Por favor, digite um ID válido (número inteiro).")
        return True
    elif opcao == 3:
        try:
            id_para_excluir = int(input('Digite o ID que gostaria de excluir: '))
            excluir(id_para_excluir)
            print('Usuário excluído!')
        except ValueError:
            print("Por favor, digite um ID válido (número inteiro).")
        return True
    elif opcao == 4:
        print(dic)
        return True
    elif opcao == 5:
        mostrar()
        return True
    elif opcao == 6:
        salvar()
        return True
    elif opcao == 7:
        print('Tem certeza que deseja sair?')
        sim = input("Digite [s] pra sair ou [n] para ficar: ")
        if sim.lower() == 's':
            print('Saindo.')
            return False
        else:
            return True
    else:
        print("Opção inválida!")
        return True

while True:
    print('\n---- Escolha uma opção ----')
    print('1 - Criar novo usuário')
    print('2 - Atualizar usuário')
    print('3 - Excluir usuário')
    print('4 - Mostrar usuários (na memória)')
    print('5 - Mostrar salvos (do arquivo)')
    print('6 - Salvar')
    print('7 - Sair')

    try:
        opcao = int(input('Digite uma opção: '))
        continuar = Opcao(opcao)
        if not continuar:
            break
    except ValueError:
        print("Por favor, digite um número inteiro.")