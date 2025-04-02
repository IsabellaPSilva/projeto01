#oieeeeee
import customtkinter
from tkinter import ttk
import sqlite3
item_vet = 0


def abrir_cadastro():
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_saida_relatorio.grid_forget()
    frame_estoque_relatorio.grid_forget()
    frame_estoque_entrada.grid_forget()
    frame_cadastro.grid_propagate(False)
    frame_cadastro.grid(row=0, column=1, pady=5, padx=5)

def abrir_editar():
    frame_cadastro.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_saida_relatorio.grid_forget()
    frame_estoque_relatorio.grid_forget()
    frame_estoque_entrada.grid_forget()
    frame_editar.grid_propagate(False)
    frame_editar.grid(row=0, column=1, pady=5, padx=5)
    ler_dados_editar()

def abrir_saida():
    frame_cadastro.grid_forget()
    frame_editar.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_saida_relatorio.grid_forget()
    frame_estoque_relatorio.grid_forget()
    frame_estoque_entrada.grid_forget()
    frame_saida.grid_propagate(False)
    frame_saida.grid(row=0, column=1, pady=5, padx=5)
    ler_dados_saida()

def abrir_entrada():
    frame_cadastro.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_relatorio.grid_forget()
    frame_saida_relatorio.grid_forget()
    frame_estoque_relatorio.grid_forget()
    frame_estoque_entrada.grid_forget()
    frame_entrada.grid_propagate(False)
    frame_entrada.grid(row=0, column=1, pady=5, padx=5)
    ler_dados_entrada()

def abrir_relatorio():
    frame_cadastro.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_saida_relatorio.grid_forget()
    frame_estoque_relatorio.grid_forget()
    frame_estoque_entrada.grid_forget()
    frame_relatorio.grid_propagate(False)
    frame_relatorio.grid(row=0, column=1, pady=5, padx=5)
    ler_dados()

def abrir_estoque_saida():
    frame_cadastro.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_estoque_relatorio.grid_forget()
    frame_estoque_entrada.grid_forget()
    frame_saida_relatorio.grid_propagate(False)
    frame_saida_relatorio.grid(row=0, column=1, pady=5, padx=5)

def abrir_estoque_entrada():
    frame_cadastro.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_saida_relatorio.grid_forget()
    frame_estoque_relatorio.grid_forget()
    frame_estoque_entrada.grid_propagate(False)
    frame_estoque_entrada.grid(row=0, column=1, pady=5, padx=5)

def adicionar_item_saida():
    global item_vet
    item_vet = str(entrada_adicionar_saida.get())

    if item_vet in items_saida:
        item_texto = entrada_adicionar_saida.get()
        if item_texto:
            frame_item = customtkinter.CTkFrame(lista_frame_saida)
            frame_item.pack(fill="x", pady=2, padx=5)

            label = customtkinter.CTkLabel(frame_item, text=item_vet, anchor="w")
            label.pack(side="left", fill="x", expand=True, padx=5)

            botao_remover = customtkinter.CTkButton(frame_item, text="🗑", width=30,
                                                    command=lambda: frame_item.destroy())
            botao_remover.pack(side="right", padx=5)

            entrada_adicionar_saida.delete(0, "end")

def adicionar_item_entrada():
    global item_vet
    item_vet = str(entrada_adicionar_entrada.get())

    if item_vet in items_entrada:
        item_texto = entrada_adicionar_entrada.get()
        if item_texto:
            frame_item = customtkinter.CTkFrame(lista_frame_entrada)
            frame_item.pack(fill="x", pady=2, padx=5)

            label = customtkinter.CTkLabel(frame_item, text=item_vet, anchor="w")
            label.pack(side="left", fill="x", expand=True, padx=5)

            botao_remover = customtkinter.CTkButton(frame_item, text="🗑", width=30,
                                                    command=lambda: frame_item.destroy())
            botao_remover.pack(side="right", padx=5)

            entrada_adicionar_entrada.delete(0, "end")

