import customtkinter
import sqlite3

def criar_banco():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS pessoas(nome text)")
    conexao.commit()
    conexao.close()


def salvar_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"INSERT INTO pessoas (nome) VALUES('{entrada.get()}')")
    conexao.commit()
    conexao.close()

def ler_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT * FROM pessoas")
    recebe_dados = terminal_sql.fetchall()
    print(recebe_dados)

    nome = ""
    for i in recebe_dados:
        nome += "\n" + str(i[0])
    label_listar.configure(text=nome)

criar_banco()

janela = customtkinter.CTk()
janela.geometry("300x300")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

label_nome = customtkinter.CTkLabel(janela, text="Sistema \nSalva Nome", font=("ariel", 20, "bold"))
label_nome.pack(pady=20)

entrada = customtkinter.CTkEntry(janela, placeholder_text="nome" ,width=150)
entrada.pack(pady=10)
salvar = customtkinter.CTkButton(janela, text="Salvar", width=150, command=salvar_dados)
salvar.pack(pady=5)
listar = customtkinter.CTkButton(janela, text="Listar", width=150, command=ler_dados)
listar.pack(pady=5)
label_listar= customtkinter.CTkLabel(janela, text="")
label_listar.pack(pady=5)
janela.mainloop()
