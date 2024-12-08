import tkinter as tk
from tkinter import messagebox

# Funções de operação
def adicionar():
    try:
        resultado = float(entry1.get()) + float(entry2.get())
        entry3.delete(0, tk.END)
        entry3.insert(0, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos")

def subtrair():
    try:
        resultado = float(entry1.get()) - float(entry2.get())
        entry3.delete(0, tk.END)
        entry3.insert(0, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos")

def multiplicar():
    try:
        resultado = float(entry1.get()) * float(entry2.get())
        entry3.delete(0, tk.END)
        entry3.insert(0, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos")

def dividir():
    try:
        divisor = float(entry2.get())
        if divisor != 0:
            resultado = float(entry1.get()) / divisor
            entry3.delete(0, tk.END)
            entry3.insert(0, str(resultado))
        else:
            messagebox.showerror("Erro", "Divisão por zero")
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Criação dos widgets
tk.Label(root, text="Número 1").grid(row=0, column=0)
tk.Label(root, text="Número 2").grid(row=1, column=0)
tk.Label(root, text="Resultado").grid(row=2, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

tk.Button(root, text="Adicionar", command=adicionar).grid(row=3, column=0)
tk.Button(root, text="Subtrair", command=subtrair).grid(row=3, column=1)
tk.Button(root, text="Multiplicar", command=multiplicar).grid(row=4, column=0)
tk.Button(root, text="Dividir", command=dividir).grid(row=4, column=1)

# Iniciar o loop principal
root.mainloop()