def abrir_janela():
    pop_up = customtkinter.CTk()
    pop_up.title("pop-up")
    pop_up.geometry("400x300")
    label_Escolher_relatorio = customtkinter.CTkLabel(pop_up, text="Escolher relatório(s):")
    label_Escolher_relatorio.grid(pady=20, row=0, column=0)
    label_Escolher_extensao = customtkinter.CTkLabel(pop_up, text="Escolher extensão:")
    label_Escolher_extensao.grid(pady=20, row=0, column=1)
    entrada_exportar_estoque = customtkinter.CTkCheckBox(pop_up, text="exportar estoque")
    entrada_exportar_estoque.grid(row=1, column=0, sticky="w", pady=10, padx=40)
    entrada_exportar_saida = customtkinter.CTkCheckBox(pop_up, text="exportar saída")
    entrada_exportar_saida.grid(row=2, column=0, sticky="w", pady=10, padx=40)
    entrada_exportar_entrada = customtkinter.CTkCheckBox(pop_up, text="exportar entrada")
    entrada_exportar_entrada.grid(row=3, column=0, sticky="w", pady=10, padx=40)
    entrada_word = customtkinter.CTkCheckBox(pop_up, text="Word")
    entrada_word.grid(row=1, column=1, sticky="w", pady=10, padx=40)
    entrada_pdf = customtkinter.CTkCheckBox(pop_up, text="PDF")
    entrada_pdf.grid(row=2, column=1, sticky="w", pady=10, padx=40)
    entrada_excel = customtkinter.CTkCheckBox(pop_up, text="Excel")
    entrada_excel.grid(row=3, column=1, sticky="w", pady=10, padx=40)
    botao_cancelar_window = customtkinter.CTkButton(pop_up, text="Cancelar", width=80, height=30)
    botao_cancelar_window.grid(row=4, column=1, pady=40, padx=5, sticky="w")
    botao_salvar_window = customtkinter.CTkButton(pop_up, text="Salvar", width=80, height=30)
    botao_salvar_window.grid(row=4, column=1, pady=40, padx=5, sticky="e")
    pop_up.mainloop()

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

def criar_banco():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS pessoas(nome text,preco float ,descricao text,quantidade integer)")
    conexao.commit()
    conexao.close()

def salvar_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"INSERT INTO pessoas  VALUES('{entrada_produto.get()}','{entrada_preco.get()}','{entrada_descricao_cadastro.get('1.0','end')}','{0}')")
    conexao.commit()
    conexao.close()

def ler_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT * FROM pessoas")
    recebe_dados = terminal_sql.fetchall()
    print(recebe_dados)

    for item in tabela_estoque.get_children():
        tabela_estoque.delete(item)

    for i in recebe_dados:
        produto = str(i[0])
        preco = str(i[1])
        descricao = str(i[2])
        quantidade = str(i[3])
        tabela_estoque.insert("", "end", values=(produto, quantidade,preco,descricao))

def ler_dados_editar():

    global caixa_editar

    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM pessoas")
    items_editar = terminal_sql.fetchall()

    for item in frame_lista_editar.winfo_children():
        item.destroy()

    for item in items_editar:
        caixa_editar = customtkinter.CTkCheckBox(frame_lista_editar, text=item, checkmark_color="Black")
        caixa_editar.grid(pady=5, padx=10, stick="s")
        caixa_editar.configure(command=lambda nome=item[0], cb=caixa_editar: (selecionar_item_editar(nome) if cb.get() == 1 else desmarcar_item()))

    def selecionar_item_editar(arg_item):
        conexao = sqlite3.connect("dados.db")
        terminal_sql = conexao.cursor()
        terminal_sql.execute(f"SELECT * FROM pessoas WHERE nome ='{arg_item}'")
        receber_dados_produto = terminal_sql.fetchall()
        print(receber_dados_produto)

        entrada_produto_editar.insert(0, receber_dados_produto[0][0])
        entrada_quantidade_editar.insert(0, receber_dados_produto[0][1])
        entrada_descricao_editar.insert(0.0, receber_dados_produto[0][2])

    def desmarcar_item():
        entrada_produto_editar.delete(0, "end")
        entrada_quantidade_editar.delete(0, "end")
        entrada_descricao_editar.delete(0.0, "end")

