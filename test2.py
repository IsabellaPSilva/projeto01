import customtkinter

item_vet = 0

def abrir_cadastro():
    frame03.grid_forget()
    frame04.grid_forget()
    frame05.grid_forget()
    frame06.grid_forget()
    frame02.grid_propagate(False)
    frame02.grid(row=0, column=1, pady=5, padx=5)

def abrir_editar():
    frame02.grid_forget()
    frame04.grid_forget()
    frame05.grid_forget()
    frame06.grid_forget()
    frame03.grid_propagate(False)
    frame03.grid(row=0, column=1, pady=5, padx=5)

def abrir_saida():
    frame02.grid_forget()
    frame03.grid_forget()
    frame05.grid_forget()
    frame06.grid_forget()
    frame04.grid_propagate(False)
    frame04.grid(row=0, column=1, pady=5, padx=5)

def abrir_entrada():
    frame02.grid_forget()
    frame03.grid_forget()
    frame04.grid_forget()
    frame06.grid_forget()
    frame05.grid_propagate(False)
    frame05.grid(row=0, column=1, pady=5, padx=5)

def abrir_relatorio():
    frame02.grid_forget()
    frame03.grid_forget()
    frame04.grid_forget()
    frame05.grid_forget()
    frame06.grid_propagate(False)
    frame06.grid(row=0, column=1, pady=5, padx=5)

def adicionar_item():
  global item_vet
  item_vet = str(entrada9.get())

  if item_vet in items :
        item_texto = entrada9
        if item_texto:
            frame_item = customtkinter.CTkFrame(lista_frame)
            frame_item.pack(fill="x", pady=2, padx=5)

            label = customtkinter.CTkLabel(frame_item, text=item_vet, anchor="w")
            label.pack(side="left", fill="x", expand=True, padx=5)

            botao_remover = customtkinter.CTkButton(frame_item, text="🗑", width=30, command=lambda: frame_item.destroy())
            botao_remover.pack(side="right", padx=5)

            entrada.delete(0, "end")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("800x400")

frame01 = customtkinter.CTkFrame(janela, width=190, height=400, corner_radius=0)
frame01.grid(row=0, column=0,pady=5,padx=5)
frame01.pack_propagate(False)

frame02 = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame02.grid(row=0, column=1, pady=5, padx=5)
frame02.grid_propagate(False)

frame03 = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame03.grid_propagate(False)

frame04 = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame04.grid_propagate(False)

frame05 = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame05.grid_propagate(False)

frame06 = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0)
frame06.grid_propagate(False)

 #Frame01 Menu

label_nm = customtkinter.CTkLabel(frame01, text="\nNome Do \nSistema\n", font=("ariel", 15, "bold"))
label_nm.pack(pady=20)
botao = customtkinter.CTkButton(frame01, text="cadastrar",command=abrir_cadastro)
botao.pack(pady=5)
botao1 = customtkinter.CTkButton(frame01, text="Editar",command=abrir_editar)
botao1.pack(pady=5)
botao2 = customtkinter.CTkButton(frame01, text="Saída",command=abrir_saida)
botao2.pack(pady=5)
botao3 = customtkinter.CTkButton(frame01, text="Entrada",command=abrir_entrada)
botao3.pack(pady=5)
botao4 = customtkinter.CTkButton(frame01, text="Relatório",command=abrir_relatorio)
botao4.pack(pady=5)

#Frame02 cadastro

entrada = customtkinter.CTkEntry(frame02, placeholder_text="Digite o nome do produto", width=300, height=20)
entrada.grid(row=1, column=1,sticky="w")
entrada2 = customtkinter.CTkEntry(frame02, placeholder_text="0,00", width=80, height=20)
entrada2.grid(row=2, column=1,sticky="w")
entrada3 = customtkinter.CTkTextbox(frame02, width=300, height=80)
entrada3.grid(row=3, column=1,sticky="e")

botao5 = customtkinter.CTkButton(frame02, text="Salvar", width=30)
botao5.grid(row=4, column=1,sticky="e",pady=5,padx=5)

label_saida = customtkinter.CTkLabel(frame02, text="Cadastro De Produto", font=("ariel", 20, "bold"))
label_saida.grid(row=0, column=1)
label_saida1 = customtkinter.CTkLabel(frame02, text="Nome Do Produto:")
label_saida1.grid(row=1, column=0,sticky="e",pady=5,padx=5)
label_saida2 = customtkinter.CTkLabel(frame02, text="Preço(R$):")
label_saida2.grid(row=2, column=0,sticky="e",pady=5,padx=5)
label_saida3 = customtkinter.CTkLabel(frame02, text="Descrição:")
label_saida3.grid(row=3, column=0,pady=5,padx=5,sticky="ne")

