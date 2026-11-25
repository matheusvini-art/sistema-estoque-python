
import json
from datetime import date, datetime

print('Seja bem-vindo ao seu estoque :)')
nome = input('Qual seu nome? ')

print(f'Seja bem-vindo, {nome}! Realize seu login ou cadastre-se.')

login = ''
ca_senha = ''
validacao = False

estoque = 0

while estoque != 3:
    print('\n1 - Fazer Login')
    print('2 - Cadastrar')
    print('3 - Sair')

    estoque = int(input('Digite a opção desejada: '))

    if estoque == 1:
        if login == '':
            print('Cadastro não encontrado. Realize seu cadastro!')
        else:
            usuario = input('Digite seu usuário: ')
            senha = input('Digite sua senha: ')

            if usuario == login and senha == ca_senha:
                validacao = True
                print('Login realizado com sucesso!')
                break
            else:
                print('Usuário ou senha incorretos!')

    elif estoque == 2:
        login = input('Cadastre um usuário: ')
        ca_senha = input('Cadastre uma senha: ')
        print('Cadastro realizado com sucesso!')

    elif estoque == 3:
        print('Você saiu do sistema!')

    else:
        print('Opção inválida!')


if validacao:

    print(f'\nBem-vindo ao estoque, {nome}!')

    # Carregar os produtos salvos no arquivo
    try:
        arquivo = open('estoque.json', 'r')
        galpao = json.load(arquivo)
        arquivo.close()

        print('Estoque carregado com sucesso!')

    except FileNotFoundError:
        galpao = []
        print('Novo estoque iniciado!')

    armazem = 0

    while armazem != 3:

        print('\n1 - Cadastrar um produto')
        print('2 - Verificar estoque')
        print('3 - Sair do sistema')

        armazem = int(input('Escolha uma opção: '))

        if armazem == 1:

            produto = input('Digite o nome do produto: ')
            marca = input('Digite a marca do produto: ')
            data = input('Digite a data de vencimento (dd/mm/aaaa): ')

            if produto == '' or marca == '' or data == '':
                print('Produto não foi cadastrado por falta de dados!')

            else:
                try:
                    vencimento = datetime.strptime(data, '%d/%m/%Y').date()

                    novo_produto = {
                        'nome': produto,
                        'marca': marca,
                        'data': data
                    }

                    galpao.append(novo_produto)

                    # Salvar os produtos no arquivo
                    arquivo = open('estoque.json', 'w')
                    json.dump(galpao, arquivo, indent=4, ensure_ascii=False)
                    arquivo.close()

                    print('Produto cadastrado e salvo com sucesso!')

                    hoje = date.today()
                    dias = (vencimento - hoje).days

                    if dias < 0:
                        print(f'ATENÇÃO! Produto vencido há {abs(dias)} dias!')

                    elif dias <= 7:
                        print(f'ATENÇÃO! Produto próximo do vencimento! Faltam {dias} dias.')

                    else:
                        print(f'Produto dentro do prazo! Faltam {dias} dias para vencer.')

                except ValueError:
                    print('Data inválida! Digite no formato dd/mm/aaaa.')

        elif armazem == 2:

            produto = input('Digite o nome do produto que deseja localizar: ')

            if not galpao:
                print('Não há produtos cadastrados!')

            else:
                encontrado = False

                for item in galpao:

                    if item['nome'].lower() == produto.lower():

                        print('\nProduto encontrado!')
                        print(f"Nome: {item['nome']}")
                        print(f"Marca: {item['marca']}")
                        print(f"Vencimento: {item['data']}")

                        vencimento = datetime.strptime(item['data'], '%d/%m/%Y').date()

                        hoje = date.today()
                        dias = (vencimento - hoje).days

                        if dias < 0:
                            print(f'Produto vencido há {abs(dias)} dias!')

                        elif dias <= 7:
                            print(f'Produto próximo do vencimento! Faltam {dias} dias.')

                        else:
                            print(f'Produto dentro do prazo! Faltam {dias} dias para vencer.')

                        encontrado = True

                if not encontrado:
                    print('Produto não encontrado no estoque!')

        elif armazem == 3:
            print('Saindo do sistema!')
            print('Você saiu do sistema com sucesso!')

        else:
            print('Opção inválida!')