def ler_dados_saida():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM pessoas")
    items_saida = terminal_sql.fetchall()

    for item in frame_lista_saida.winfo_children():
        item.destroy()

    for item in items_saida:
        caixa_saida = customtkinter.CTkCheckBox(frame_lista_saida, text=item, checkmark_color="Black")
        caixa_saida.grid(pady=5, padx=10, stick="s")
        caixa_saida.configure(command=lambda nome=item[0], cb=caixa_saida: (selecionar_item_saida(nome) if cb.get() == 1 else desmarcar_item_saida()))

    def selecionar_item_saida(arg_item):
        conexao = sqlite3.connect("dados.db")
        terminal_sql = conexao.cursor()
        terminal_sql.execute(f"SELECT * FROM pessoas WHERE nome ='{arg_item}'")
        receber_dados_produto = terminal_sql.fetchall()
        print(receber_dados_produto)

        entrada_adicionar_saida.insert(0, receber_dados_produto[0][0])
        entrada_quantidade_saida.insert(0, receber_dados_produto[0][3])

    def desmarcar_item_saida():
        entrada_adicionar_saida.delete(0, "end")
        entrada_quantidade_saida.delete(0, "end")

def ler_dados_entrada():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM pessoas")
    items_entrada = terminal_sql.fetchall()

    for widget in frame_lista_entrada.winfo_children():
        widget.destroy()

    for item in items_entrada:
        caixa_entrada = customtkinter.CTkCheckBox(frame_lista_entrada,text=item[0])
        caixa_entrada.grid(pady=5)
        caixa_entrada.configure(command=lambda nome=item[0], cb=caixa_entrada: (selecionar_item_entrada(nome) if cb.get() == 1 else desmarcar_item_entrada()))

    def selecionar_item_entrada(arg_item):
        conexao = sqlite3.connect("dados.db")
        terminal_sql = conexao.cursor()
        terminal_sql.execute(f"SELECT * FROM pessoas WHERE nome ='{arg_item}'")
        receber_dados_produto = terminal_sql.fetchall()
        print(receber_dados_produto)

        entrada_adicionar_entrada.insert(0, receber_dados_produto[0][0])
        entrada_quantidade_entrada.insert(0, receber_dados_produto[0][3])

    def desmarcar_item_entrada():
        entrada_adicionar_entrada.delete(0, "end")
        entrada_quantidade_entrada.delete(0, "end")

def deletar_produto(nome_produto):
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"DELETE FROM pessoas WHERE nome = '{nome_produto}'")
    conexao.commit()
    conexao.close()
    entrada_produto_editar.delete(0, "end")
    entrada_quantidade_editar.delete(0, "end")
    entrada_descricao_editar.delete(0.0, "end")
    ler_dados_editar()

def editar_produtos(nome_produto, preco_produto, descriacao_produto):
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"UPDATE pessoas SET nome = '{nome_produto}',preco = '{preco_produto}', descricao = '{descriacao_produto}' WHERE nome = '{nome_produto}'")
    conexao.commit()
    conexao.close()
    entrada_produto_editar.delete(0, "end")
    entrada_quantidade_editar.delete(0, "end")
    entrada_descricao_editar.delete(0.0, "end")
    ler_dados_editar()


criar_banco()

janela = customtkinter.CTk()
janela.geometry("800x400")

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#2a2d2e",
                foreground="white",
                rowheight=25,
                fieldbackground="#343638",
                bordercolor="#343638",
                borderwidth=0)
style.map('Treeview', background=[('selected', '#22559b')])

style.configure("Treeview.Heading",
                background="#565b5e",
                foreground="white",
                relief="flat")
style.map("Treeview.Heading",
          background=[('active', '#3484F0')])

