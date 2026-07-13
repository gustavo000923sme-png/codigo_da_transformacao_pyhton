import tkinter as tk
from tkinter import messagebox, ttk

# ==========================================================
# PALETA DE CORES DEFINIDA POR VOCÊ
# ==========================================================
COR_AE = "#004d6e"  # Azul Escuro
COR_AM = "#0081ab"  # Azul Médio
COR_AC = "#00b1cd"  # Azul Claro
COR_V  = "#a6c844"  # Verde
COR_R  = "#b83764"  # Rosa / Vermelho
COR_A  = "#edce01"  # Amarelo
COR_B  = "#4a3336"  # Bordô / Marrom Escuro

# ==========================================================
# SEU CÓDIGO ORIGINAL - VARIÁVEIS INTACTAS
# ==========================================================
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

# Variáveis de controle para o histórico de vendas
ultima_venda_produto = ""
ultima_venda_quantidade = 0
ultima_venda_valor = 0.0

# ==========================================================
# FUNÇÕES DE LÓGICA DO SISTEMA
# ==========================================================

def atualizar_lista_produtos():
    txt_lista.delete('1.0', tk.END)
    global p1_nome, p2_nome, p3_nome, p4_nome, p5_nome
    
    if p1_nome == '' and p2_nome == '' and p3_nome == '' and p4_nome == '' and p5_nome == '':
        txt_lista.insert(tk.END, 'Nenhum produto cadastrado no sistema ainda.')
        return

    produtos = [
        (p1_nome, p1_preco, p1_estoque, p1_validade, p1_descricao),
        (p2_nome, p2_preco, p2_estoque, p2_validade, p2_descricao),
        (p3_nome, p3_preco, p3_estoque, p3_validade, p3_descricao),
        (p4_nome, p4_preco, p4_estoque, p4_validade, p4_descricao),
        (p5_nome, p5_preco, p5_estoque, p5_validade, p5_descricao)
    ]
    
    for i, prod in enumerate(produtos, 1):
        if prod[0] != '':
            txt_lista.insert(tk.END, f'VAGA {i} - Nome: {prod[0]} | Preço: R$ {prod[1]:.2f} | Estoque: {prod[2]} unid.\n')
            txt_lista.insert(tk.END, f'Validade: {prod[3]} | Descrição: {prod[4]}\n')
            txt_lista.insert(tk.END, '-' * 65 + '\n')

def cadastrar_produto():
    global p1_nome, p1_descricao, p1_validade, p1_estoque, p1_preco
    global p2_nome, p2_descricao, p2_validade, p2_estoque, p2_preco
    global p3_nome, p3_descricao, p3_validade, p3_estoque, p3_preco
    global p4_nome, p4_descricao, p4_validade, p4_estoque, p4_preco
    global p5_nome, p5_descricao, p5_validade, p5_estoque, p5_preco

    nome = ent_cad_nome.get()
    desc = ent_cad_desc.get()
    val = ent_cad_val.get()
    
    try:
        est = int(ent_cad_est.get())
        prc = float(ent_cad_prc.get())
    except ValueError:
        messagebox.showerror("Erro", "Estoque deve ser inteiro e Preço deve ser número!")
        return

    if p1_nome == '':
        p1_nome, p1_descricao, p1_validade, p1_estoque, p1_preco = nome, desc, val, est, prc
        messagebox.showinfo("Sucesso", f"Produto ({p1_nome}) cadastrado na vaga 1!")
    elif p2_nome == '':
        p2_nome, p2_descricao, p2_validade, p2_estoque, p2_preco = nome, desc, val, est, prc
        messagebox.showinfo("Sucesso", f"Produto ({p2_nome}) cadastrado na vaga 2!")
    elif p3_nome == '':
        p3_nome, p3_descricao, p3_validade, p3_estoque, p3_preco = nome, desc, val, est, prc
        messagebox.showinfo("Sucesso", f"Produto ({p3_nome}) cadastrado na vaga 3!")
    elif p4_nome == '':
        p4_nome, p4_descricao, p4_validade, p4_estoque, p4_preco = nome, desc, val, est, prc
        messagebox.showinfo("Sucesso", f"Produto ({p4_nome}) cadastrado na vaga 4!")
    elif p5_nome == '':
        p5_nome, p5_descricao, p5_validade, p5_estoque, p5_preco = nome, desc, val, est, prc
        messagebox.showinfo("Sucesso", f"Produto ({p5_nome}) cadastrado na vaga 5!")
    else:
        messagebox.showwarning("Aviso", "Todas as vagas estão cheias! Exclua um produto primeiro.")
    
    atualizar_lista_produtos()

