import tkinter as tk

def converter_base():
    decimal = entry_decimal.get()
    
    try:
        decimal_value = int(decimal)
        binario = bin(decimal_value)[2:]
        octal = oct(decimal_value)[2:]
        hexadecimal = hex(decimal_value)[2:]
        
        label_binario.config(text=f'Binário: {binario}')
        label_octal.config(text=f'Octal: {octal}')
        label_hexadecimal.config(text=f'Hexadecimal: {hexadecimal}')
    except ValueError:
        label_binario.config(text='Valor inválido')
        label_octal.config(text='Valor inválido')
        label_hexadecimal.config(text='Valor inválido')

# Configuração da interface gráfica
root = tk.Tk()
root.title('Conversor de Bases')

label_decimal = tk.Label(root, text='Decimal:')
label_decimal.grid(row=0, column=0, padx=10, pady=10)

entry_decimal = tk.Entry(root)
entry_decimal.grid(row=0, column=1, padx=10, pady=10)

btn_converter = tk.Button(root, text='Converter', command=converter_base)
btn_converter.grid(row=1, column=0, columnspan=2, pady=10)

label_binario = tk.Label(root, text='Binário:')
label_binario.grid(row=2, column=0, columnspan=2)

label_octal = tk.Label(root, text='Octal:')
label_octal.grid(row=3, column=0, columnspan=2)

label_hexadecimal = tk.Label(root, text='Hexadecimal:')
label_hexadecimal.grid(row=4, column=0, columnspan=2)

root.mainloop()