frame_Menu = customtkinter.CTkFrame(janela, width=190, height=400, corner_radius=0)
frame_Menu.grid(row=0, column=0, pady=5, padx=5)
frame_Menu.pack_propagate(False)

frame_cadastro = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame_cadastro.grid(row=0, column=1, pady=5, padx=5)
frame_cadastro.grid_propagate(False)

frame_editar = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame_editar.grid_propagate(False)

frame_saida = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame_saida.grid_propagate(False)

frame_entrada = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame_entrada.grid_propagate(False)

frame_relatorio = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame_relatorio.grid_propagate(False)

frame_saida_relatorio = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame_saida_relatorio.grid_propagate(False)

frame_estoque_relatorio = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame_estoque_relatorio.grid_propagate(False)

frame_estoque_entrada = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame_estoque_entrada.grid_propagate(False)

# Frame do Menu

label_nome_menu = customtkinter.CTkLabel(frame_Menu, text="\nNome Do \nSistema\n", font=("ariel", 15, "bold"))
label_nome_menu.pack(pady=20)
botao_cadastro_menu = customtkinter.CTkButton(frame_Menu, text="cadastrar", command=abrir_cadastro)
botao_cadastro_menu.pack(pady=5)
botao_editar_menu = customtkinter.CTkButton(frame_Menu, text="Editar", command=abrir_editar)
botao_editar_menu.pack(pady=5)
botao_saida_menu = customtkinter.CTkButton(frame_Menu, text="Saída", command=abrir_saida)
botao_saida_menu.pack(pady=5)
botao_entrada_menu = customtkinter.CTkButton(frame_Menu, text="Entrada", command=abrir_entrada)
botao_entrada_menu.pack(pady=5)
botao_relatorio_menu = customtkinter.CTkButton(frame_Menu, text="Relatório", command=abrir_relatorio)
botao_relatorio_menu.pack(pady=5)

# Frame do cadastro

entrada_produto = customtkinter.CTkEntry(frame_cadastro, placeholder_text="Digite o nome do produto", width=300,
                                         height=20)
entrada_produto.grid(row=1, column=1, sticky="w")
entrada_preco = customtkinter.CTkEntry(frame_cadastro, placeholder_text="0,00", width=80, height=20)
entrada_preco.grid(row=2, column=1, sticky="w")
entrada_descricao_cadastro = customtkinter.CTkTextbox(frame_cadastro, width=300, height=80)
entrada_descricao_cadastro.grid(row=3, column=1, sticky="e")

botao_salvar = customtkinter.CTkButton(frame_cadastro, text="Salvar", width=30, command=salvar_dados)
botao_salvar.grid(row=4, column=1, sticky="e", pady=5, padx=5)

label_cadastro = customtkinter.CTkLabel(frame_cadastro, text="Cadastro De Produto", font=("ariel", 20, "bold"))
label_cadastro.grid(row=0, column=1)
label_produto_cadastro = customtkinter.CTkLabel(frame_cadastro, text="Nome Do Produto:")
label_produto_cadastro.grid(row=1, column=0, sticky="e", pady=5, padx=5)
label_preco_cadastro = customtkinter.CTkLabel(frame_cadastro, text="Preço(R$):")
label_preco_cadastro.grid(row=2, column=0, sticky="e", pady=5, padx=5)
label_descricao_cadastro = customtkinter.CTkLabel(frame_cadastro, text="Descrição:")
label_descricao_cadastro.grid(row=3, column=0, pady=5, padx=5, sticky="ne")

# Frame de editar

label_produto_cadastrado = customtkinter.CTkLabel(frame_editar, text="\nEditar Produto Cadastrado\n",
                                                  font=("ariel", 20, "bold"))
label_produto_cadastrado.grid(pady=5, padx=10, row=0, column=0, sticky="n", columnspan=6)