def excluir_produto():
    global p1_nome, p2_nome, p3_nome, p4_nome, p5_nome
    prod_excluir = ent_acao_nome.get().lower()
    
    if p1_nome == "" and p2_nome == "" and p3_nome == "" and p4_nome == "" and p5_nome == "":
        messagebox.showinfo("Informação", "Não há produtos para excluir.")
        return

    if prod_excluir == p1_nome.lower() and p1_nome != "":
        p1_nome = ''
        messagebox.showinfo("Sucesso", "Produto da vaga 1 excluído com sucesso!")
    elif prod_excluir == p2_nome.lower() and p2_nome != "":
        p2_nome = ''
        messagebox.showinfo("Sucesso", "Produto da vaga 2 excluído com sucesso!")
    elif prod_excluir == p3_nome.lower() and p3_nome != "":
        p3_nome = ''
        messagebox.showinfo("Sucesso", "Produto da vaga 3 excluído com sucesso!")
    elif prod_excluir == p4_nome.lower() and p4_nome != "":
        p4_nome = ''
        messagebox.showinfo("Sucesso", "Produto da vaga 4 excluído com sucesso!")
    elif prod_excluir == p5_nome.lower() and p5_nome != "":
        p5_nome = ''
        messagebox.showinfo("Sucesso", "Produto da vaga 5 excluído com sucesso!")
    else:
        messagebox.showerror("Erro", "Produto não encontrado.")
    
    atualizar_lista_produtos()

def pesquisar_produto():
    prod_pesq = ent_acao_nome.get().lower()
    
    if prod_pesq == p1_nome.lower() and p1_nome != "":
        messagebox.showinfo("🔍 Encontrado", f"Vaga 1!\nNome: {p1_nome}\nPreço: R$ {p1_preco:.2f}\nEstoque: {p1_estoque} unid.")
    elif prod_pesq == p2_nome.lower() and p2_nome != "":
        messagebox.showinfo("🔍 Encontrado", f"Vaga 2!\nNome: {p2_nome}\nPreço: R$ {p2_preco:.2f}\nEstoque: {p2_estoque} unid.")
    elif prod_pesq == p3_nome.lower() and p3_nome != "":
        messagebox.showinfo("🔍 Encontrado", f"Vaga 3!\nNome: {p3_nome}\nPreço: R$ {p3_preco:.2f}\nEstoque: {p3_estoque} unid.")
    elif prod_pesq == p4_nome.lower() and p4_nome != "":
        messagebox.showinfo("🔍 Encontrado", f"Vaga 4!\nNome: {p4_nome}\nPreço: R$ {p4_preco:.2f}\nEstoque: {p4_estoque} unid.")
    elif prod_pesq == p5_nome.lower() and p5_nome != "":
        messagebox.showinfo("🔍 Encontrado", f"Vaga 5!\nNome: {p5_nome}\nPreço: R$ {p5_preco:.2f}\nEstoque: {p5_estoque} unid.")
    else:
        messagebox.showerror("Erro", "Esse produto não foi encontrado no estoque.")

