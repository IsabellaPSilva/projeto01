import customtkinter as ctk

def ler_dados_editar(event=None):
    print("Rolagem detectada")

# Configuração da janela
root = ctk.CTk()
root.geometry("400x300")

# Criar um frame pai
frame_editar = ctk.CTkFrame(root)
frame_editar.pack(fill="both", expand=True)

# Criar o CTkScrollableFrame (sem 'command')
frame_lista_editar = ctk.CTkScrollableFrame(frame_editar)
frame_lista_editar.pack(fill="both", expand=True)

# Adicionar conteúdo para permitir a rolagem
for i in range(20):
    label = ctk.CTkLabel(frame_lista_editar, text=f"Item {i+1}")
    label.pack(pady=5)

# Detectar rolagem com a barra interna
frame_lista_editar._parent_canvas.bind("<Configure>", ler_dados_editar)
frame_lista_editar._parent_canvas.bind("<MouseWheel>", ler_dados_editar)  # Para detectar o scroll do mouse

root.mainloop()