entrada_produto_editar = customtkinter.CTkEntry(frame_editar, placeholder_text="Nome do produto:", width=230)
entrada_produto_editar.grid(row=2, column=1, sticky="ws", columnspan=3, pady=5, padx=5)
entrada_quantidade_editar = customtkinter.CTkEntry(frame_editar, placeholder_text="0,00", width=80)
entrada_quantidade_editar.grid(row=3, column=1, sticky="w", columnspan=3, pady=5, padx=5)
entrada_descricao_editar = customtkinter.CTkTextbox(frame_editar, width=250, height=100)
entrada_descricao_editar.grid(row=4, column=1, sticky="w", columnspan=3, pady=10, padx=10)
entrada_pesquisa_editar = customtkinter.CTkEntry(frame_editar, placeholder_text="Buscar Produto:", width=230)
entrada_pesquisa_editar.grid(row=1, column=0, sticky="w", pady=5, padx=5)

botao_excluir_editar = customtkinter.CTkButton(frame_editar, text="Excluir", width=100, fg_color="red",command=lambda: deletar_produto (entrada_produto_editar.get()))
botao_excluir_editar.grid(row=5, column=1, sticky="e", pady=5, padx=5)
botao_cancelar_editar = customtkinter.CTkButton(frame_editar, text="Cancelar", width=100)
botao_cancelar_editar.grid(row=5, column=2, sticky="e", pady=5, padx=5)
botao_salvar_editar = customtkinter.CTkButton(frame_editar, text="Salvar", width=100, command=lambda : editar_produtos(entrada_produto_editar.get(),entrada_quantidade_editar.get(),entrada_descricao_editar.get(0.0, "end")))
botao_salvar_editar.grid(row=5, column=3, sticky="e", pady=5, padx=5)

frame_lista_editar = customtkinter.CTkScrollableFrame(frame_editar)
frame_lista_editar.grid(pady=5, padx=5, row=2, column=0, rowspan=4)


# Frame da Saida

label_saida_produto = customtkinter.CTkLabel(frame_saida, text="\nSaída do Produto:\n", font=("ariel", 20, "bold"))
label_saida_produto.grid(pady=5, padx=10, row=0, column=0, columnspan=6, stick="n")

entrada_pesquisa_saida = customtkinter.CTkEntry(frame_saida, width=220)
entrada_pesquisa_saida.grid(row=1, column=0, sticky="w", pady=5, padx=5)
entrada_adicionar_saida = customtkinter.CTkEntry(frame_saida, width=230)
entrada_adicionar_saida.grid(row=1, column=1, sticky="w", pady=5, padx=5)
entrada_quantidade_saida = customtkinter.CTkEntry(frame_saida, width=100)
entrada_quantidade_saida.grid(row=2, column=1, sticky="w")

botao_cancelar_saida = customtkinter.CTkButton(frame_saida, text="Cancelar", width=100)
botao_cancelar_saida.grid(row=4, column=1, sticky="w", pady=5, padx=5)
botao_salvar_saida = customtkinter.CTkButton(frame_saida, text="Salvar", width=100)
botao_salvar_saida.grid(row=4, column=1, sticky="e", pady=5, padx=5)
botao_adicionar_saida = customtkinter.CTkButton(frame_saida, text="Adicionar Item", width=128,
                                                command=adicionar_item_saida)
botao_adicionar_saida.grid(row=2, column=1, sticky="e", pady=5, padx=5)

frame_lista_saida = customtkinter.CTkScrollableFrame(frame_saida)
frame_lista_saida.grid(pady=5, padx=5, row=2, column=0, rowspan=4)

lista_frame_saida = customtkinter.CTkFrame(frame_saida, width=300, height=180)
lista_frame_saida.grid(padx=5, pady=5, row=3, column=1, stick="nwes")

# Frame da Entrada

label_saida_entrada = customtkinter.CTkLabel(frame_entrada, text="\nEntrada:\n", font=("ariel", 20, "bold"))
label_saida_entrada.grid(pady=5, padx=10, row=0, column=0, columnspan=6, stick="n")