def realizar_venda():
    global p1_estoque, p2_estoque, p3_estoque, p4_estoque, p5_estoque
    global ultima_venda_produto, ultima_venda_quantidade, ultima_venda_valor
    
    venda_nome = ent_acao_nome.get().lower()
    try:
        qtd = int(ent_acao_qtd.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite uma quantidade válida para a venda.")
        return

    sucesso_venda = False

    if venda_nome == p1_nome.lower() and p1_nome != "":
        if qtd <= p1_estoque:
            p1_estoque -= qtd
            ultima_venda_valor = qtd * p1_preco
            ultima_venda_produto = "vaga1"
            ultima_venda_quantidade = qtd
            sucesso_venda = True
        else: messagebox.showerror("Erro", f"Estoque insuficiente ({p1_estoque} disponíveis)")
    elif venda_nome == p2_nome.lower() and p2_nome != "":
        if qtd <= p2_estoque:
            p2_estoque -= qtd
            ultima_venda_valor = qtd * p2_preco
            ultima_venda_produto = "vaga2"
            ultima_venda_quantidade = qtd
            sucesso_venda = True
        else: messagebox.showerror("Erro", f"Estoque insuficiente ({p2_estoque} disponíveis)")
    elif venda_nome == p3_nome.lower() and p3_nome != "":
        if qtd <= p3_estoque:
            p3_estoque -= qtd
            ultima_venda_valor = qtd * p3_preco
            ultima_venda_produto = "vaga3"
            ultima_venda_quantidade = qtd
            sucesso_venda = True
        else: messagebox.showerror("Erro", f"Estoque insuficiente ({p3_estoque} disponíveis)")
    elif venda_nome == p4_nome.lower() and p4_nome != "":
        if qtd <= p4_estoque:
            p4_estoque -= qtd
            ultima_venda_valor = qtd * p4_preco
            ultima_venda_produto = "vaga4"
            ultima_venda_quantidade = qtd
            sucesso_venda = True
        else: messagebox.showerror("Erro", f"Estoque insuficiente ({p4_estoque} disponíveis)")
    elif venda_nome == p5_nome.lower() and p5_nome != "":
        if qtd <= p5_estoque:
            p5_estoque -= qtd
            ultima_venda_valor = qtd * p5_preco
            ultima_venda_produto = "vaga5"
            ultima_venda_quantidade = qtd
            sucesso_venda = True
        else: messagebox.showerror("Erro", f"Estoque insuficiente ({p5_estoque} disponíveis)")
    else:
        messagebox.showerror("Erro", "Produto indisponível ou não cadastrado.")

    if sucesso_venda:
        messagebox.showinfo("Sucesso", f"Venda efetuada! Total: R$ {ultima_venda_valor:.2f}")
        atualizar_lista_produtos()

def cancelar_venda():
    global p1_estoque, p2_estoque, p3_estoque, p4_estoque, p5_estoque
    global ultima_venda_produto, ultima_venda_quantidade, ultima_venda_valor
    
    if ultima_venda_produto == "":
        messagebox.showwarning("Aviso", "Nenhuma venda registrada para cancelamento.")
        return
        
    confirmar = messagebox.askyesno("Confirmar", f"Deseja estornar a última venda de R$ {ultima_venda_valor:.2f}?")
    if confirmar:
        if ultima_venda_produto == "vaga1": p1_estoque += ultima_venda_quantidade
        elif ultima_venda_produto == "vaga2": p2_estoque += ultima_venda_quantidade
        elif ultima_venda_produto == "vaga3": p3_estoque += ultima_venda_quantidade
        elif ultima_venda_produto == "vaga4": p4_estoque += ultima_venda_quantidade
        elif ultima_venda_produto == "vaga5": p5_estoque += ultima_venda_quantidade
        
        messagebox.showinfo("↩ Estornado", f"Venda cancelada! {ultima_venda_quantidade} unidades retornaram ao estoque.")
        ultima_venda_produto = ""
        ultima_venda_quantidade = 0
        ultima_venda_valor = 0.0
        atualizar_lista_produtos()

def mostrar_suporte():
    messagebox.showinfo("📞 SAC - Suporte", "Central de Ajuda da Padaria\n\nTelefone: 0800-777-PADARIA\nE-mail: suporte@padariaprojeto.com.br")

def mostrar_relatorio():
    total_itens = sum([p1_estoque if type(p1_estoque)==int else 0, p2_estoque, p3_estoque, p4_estoque, p5_estoque])
    messagebox.showinfo("📊 Relatório Técnico", f"📦 Total no Estoque Geral: {total_itens} unidades\n💰 Última Venda Movimentada: R$ {ultima_venda_valor:.2f}")

def mostrar_dev():
    messagebox.showinfo("💻 Desenvolvedor", "Sistema de Controle de Padaria v1.0\n\nOrganização: Memória Estática de Vagas.")

# ==========================================================
# INTERFACE GRÁFICA COM TKINTER E CORES PERSONALIZADAS
# ==========================================================
janela = tk.Tk()
janela.title("Sistema de Vendas - Padaria")
janela.geometry("780x650")
janela.configure(bg=COR_AE) # Fundo principal em Azul Escuro (AE)

# Configurando o estilo das Abas para combinar com a paleta
estilo = ttk.Style()
estilo.theme_use('default')
estilo.configure('TNotebook', background=COR_AE)
estilo.configure('TNotebook.Tab', background=COR_AM, foreground="white", padding=[15, 5])
estilo.map('TNotebook.Tab', background=[('selected', COR_AC)], foreground=[('selected', COR_B)])

abas = ttk.Notebook(janela)
aba_loja = tk.Frame(abas, bg=COR_AE)
aba_cadastro = tk.Frame(abas, bg=COR_AE)
abas.add(aba_loja, text="Loja e Operações")
abas.add(aba_cadastro, text="Cadastrar Produto")
abas.pack(expand=1, fill="both")

# --- LAYOUT DA ABA LOJA ---
lbl_titulo = tk.Label(aba_loja, text="Padaria - Painel de Controle", font=("Arial", 16, "bold"), bg=COR_AE, fg="white")
lbl_titulo.pack(pady=10)

# Área de listagem de produtos
frame_lista = tk.LabelFrame(aba_loja, text=" Estoque Atual (Produtos Cadastrados) ", font=("Arial", 10, "bold"), bg=COR_AE, fg=COR_AC)
frame_lista.pack(fill="both", expand=True, padx=15, pady=5)

txt_lista = tk.Text(frame_lista, height=12, width=85, font=("Courier", 10, "bold"), bg="white", fg=COR_B)
txt_lista.pack(padx=10, pady=10, fill="both", expand=True)

# Bloco de ações (Pesquisa, Venda, Exclusão)
frame_acoes = tk.LabelFrame(aba_loja, text=" Operações por Nome do Produto ", font=("Arial", 10, "bold"), bg=COR_AE, fg=COR_AC)
frame_acoes.pack(fill="x", padx=15, pady=10)

tk.Label(frame_acoes, text="Nome do Produto:", font=("Arial", 10), bg=COR_AE, fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="e")
ent_acao_nome = tk.Entry(frame_acoes, width=25, font=("Arial", 10), bg="white", fg=COR_B)
ent_acao_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_acoes, text="Qtd (para Venda):", font=("Arial", 10), bg=COR_AE, fg="white").grid(row=0, column=2, padx=10, pady=10, sticky="e")
ent_acao_qtd = tk.Entry(frame_acoes, width=8, font=("Arial", 10), bg="white", fg=COR_B)
ent_acao_qtd.insert(0, "1")
ent_acao_qtd.grid(row=0, column=3, padx=10, pady=10)

