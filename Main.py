import tkinter as tk
from datetime import datetime

def relogio():
    agora = datetime.now()

    hora_formatada = agora.strftime("%H:%M:%S")

    texto.config(text=str(hora_formatada))

    texto.after(1000, relogio)



tela = tk.Tk()
tela.title("Relógio")
tela.geometry("250x100")


texto = tk.Label(tela, font=("Arial", 24, "bold"))
texto.pack(expand=True)

relogio()


tela.mainloop()