entrada_pesquisa_entrada = customtkinter.CTkEntry(frame_entrada, width=220)
entrada_pesquisa_entrada.grid(row=1, column=0, sticky="w", pady=5, padx=5)
entrada_adicionar_entrada = customtkinter.CTkEntry(frame_entrada, width=230)
entrada_adicionar_entrada.grid(row=1, column=1, sticky="w", pady=5, padx=5)


entrada_quantidade_entrada = customtkinter.CTkEntry(frame_entrada, width=100)
entrada_quantidade_entrada.grid(row=2, column=1, sticky="w")

botao_cancelar_entrada = customtkinter.CTkButton(frame_entrada, text="Cancelar", width=100)
botao_cancelar_entrada.grid(row=4, column=1, sticky="w", pady=5, padx=5)
botao_salvar_entrada = customtkinter.CTkButton(frame_entrada, text="Salvar", width=100)
botao_salvar_entrada.grid(row=4, column=1, sticky="e", pady=5, padx=5)
botao_adicionar_entrada = customtkinter.CTkButton(frame_entrada, text="Adicionar Item", width=128,
                                                  command=adicionar_item_entrada)
botao_adicionar_entrada.grid(row=2, column=1, sticky="e", pady=5, padx=5)

frame_lista_entrada = customtkinter.CTkScrollableFrame(frame_entrada)
frame_lista_entrada.grid(pady=5, padx=5, row=2, column=0, rowspan=4)


lista_frame_entrada = customtkinter.CTkFrame(frame_entrada, width=300, height=180)
lista_frame_entrada.grid(padx=5, pady=5, row=3, column=1, stick="nwes")

# Frame do Relatório

label_relatorio_estoque = customtkinter.CTkLabel(frame_relatorio, text="\nRelatório do estoque\n",
                                                 font=("ariel", 20, "bold"))
label_relatorio_estoque.grid(pady=5, padx=10, row=0, column=0, columnspan=6, stick="n")

entrada_pesquisa_relatorio = customtkinter.CTkEntry(frame_relatorio, placeholder_text="Barra de pesquisa", width=200)
entrada_pesquisa_relatorio.grid(row=1, column=0, sticky="w", padx=15)

tabela_estoque = ttk.Treeview(frame_relatorio, columns=("Nome", "quantidade", "Preço", "Descrição"), show="headings", height=8)
tabela_estoque.heading("#1", text="Nome")
tabela_estoque.heading("#2", text="quantidade")
tabela_estoque.heading("#3", text="Preço")
tabela_estoque.heading("#4", text="Descrição")
tabela_estoque.column("#1", width=130, anchor="center")
tabela_estoque.column("#2", width=130, anchor="center")
tabela_estoque.column("#3", width=130, anchor="center")
tabela_estoque.column("#4", width=135, anchor="center")

tabela_estoque.grid(row=2, column=0, sticky="ew", columnspan=4, padx=10)

botao_exportar_relatorio = customtkinter.CTkButton(frame_relatorio, text="Exportar", width=100, command=abrir_janela)
botao_exportar_relatorio.grid(row=1, column=3, pady=5, padx=5)
botao_estoque_relatorio = customtkinter.CTkButton(frame_relatorio, text="Estoque", width=100, command=abrir_relatorio)
botao_estoque_relatorio.grid(row=3, column=1, pady=5, padx=5)
botao_ssaida_relatorio = customtkinter.CTkButton(frame_relatorio, text="Saída", width=100, command=abrir_estoque_saida)
botao_ssaida_relatorio.grid(row=3, column=2, pady=3, padx=3)
botao_entrada_relatorio = customtkinter.CTkButton(frame_relatorio, text="Entrada", width=100,
                                                  command=abrir_estoque_entrada)
botao_entrada_relatorio.grid(row=3, column=3, pady=5, padx=5)

# frame da saida do relatorio

label_relatorio_saida = customtkinter.CTkLabel(frame_saida_relatorio, text="\nRelatório da saída\n",
                                               font=("ariel", 20, "bold"))
label_relatorio_saida.grid(pady=5, padx=10, row=0, column=0, columnspan=6, stick="n")

