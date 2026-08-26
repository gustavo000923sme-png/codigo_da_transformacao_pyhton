# 🥖 Sistema de Vendas CLI - Padaria (Módulo 01)

Sistema de vendas e gerenciamento de estoque para padaria desenvolvido em Python via **CLI (Command Line Interface)**, funcionando diretamente no terminal.

---

## 📄 Visão Geral e Histórias de Usuário

O objetivo principal deste projeto é atender às necessidades dos diversos atores envolvidos na gestão e uso de um sistema de vendas para padaria:

- **PD (Dono do Negócio):** Quer criar um sistema de vendas para a padaria para que os clientes possam comprar produtos online e para ter controle sobre as vendas e o estoque disponível.
- **QA (Cliente):** Quer facilidade para comprar produtos online, economizando tempo e evitando filas.
- **Tech / Dev (Programador):** Quer implementar o sistema utilizando boas práticas de desenvolvimento (cadastro, gerenciamento de estoque, busca, cancelamento e processamento de pedidos).
- **UX (Designer de Experiência):** Busca garantir uma navegação simples e intuitiva (adaptada para terminal/CLI).
- **IA (Análise de Dados):** Busca coletar dados de vendas para gerar insights sobre padrões de compra e apoiar estratégias de marketing.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Interface:** CLI (Terminal / Linha de Comando)
- **Estruturas de Controle:** Loops (`while`), condicionais (`if`, `elif`, `else`), manipulação de strings e conversão de tipos.

---

## ⚙️ Funcionalidades do Sistema

1. **Cadastrar Produto:** Permite cadastrar até 5 produtos com Nome, Descrição, Validade, Estoque e Preço.
2. **Listar Produtos:** Exibe todos os produtos atualmente cadastrados no sistema.
3. **Excluir Produto:** Libera uma vaga de cadastro ao remover um produto pesquisado pelo nome.
4. **Pesquisar Produto:** Localiza um produto no estoque pelo nome e exibe suas informações detalhadas.
5. **Realizar Venda:** Módulo para registro e processamento de pedidos.
6. **Suporte ao Cliente:** Canal para atendimento e dúvidas do cliente.
7. **Cancelar Venda:** Permite estornar ou cancelar uma transação.
8. **Sair:** Encerra a execução do programa.

---

## 💻 Código Fonte (`main.py`)

