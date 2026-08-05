'''
tabela ascii, Faz a tradução de uma string (letras e números) para símbolos de texto.
Sem o uso dela seria somente a leitura em booleano, ou seja, 0 ou 1.
realiza as traduções, como apple para maçã.

Com basse nesse código preciso que me ensine passo a passo como deixar em formato GUI 
usando tkinter e menssagembox

'''

import random
import string
import tkinter as tk
from tkinter import messagebox

# Palette de Cores
COR_AE = "#004d6e"  # Azul Escuro
COR_AM = "#0081ab"  # Azul Médio
COR_AC = "#00b1cd"  # Azul Claro
COR_V  = "#a6c844"  # Verde
COR_R  = "#b83764"  # Rosa / Vermelho
COR_A  = "#edce01"  # Amarelo
COR_B  = "#4a3336"  # Bordô / Marrom Escuro

def gerar_senha_gui():
    try:
        tamanho = int(entry_tamanho.get())
        
        if tamanho <= 0:
            messagebox.showwarning("Atenção", "Por favor, insira um número maior que zero!")
            return
            
        senha_caracteres = string.ascii_letters + string.digits + string.punctuation
        senha_gerada = ''.join(random.choice(senha_caracteres) for _ in range(tamanho))
        
        messagebox.showinfo("Senha Gerada", f"Sua senha criada foi:\n\n{senha_gerada}")
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número inteiro válido!")

# Criando a janela principal
janela = tk.Tk()
janela.title("💛💙 Criar Senhas - Vocacao 💙💛")
janela.geometry("400x325")
janela.configure(bg=COR_AM)  # Fundo da janela principal (Azul Medio)
janela.eval('tk::PlaceWindow . center')

# Rótulo explicativo
label_instrucao = tk.Label(
    janela, 
    text="🔐Digite o tamanho da senha:🔐", 
    bg=COR_AC,       # Fundo no tom da janela
    fg=COR_AE,       # Texto em Aul Escuro
    font=("Arial", 11, "bold")
)
label_instrucao.pack(pady=12)

# Campo onde o usuário digita o número
entry_tamanho = tk.Entry(
    janela, 
    width=10, 
    bg="white", 
    fg=COR_B,        # Texto digitado em Bordô
    insertbackground=COR_B, # Cor do cursor de digitação
    justify="center"
)
entry_tamanho.pack(pady=5)
entry_tamanho.insert(0, "12")

# Botão para acionar a função
botao_gerar = tk.Button(
    janela, 
    text="Gerar Senha", 
    command=gerar_senha_gui,
    bg=COR_V,        # Fundo do botão Verde
    fg=COR_B,        # Texto do botão Bordô
    activebackground=COR_A, # Cor do botão ao ser clicado (Amarelo)
    activeforeground=COR_B,
    font=("Arial", 10, "bold"),
    relief="flat"    # Estilo de borda plana
)
botao_gerar.pack(pady=15)

# Inicia o loop da interface gráfica
janela.mainloop()