'''
Isso é um bloco de comentário

Projeto Padaria:


>PD (Como dono do negócio: Eu quero criar um sistema de vendas para a padaria,
para que os clientes possam comprar nossos produtos online e para que eu consiga contolar
as vendas e os produtos disponíveis.)

>QA (Como cliente: Eu quero poder ter facilidade para comprar os produtos da padaria online,
para que eu possa economizar tempo e evitar filas.)

>Tech (Como programador: Eu quero criar um sistema de vendas para que eu possa desenvolver
minhas habilidades de programação e criar um projeto útil para a padaria.)

>Dev (Como programador: quero um sistema de vendas para a padaria para que eu possa
implementar as funcionalidades necessárias, como cadastro de produtos, gerenciamento de estoque
e processamento de pedidos, utilizando as melhores práticas de desenvolvimento de software.)

>Uk (Como designer de experiêcia do usuário: Eu quero um sistema de vendas para a padaria
para que eu possa criar uma interface intuitiva e agradável para os clientes,
facilitando a navegação e a realização de compras online.)

>IA (Como análise de dados: Eu quero um sistema de vendas para a padaria para que eu possa coletar
e analisar os dados de vendas, identificar padrões de compra e fornecer insights para melhorar
as estratégias de marketing e vendas da padaria.)

>>Criar um aplicativo, sistema CLT - Command Line Interface, ou seja, um sistema que funcione no
terminal, sem interface gráfica.
>>Completar e Implementar o app

'''

# Inicializando as variáveis dos 3 produtos (vagas vazias)
p1_nome = p1_descricao = p1_validade = ''
p1_estoque = 0
p1_preco = 0.0

p2_nome = p2_descricao = p2_validade = ''
p2_estoque = 0
p2_preco = 0.0

p3_nome = p3_descricao = p3_validade = ''
p3_estoque = 0
p3_preco = 0.0

while True:
    print('\n---------------------------------------------------')
    print('Bem vindo ao sistema de vendas - Padaria\n')
    print('1. Cadastrar Produto')
    print('2. Listar Produtos')
    print('3. Excluir Produto')
    print('4. Pesquisar Produto')
    print('5. Realizar Venda')
    print('6. Suporte ao cliente')
    print('7. Cancelar venda')
    print('0. Sair')
    print('---------------------------------------------------\n')

    opcao = input('Digite a opção desejada: ')

# Inicializando as variáveis dos 3 produtos (vagas vazias)
p1_nome = p1_descricao = p1_validade = ''
p1_estoque = 0
p1_preco = 0.0

p2_nome = p2_descricao = p2_validade = ''
p2_estoque = 0
p2_preco = 0.0

p3_nome = p3_descricao = p3_validade = ''
p3_estoque = 0
p3_preco = 0.0

