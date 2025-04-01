import customtkinter as ctk
import pygame  # Para som


# Configuração do CustomTkinter
ctk.set_appearance_mode("light")  # Modo claro para ficar mais delicado
ctk.set_default_color_theme("green")  # Tema verdinho, bem fresh ✨

# Criar a janela principal
root = ctk.CTk()
root.geometry("400x550")
root.title("Mensagens Especiais 💖")

# Criar um frame rolável para exibir as mensagens
scrollable_frame = ctk.CTkScrollableFrame(root, width=350, height=450)
scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Lista de mensagens fofinhas
frases = [
    "💖 Você é especial do jeitinho que é! 🌸",
    "✨ Seu sorriso ilumina qualquer lugar! 😍",
    "🌟 A vida é mais bonita com você por perto! 💕",
    "🥰 Você é forte, capaz e incrível! Nunca esqueça! 🌷",
    "💌 Cada dia ao seu lado é um presente lindo! 🎁",
    "🌞 Que hoje seja um dia tão maravilhoso quanto você! 💖",
    "🌈 Espalhe amor e ele voltará para você em dobro! 💫",
    "💜 Seu coração é do tamanho do universo! ✨",
    "🎶 Sua energia é como uma música bonita para o mundo! 🎵",
    "🌸 Nunca esqueça: você merece o melhor sempre! 😘"
]


# Função para tocar um som ao clicar
def tocar_som():
    try:
        pygame.mixer.Sound("click.wav").play()  # Toca um som de clique (coloque um "click.wav" na pasta)
    except Exception as e:
        print(f"Erro ao tocar som: {e}")


# Função quando um item é clicado
def frase_clicada(frase):
    tocar_som()  # Toca o som ao clicar
    popup = ctk.CTkToplevel(root)
    popup.geometry("300x180")
    popup.title("Mensagem Especial 💌")

    # Mostrar a frase com carinho
    label = ctk.CTkLabel(popup, text=frase, font=("Arial", 16), wraplength=280, text_color="#FF69B4")
    label.pack(pady=20)

    ctk.CTkButton(popup, text="Fechar 💖", fg_color="#FF69B4", hover_color="#FF1493",
                  text_color="white", command=popup.destroy).pack(pady=10)


# Criar os botões fofinhos com animação
for frase in frases:
    botao = ctk.CTkButton(scrollable_frame, text=frase, fg_color="#FFD1DC", hover_color="#FF69B4",
                          text_color="#8B008B", corner_radius=15, font=("Arial", 14, "bold"),
                          command=lambda f=frase: frase_clicada(f))

    botao.pack(pady=5, padx=10, fill="x")

    # Animação dos botões (mudam de cor ao passar o mouse)
    botao.bind("<Enter>", lambda e, b=botao: b.configure(fg_color="#FF69B4", text_color="white"))
    botao.bind("<Leave>", lambda e, b=botao: b.configure(fg_color="#FFD1DC", text_color="#8B008B"))

# Rodar a interface
root.mainloop()