entrada_pesquisa_relatorio_saida = customtkinter.CTkEntry(frame_saida_relatorio, placeholder_text="Barra de pesquisa",
                                                          width=200)
entrada_pesquisa_relatorio_saida.grid(row=1, column=0, sticky="w", padx=15)

tabela_saida = ttk.Treeview(frame_saida_relatorio, columns=("Nome", "quantidade", "Data/hora"), show="headings",
                            height=8)
tabela_saida.heading("#1", text="Nome")
tabela_saida.heading("#2", text="quantidade")
tabela_saida.heading("#3", text="Data/hora")
tabela_saida.column("#1", width=175)
tabela_saida.column("#2", width=175)
tabela_saida.column("#3", width=175)
tabela_saida.grid(row=2, column=0, sticky="ew", columnspan=4, padx=10)

botao_exportar_saida_relatorio = customtkinter.CTkButton(frame_saida_relatorio, text="Exportar", width=100,
                                                         command=abrir_janela)
botao_exportar_saida_relatorio.grid(row=1, column=3, pady=5, padx=5)
botao_estoque_saida_relatorio = customtkinter.CTkButton(frame_saida_relatorio, text="Estoque", width=100,
                                                        command=abrir_relatorio)
botao_estoque_saida_relatorio.grid(row=3, column=1, pady=5, padx=5)
botao_saida_relatorio = customtkinter.CTkButton(frame_saida_relatorio, text="Saída", width=100,
                                                command=abrir_estoque_saida)
botao_saida_relatorio.grid(row=3, column=2, pady=3, padx=3)
botao_entrada_saida_relatorio = customtkinter.CTkButton(frame_saida_relatorio, text="Entrada", width=100,
                                                        command=abrir_estoque_entrada)
botao_entrada_saida_relatorio.grid(row=3, column=3, pady=5, padx=5)

# frame da entrada do relarotorio

label_relatorio_entrada = customtkinter.CTkLabel(frame_estoque_entrada, text="\nRelatorio da Entrada\n",
                                                 font=("ariel", 20, "bold"))
label_relatorio_entrada.grid(pady=5, padx=10, row=0, column=0, columnspan=6, stick="n")

entrada_pesquisa_relatorio_entrada = customtkinter.CTkEntry(frame_estoque_entrada, placeholder_text="Barra de pesquisa",
                                                            width=200)
entrada_pesquisa_relatorio_entrada.grid(row=1, column=0, sticky="w", padx=15)
tabela_entrada = ttk.Treeview(frame_estoque_entrada, columns=("Nome", "quantidade", " Data/hora"), show="headings",
                              height=8)
tabela_entrada.heading("#1", text="Nome")
tabela_entrada.heading("#2", text="quantidade")
tabela_entrada.heading("#3", text="Data/hora")
tabela_entrada.column("#1", width=175)
tabela_entrada.column("#2", width=175)
tabela_entrada.column("#3", width=175)
tabela_entrada.grid(row=2, column=0, sticky="ew", columnspan=4, padx=10)

botao_exportar_entrada_relatorio = customtkinter.CTkButton(frame_estoque_entrada, text="Exportar", width=100,
                                                           command=abrir_janela)
botao_exportar_entrada_relatorio.grid(row=1, column=3, pady=5, padx=5)
botao_estoque_entrada_relatorio = customtkinter.CTkButton(frame_estoque_entrada, text="Estoque", width=100,
                                                          command=abrir_relatorio)
botao_estoque_entrada_relatorio.grid(row=3, column=1, pady=5, padx=5)
botao_saida_entrada_relatorio = customtkinter.CTkButton(frame_estoque_entrada, text="Saída", width=100,
                                                        command=abrir_estoque_saida)
botao_saida_entrada_relatorio.grid(row=3, column=2, pady=3, padx=3)
botao_eentrada_relatorio = customtkinter.CTkButton(frame_estoque_entrada, text="Entrada", width=100,
                                                   command=abrir_estoque_entrada)
botao_eentrada_relatorio.grid(row=3, column=3, pady=5, padx=5)

janela.mainloop()