while True:
    print('\n---------------------------------------------------')
    print('Bem vindo ao sistema de vendas - Padaria\n')
    print('1. Cadastrar Produto')
    print('2. Listar Produtos')
    print('3. Excluir Produto')
    print('4. Pesquisar Produto')
    print('5. Realizar Venda')
    print('6. Suporte ao cliente')
    print('7. Cancelar venda')
    print('0. Sair')
    print('---------------------------------------------------\n')

    opcao = input('Digite a opção desejada: ')

    # 1. CADASTRAR PRODUTO
    if opcao == '1':
        print('\nOpção 1 selecionada: Cadastrando Produtos...')
        
        if p1_nome == '':
            p1_nome = input('Digite o nome do produto: ')
            p1_descricao = input('Digite a descrição do produto: ')
            p1_validade = input('Digite a validade do produto: ')
            p1_estoque = int(input('Digite a quantidade em estoque: '))
            p1_preco = float(input('Digite o preço do produto: '))
            print(f'\n✨ Produto ({p1_nome}) cadastrado na vaga 1!')

        elif p2_nome == '':
            p2_nome = input('Digite o nome do produto: ')
            p2_descricao = input('Digite a descrição do produto: ')
            p2_validade = input('Digite a validade do produto: ')
            p2_estoque = int(input('Digite a quantidade em estoque: '))
            p2_preco = float(input('Digite o preço do produto: '))
            print(f'\n✨ Produto ({p2_nome}) cadastrado na vaga 2!')

        elif p3_nome == '':
            p3_nome = input('Digite o nome do produto: ')
            p3_descricao = input('Digite a descrição do produto: ')
            p3_validade = input('Digite a validade do produto: ')
            p3_estoque = int(input('Digite a quantidade em estoque: '))
            p3_preco = float(input('Digite o preço do produto: '))
            print(f'\n✨ Produto ({p3_nome}) cadastrado na vaga 3!')
        else:
            print('\n❌ Todas as vagas de produtos estão cheias!')

    # 2. LISTAR PRODUTOS
    elif opcao == '2':
        print('\nOpção 2 selecionada: Listando Produtos...')
        
        if p1_nome == '' and p2_nome == '' and p3_nome == '':
            print('Nenhum produto cadastrado no sistema ainda.')
        else:
            if p1_nome != '':
                print(f'Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.')
                print(f'Validade: {p1_validade} | Descrição: {p1_descricao}')
                print('-' * 30)

            if p2_nome != '':
                print(f'Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.')
                print(f'Validade: {p2_validade} | Descrição: {p2_descricao}')
                print('-' * 30)

            if p3_nome != '':
                print(f'Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.')
                print(f'Validade: {p3_validade} | Descrição: {p3_descricao}')
                print('-' * 30)      

    # 3. EXCLUIR PRODUTO - AQUI QUE EU MUDEI
    elif opcao == '3':
        print('\nOpção 3 selecionada: Excluindo Produto\n')
        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print('Não há produtos para excluir.')
        else:
            produto_excluir = input('Digite o nome do produto que deseja excluir: ')
            
            if produto_excluir.lower() == p1_nome.lower() and p1_nome != "":
                p1_nome = p1_descricao = p1_validade = ''  # Limpa tudo
                p1_estoque = 0
                p1_preco = 0.0
                print('✔ Produto da vaga 1 excluído com sucesso!')
            elif produto_excluir.lower() == p2_nome.lower() and p2_nome != "":
                p2_nome = p2_descricao = p2_validade = ''  # Limpa tudo
                p2_estoque = 0
                p2_preco = 0.0
                print('✔ Produto da vaga 2 excluído com sucesso!')
            elif produto_excluir.lower() == p3_nome.lower() and p3_nome != "":
                p3_nome = p3_descricao = p3_validade = ''  # Limpa tudo
                p3_estoque = 0
                p3_preco = 0.0
                print('✔ Produto da vaga 3 excluído com sucesso!')
            else:
                print('❌ Produto não encontrado.')

    # 4. PESQUISAR PRODUTO
    elif opcao == '4':
        print('\nOpção 4 selecionada: Pesquisando produto...')
        
        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print('O estoque está completamente vazio.')
        else:
            procurar_produto_no_estoque = input('Digite o nome do produto para procurar no estoque: ')
            
            if procurar_produto_no_estoque.lower() == p1_nome.lower() and p1_nome != "":
                print(f'\n🔍 Produto encontrado na Vaga 1!')
                print(f'Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unidades.')
            elif procurar_produto_no_estoque.lower() == p2_nome.lower() and p2_nome != "":
                print(f'\n🔍 Produto encontrado na Vaga 2!')
                print(f'Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unidades.')
            elif procurar_produto_no_estoque.lower() == p3_nome.lower() and p3_nome != "":
                print(f'\n🔍 Produto encontrado na Vaga 3!')
                print(f'Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unidades.')
            else:
                print('❌ Esse produto não foi encontrado no estoque.')

    # 5. REALIZAR VENDA
    elif opcao == '5':
        print('\nOpção 5 selecionada: Realizando venda...')
        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print('Não há produtos cadastrados para realizar vendas.')
        else:
            nome_venda = input('Digite o nome do produto que deseja comprar: ')
            
            if nome_venda.lower() == p1_nome.lower() and p1_nome != "":
                qtd_venda = int(input(f"Quantas unidades de {p1_nome} deseja vender? "))
                if qtd_venda <= p1_estoque:
                    p1_estoque -= qtd_venda
                    total_venda = qtd_venda * p1_preco
                    print(f'\n✔ Venda realizada! Total: R$ {total_venda:.2f}')
                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')
                else:
                    print(f'\n❌ Estoque insuficiente! Temos apenas {p1_estoque} unidades em estoque.')

            elif nome_venda.lower() == p2_nome.lower() and p2_nome != "":
                qtd_venda = int(input(f"Quantas unidades de {p2_nome} deseja vender? "))
                if qtd_venda <= p2_estoque:
                    p2_estoque -= qtd_venda
                    total_venda = qtd_venda * p2_preco
                    print(f'\n✔ Venda realizada! Total: R$ {total_venda:.2f}')
                    print(f'Estoque atual de {p2_nome}: {p2_estoque} unidades.')
                else:
                    print(f'\n❌ Estoque insuficiente! Temos apenas {p2_estoque} unidades em estoque.')
        
            elif nome_venda.lower() == p3_nome.lower() and p3_nome != "":
                qtd_venda = int(input(f"Quantas unidades de {p3_nome} deseja vender? "))
                if qtd_venda <= p3_estoque:
                    p3_estoque -= qtd_venda
                    total_venda = qtd_venda * p3_preco
                    print(f'\n✔ Venda realizada! Total: R$ {total_venda:.2f}')
                    print(f'Estoque atual de {p3_nome}: {p3_estoque} unidades.')
                else:
                    print(f'\n❌ Estoque insuficiente! Temos apenas {p3_estoque} unidades em estoque.')
            else:
                print(f'\n🔥 Produto {nome_venda} não encontrado no estoque!')

    # 6. SUPORTE AO CLIENTE
    elif opcao == '6':
        print('\nOpção 6 selecionada: Suporte ao cliente')
        print('1. Central de ajuda')
        print('2. Chat ao vivo com atendente')
        print('3. Envie formulário ou mensagens para a equipe de suporte')
        suporte_opcao = input('Digite a opção de suporte desejada: ')
        print('✔ Redirecionando para o canal de suporte solicitado...')

    # 7. CANCELAR VENDA
    elif opcao == '7':
        print('\nOpção 7 selecionada: Cancelando venda...')
        nome_cancelar = input('Digite o nome do produto cuja a venda será cancelada: ')
        
        if nome_cancelar.lower() == p1_nome.lower() and p1_nome != "":
            qtd_cancelar = int(input('Quantidade a ser devolvida ao estoque: '))
            p1_estoque += qtd_cancelar
            print(f'✔ Venda cancelada. {qtd_cancelar} unidades retornaram ao estoque do {p1_nome}.')
        elif nome_cancelar.lower() == p2_nome.lower() and p2_nome != "":
            qtd_cancelar = int(input('Quantidade a ser devolvida ao estoque: '))
            p2_estoque += qtd_cancelar
            print(f'✔ Venda cancelada. {qtd_cancelar} unidades retornaram ao estoque do {p2_nome}.')
        elif nome_cancelar.lower() == p3_nome.lower() and p3_nome != "":
            qtd_cancelar = int(input('Quantidade a ser devolvida ao estoque: '))
            p3_estoque += qtd_cancelar
            print(f'✔ Venda cancelada. {qtd_cancelar} unidades retornaram ao estoque do {p3_nome}.')
        else:
            print('❌ Produto não identificado para cancelamento.')

    # 0. SAIR
    elif opcao == '0':
        print('Saindo do sistema... Até logo!')
        break

    # OPÇÃO INVÁLIDA
    else:
        print('Opção inválida!')