# Botões de Ação com as Cores Solicitadas
btn_pesq = tk.Button(frame_acoes, text="🔍 Pesquisar (4)", command=pesquisar_produto, bg=COR_AC, fg=COR_B, font=("Arial", 10, "bold"), relief="raised")
btn_pesq.grid(row=1, column=0, padx=10, pady=10, sticky="we")

btn_venda = tk.Button(frame_acoes, text="💵 Vender (5)", command=realizar_venda, bg=COR_V, fg=COR_B, font=("Arial", 10, "bold"), relief="raised")
btn_venda.grid(row=1, column=1, padx=10, pady=10, sticky="we")

btn_excluir = tk.Button(frame_acoes, text="❌ Excluir (3)", command=excluir_produto, bg=COR_R, fg="white", font=("Arial", 10, "bold"), relief="raised")
btn_excluir.grid(row=1, column=2, padx=10, pady=10, sticky="we")

btn_cancelar = tk.Button(frame_acoes, text="↩ Cancelar Venda (7)", command=cancelar_venda, bg=COR_A, fg=COR_B, font=("Arial", 10, "bold"), relief="raised")
btn_cancelar.grid(row=1, column=3, padx=10, pady=10, sticky="we")

# Botões de Utilidades e Sistema no rodapé
frame_sistema = tk.Frame(aba_loja, bg=COR_AE)
frame_sistema.pack(pady=15)

tk.Button(frame_sistema, text="📞 Suporte (6)", command=mostrar_suporte, width=12, bg=COR_AM, fg="white").pack(side="left", padx=10)
tk.Button(frame_sistema, text="📊 Relatório (8)", command=mostrar_relatorio, width=12, bg=COR_AM, fg="white").pack(side="left", padx=10)
tk.Button(frame_sistema, text="💻 Dev Info (9)", command=mostrar_dev, width=12, bg=COR_AM, fg="white").pack(side="left", padx=10)
tk.Button(frame_sistema, text="🚪 Sair (0)", command=janela.quit, bg=COR_B, fg="white", width=12, font=("Arial", 9, "bold")).pack(side="left", padx=10)

# --- LAYOUT DA ABA CADASTRO (Opção 1) ---
frame_cad = tk.LabelFrame(aba_cadastro, text=" Informações do Novo Produto ", font=("Arial", 11, "bold"), bg=COR_AE, fg=COR_AC)
frame_cad.pack(padx=30, pady=30, fill="both", expand=True)

labels = ["Nome do Produto:", "Descrição:", "Validade (DD-MM-AAAA):", "Quantidade em Estoque:", "Preço Unitário (R$):"]
entries = []

for i, texto in enumerate(labels):
    tk.Label(frame_cad, text=texto, font=("Arial", 10), bg=COR_AE, fg="white").grid(row=i, column=0, padx=20, pady=15, sticky="e")
    entry = tk.Entry(frame_cad, width=35, font=("Arial", 10), bg="white", fg=COR_B)
    entry.grid(row=i, column=1, padx=20, pady=15)
    entries.append(entry)

ent_cad_nome, ent_cad_desc, ent_cad_val, ent_cad_est, ent_cad_prc = entries

# Botão salvar com destaque em verde (V)
btn_salvar_cadastro = tk.Button(frame_cad, text="✨ Gravar na Vaga Disponível", command=cadastrar_produto, font=("Arial", 11, "bold"), bg=COR_V, fg=COR_B, padx=10, pady=5)
btn_salvar_cadastro.grid(row=5, column=0, columnspan=2, pady=30)

# Inicializa o estoque na caixa de texto ao abrir
atualizar_lista_produtos()

# Inicia a tela do Tkinter
janela.mainloop()