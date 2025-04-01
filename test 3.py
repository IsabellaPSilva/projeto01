import tkinter as tk

def selecionar_item(item):
    """Garante que apenas um checkbox seja marcado e atualiza o TextBox."""
    for opcao in vars:
        if opcao != item:
            vars[opcao].set(False)  # Desmarca todos os outros

    # Atualiza o TextBox com o item selecionado
    textbox.delete("1.0", tk.END)
    if vars[item].get():
        textbox.insert(tk.END, item)

# Configuração da Janela
root = tk.Tk()
root.title("Apenas um CheckBox por vez")

# Criando o dicionário para armazenar os estados dos checkboxes
vars = {}

# Lista de opções
opcoes = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

# Criando Checkbuttons dinamicamente
for opcao in opcoes:
    vars[opcao] = tk.BooleanVar()  # Criando a variável de controle para cada checkbox
    checkbox = tk.Checkbutton(root, text=opcao, variable=vars[opcao],
                              command=lambda opcao=opcao: selecionar_item(opcao))
    checkbox.pack(anchor="w")

# Criando TextBox para exibir o item selecionado
textbox = tk.Text(root, height=2, width=30)
textbox.pack(pady=10)

root.mainloop()
