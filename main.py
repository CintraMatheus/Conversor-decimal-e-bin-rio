import tkinter as tk
from tkinter import messagebox

def converter_para_binario():
    numero_decimal = entrada_decimal.get()
    
    try:
        decimal = int(numero_decimal)
        binario = bin(decimal)[2:]  # Remove o '0b' do início
        resultado_binario.config(text=f"Binário: {binario}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")

def converter_para_decimal():
    try:
        numero_binario = int(entrada_binario.get())
        def checagem_binario(numero_binario):
            return all(digito in '01' for digito in str(numero_binario))
        decimal = 0
        i = 0
        if not checagem_binario(numero_binario=numero_binario):
            raise ValueError
        while numero_binario > 0:
            resto = numero_binario % 10
            decimal += resto * (2 ** i)
            numero_binario = numero_binario // 10
            i += 1

        resultado_decimal.config(text=f'Decimal: {decimal}')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número binário válido.")


# Criar a janela principal
janela = tk.Tk()
janela.title("Conversor Decimal e Binário")
janela.geometry("300x300")
janela.resizable(False, False)
janela.config(background="#3B3F3E")

# Label e entrada para o número decimal
tk.Label(janela, text="Número Decimal :").pack(pady=10)
entrada_decimal = tk.Entry(janela, width=20)
entrada_decimal.pack()

# Botão para converter para binario
botao_converter_para_bin = tk.Button(janela, text="Converter", command=converter_para_binario)
botao_converter_para_bin.pack(pady=10)

# Label e entrada para o número binário
tk.Label(janela, text="Número Binário :").pack(pady=10)
entrada_binario = tk.Entry(janela, width=20)
entrada_binario.pack()

# Botão para converter para decimal
botao_converter_para_dec = tk.Button(janela, text="Converter", command=converter_para_decimal)
botao_converter_para_dec.pack(pady=10)

# Label para exibir o resultado
resultado_binario = tk.Label(janela, text="Binário: ")
resultado_binario.pack(pady=10)
resultado_decimal = tk.Label(janela, text='Decimal: ')
resultado_decimal.pack(pady=10)

# Rodar o aplicativo
janela.mainloop()