#Frame03 editar

label_saida4 = customtkinter.CTkLabel(frame03, text="\nEditar Produto Cadastrado\n", font=("ariel",20, "bold"))
label_saida4.grid(pady=5,padx=10,row=0, column=0,sticky="n",columnspan=6)

entrada4 = customtkinter.CTkEntry(frame03, placeholder_text="Nome do produto:", width=230)
entrada4.grid(row=2, column=1,sticky="ws",columnspan=3,pady=5, padx=5)
entrada5 = customtkinter.CTkEntry(frame03, placeholder_text="0,00", width=80)
entrada5.grid(row=3, column=1,sticky="w",columnspan=3,pady=5,padx=5)
entrada6 = customtkinter.CTkTextbox(frame03, width=250,height=100)
entrada6.grid(row=4, column=1,sticky="w",columnspan=3, pady=10, padx=10)
entrada7 = customtkinter.CTkEntry(frame03, placeholder_text="Buscar Produto:", width=230)
entrada7.grid(row=1, column=0,sticky="w",pady=5, padx=5)

botao6 = customtkinter.CTkButton(frame03, text="Excluir", width=100,fg_color="red")
botao6.grid(row=5, column=1,sticky="e",pady=5,padx=5)
botao7 = customtkinter.CTkButton(frame03, text="Cancelar", width=100)
botao7.grid(row=5, column=2,sticky="e",pady=5,padx=5)
botao8 = customtkinter.CTkButton(frame03, text="Salvar", width=100)
botao8.grid(row=5, column=3,sticky="e",pady=5,padx=5)

scrollable_frame = customtkinter.CTkScrollableFrame(frame03)
scrollable_frame.grid(pady=5, padx=5,row=2, column=0, rowspan=4)
items = ["Produto 1", "Produto 2", "Produto 3", "Produto 4","Produto 5", "Produto 6", "Produto 7", "Produto 8"]
for item in items:
   box = customtkinter.CTkCheckBox(scrollable_frame, text=item,checkmark_color="Black")
   box.grid(pady=5, padx=10, stick="s")

#Frame04 Saida

label_saida5 = customtkinter.CTkLabel(frame04, text="\nSaída do Produto:\n", font=("ariel", 20, "bold"))
label_saida5.grid(pady=5,padx=10,row=0, column=1,columnspan=6)

entrada8 = customtkinter.CTkEntry(frame04, width=220)
entrada8.grid(row=1, column=0,sticky="w",pady=5, padx=5)
entrada9 = customtkinter.CTkEntry(frame04, width=230)
entrada9.grid(row=1, column=1,sticky="w",pady=5, padx=5)

entrada10 = customtkinter.CTkEntry(frame04, width=100)
entrada10.grid(row=2, column=1,sticky="w")

botao9 = customtkinter.CTkButton(frame04, text="Cancelar", width=100)
botao9.grid(row=4, column=1,sticky="w",pady=5,padx=5)
botao10 = customtkinter.CTkButton(frame04, text="Salvar", width=100)
botao10.grid(row=4, column=1,sticky="e",pady=5,padx=5)
botao11 = customtkinter.CTkButton(frame04,text="Adicionar Item", width=128,command=adicionar_item)
botao11.grid(row=2, column=1,sticky="e",pady=5, padx=5)

scrollable_frame = customtkinter.CTkScrollableFrame(frame04)
scrollable_frame.grid(pady=5, padx=5,row=2, column=0, rowspan=4)
items = ["Produto 1", "Produto 2", "Produto 3", "Produto 4","Produto 5", "Produto 6", "Produto 7", "Produto 8"]
for item in items:
   box = customtkinter.CTkCheckBox(scrollable_frame, text=item, checkmark_color="Black")
   box.grid(pady=5, padx=10, stick="s")

lista_frame =customtkinter.CTkFrame(frame04, width=220,height=150)
lista_frame.grid(padx=5, pady=5,row=3, column=1, stick="wens")







label_saida6 = customtkinter.CTkLabel(frame05, text="Entrada:", font=("ariel", 20, "bold"))
label_saida6.grid(pady=20)
label_saida7 = customtkinter.CTkLabel(frame06, text="Relatorio:", font=("ariel", 20, "bold"))
label_saida7.grid(pady=20)


janela.mainloop()