```python
# ==============================================================================
# PROJETO PADARIA - SISTEMA DE VENDAS CLI
# ==============================================================================

# Inicialização de variáveis dos produtos (Slots de 1 a 5)
p1_nome = 'Pão Francês'
p1_descricao = 'Pão Francês feito na hora!'
p1_validade = '04-07-2026'
p1_estoque = 50
p1_preco = 1.50

p2_nome = 'Croissant'
p2_descricao = 'Croissant de queijo'
p2_validade = '04-07-2026'
p2_estoque = 30
p2_preco = 8.00

p3_nome = 'Sonho'
p3_descricao = 'Sonho pequeno, Recheado - creme'
p3_validade = '04-07-2026'
p3_estoque = 20
p3_preco = 6.00

p4_nome = 'Café'
p4_descricao = 'Café expresso. 300ml. Feito na Hora!'
p4_validade = '08-07-2026'
p4_estoque = 40
p4_preco = 10.00

p5_nome = 'Suco de laranja'
p5_descricao = 'Suco natural. 300ml.' 
p5_validade = '08-07-2026'
p5_estoque = 40
p5_preco = 10.00


while True:
    print('\n===================================================')
    print('   Bem-vindo ao Sistema de Vendas - Padaria CLI    ')
    print('===================================================')
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

    # --------------------------------------------------------------------------
    # 1. CADASTRAR PRODUTO
    # --------------------------------------------------------------------------
    if opcao == '1':
        print('\n[Opção 1] Cadastrando Produtos...')
        
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

        elif p4_nome == '':
            p4_nome = input('Digite o nome do produto: ')
            p4_descricao = input('Digite a descrição do produto: ')
            p4_validade = input('Digite a validade do produto: ')
            p4_estoque = int(input('Digite a quantidade em estoque: '))
            p4_preco = float(input('Digite o preço do produto: '))
            print(f'\n✨ Produto ({p4_nome}) cadastrado na vaga 4!') 

        elif p5_nome == '':
            p5_nome = input('Digite o nome do produto: ')
            p5_descricao = input('Digite a descrição do produto: ')
            p5_validade = input('Digite a validade do produto: ')
            p5_estoque = int(input('Digite a quantidade em estoque: '))
            p5_preco = float(input('Digite o preço do produto: '))
            print(f'\n✨ Produto ({p5_nome}) cadastrado na vaga 5!') 

        else:
            print('\n⚠️ Limite de vagas de produtos atingido (máximo 5). Exclua um produto para cadastrar outro.')

    # --------------------------------------------------------------------------
    # 2. LISTAR PRODUTOS
    # --------------------------------------------------------------------------
    elif opcao == '2':
        print('\n[Opção 2] Listando Produtos...')
        
        if p1_nome == '' and p2_nome == '' and p3_nome == '' and p4_nome == '' and p5_nome == '':
            print('Nenhum produto cadastrado no sistema ainda.')

        else:
            if p1_nome != '':
                print(f'Nome: {p1_nome} | Preço: R$ {float(p1_preco):.2f} | Estoque: {p1_estoque} unid.')
                print(f'Validade: {p1_validade} | Descrição: {p1_descricao}')
                print('-' * 40)

            if p2_nome != '':
                print(f'Nome: {p2_nome} | Preço: R$ {float(p2_preco):.2f} | Estoque: {p2_estoque} unid.')
                print(f'Validade: {p2_validade} | Descrição: {p2_descricao}')
                print('-' * 40)

            if p3_nome != '':
                print(f'Nome: {p3_nome} | Preço: R$ {float(p3_preco):.2f} | Estoque: {p3_estoque} unid.')
                print(f'Validade: {p3_validade} | Descrição: {p3_descricao}')
                print('-' * 40)    

            if p4_nome != '':
                print(f'Nome: {p4_nome} | Preço: R$ {float(p4_preco):.2f} | Estoque: {p4_estoque} unid.')
                print(f'Validade: {p4_validade} | Descrição: {p4_descricao}')
                print('-' * 40)       

            if p5_nome != '':
                print(f'Nome: {p5_nome} | Preço: R$ {float(p5_preco):.2f} | Estoque: {p5_estoque} unid.')
                print(f'Validade: {p5_validade} | Descrição: {p5_descricao}')
                print('-' * 40)       

    # --------------------------------------------------------------------------
    # 3. EXCLUIR PRODUTO
    # --------------------------------------------------------------------------
    elif opcao == '3':
        print('\n[Opção 3] Excluindo Produto...')
        
        if p1_nome == "" and p2_nome == "" and p3_nome == "" and p4_nome == "" and p5_nome == "":
            print('Não há produtos para excluir.')
        else:
            produto_excluir = input('Digite o nome do produto que deseja excluir: ')
            
            if produto_excluir.lower() == p1_nome.lower() and p1_nome != "":
                p1_nome = ''
                print('✔ Produto da vaga 1 excluído com sucesso!')
            elif produto_excluir.lower() == p2_nome.lower() and p2_nome != "":
                p2_nome = ''
                print('✔ Produto da vaga 2 excluído com sucesso!')
            elif produto_excluir.lower() == p3_nome.lower() and p3_nome != "":
                p3_nome = ''
                print('✔ Produto da vaga 3 excluído com sucesso!')
            elif produto_excluir.lower() == p4_nome.lower() and p4_nome != "":
                p4_nome = ''
                print('✔ Produto da vaga 4 excluído com sucesso!')   
            elif produto_excluir.lower() == p5_nome.lower() and p5_nome != "":
                p5_nome = ''   
                print('✔ Produto da vaga 5 excluído com sucesso!')
            else:
                print('❌ Produto não encontrado.')

    # --------------------------------------------------------------------------
    # 4. PESQUISAR PRODUTO
    # --------------------------------------------------------------------------
    elif opcao == '4':
        print('\n[Opção 4] Pesquisando produto...')
        if p1_nome == "" and p2_nome == "" and p3_nome == "" and p4_nome == "" and p5_nome == "":
            print('O estoque está completamente vazio.')
        else:
            procurar_produto = input('Digite o nome do produto para procurar no estoque: ')
            
            if procurar_produto.lower() == p1_nome.lower() and p1_nome != "":
                print(f'\n🔍 Produto encontrado na Vaga 1!')
                print(f'Nome: {p1_nome} | Preço: R$ {float(p1_preco):.2f} | Estoque: {p1_estoque} unidades.')
            elif procurar_produto.lower() == p2_nome.lower() and p2_nome != "":
                print(f'\n🔍 Produto encontrado na Vaga 2!')
                print(f'Nome: {p2_nome} | Preço: R$ {float(p2_preco):.2f} | Estoque: {p2_estoque} unidades.')
            elif procurar_produto.lower() == p3_nome.lower() and p3_nome != "":
                print(f'\n🔍 Produto encontrado na Vaga 3!')
                print(f'Nome: {p3_nome} | Preço: R$ {float(p3_preco):.2f} | Estoque: {p3_estoque} unidades.')
            elif procurar_produto.lower() == p4_nome.lower() and p4_nome != "":
                print(f'\n🔍 Produto encontrado na Vaga 4!')
                print(f'Nome: {p4_nome} | Preço: R$ {float(p4_preco):.2f} | Estoque: {p4_estoque} unidades.')
            elif procurar_produto.lower() == p5_nome.lower() and p5_nome != "":
                print(f'\n🔍 Produto encontrado na Vaga 5!')
                print(f'Nome: {p5_nome} | Preço: R$ {float(p5_preco):.2f} | Estoque: {p5_estoque} unidades.')
            else:
                print('❌ Esse produto não foi encontrado no estoque.')

    # --------------------------------------------------------------------------
    # 5. REALIZAR VENDA
    # --------------------------------------------------------------------------
    elif opcao == '5':
        print('\n[Opção 5] Realizando venda...')
        # Espaço reservado para futura implementação das regras de negócio de vendas.

    # --------------------------------------------------------------------------
    # 6. SUPORTE AO CLIENTE
    # --------------------------------------------------------------------------
    elif opcao == '6':
        print('\n[Opção 6] Suporte ao cliente')
        print('Para suporte, entre em contato pelo e-mail: suporte@padaria.com')

    # --------------------------------------------------------------------------
    # 7. CANCELAR VENDA
    # --------------------------------------------------------------------------
    elif opcao == '7':
        print('\n[Opção 7] Cancelando venda...')
        # Espaço reservado para estorno/cancelamento de vendas.

    # --------------------------------------------------------------------------
    # 0. SAIR
    # --------------------------------------------------------------------------
    elif opcao == '0':
        print('\nEncerrando o programa. Obrigado por utilizar o sistema da Padaria!')
        break

    else:
        print('\n❌ Opção inválida! Tente novamente.')
