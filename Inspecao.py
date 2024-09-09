import tkinter as tk
from tkinter import scrolledtext, messageboxj

# Função que será chamada quando o formulário for submetido
def run_inspection_form():
    # Recuperar valores dos campos
    inspecao_codigo = entry_inspecao_codigo.get()
    clientes_codigo = entry_clientes_codigo.get()
    equipamento_codigo = entry_equipamento_codigo.get()
    periodode = entry_periodode.get()
    periodoate = entry_periodoate.get()
    tipoinspecao = entry_tipoinspecao.get()
    datarealizada1 = entry_datarealizada1.get()
    datarealizada2 = entry_datarealizada2.get()
    datarealizada3 = entry_datarealizada3.get()
    inspetorexecutante_codigo = entry_inspetorexecutante_codigo.get()
    inspecaodocumento = entry_inspecaodocumento.get()
    introducaoinspecao = entry_introducaoinspecao.get()

    # Verificar se todos os campos foram preenchidos
    if not (inspecao_codigo and clientes_codigo and equipamento_codigo and periodode and periodoate and
            tipoinspecao and datarealizada1 and datarealizada2 and datarealizada3 and
            inspetorexecutante_codigo and inspecaodocumento and introducaoinspecao):
        # Mostra uma caixa de diálogo de erro se algum campo estiver vazio
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    # Exibir os dados preenchidos no ScrolledText
    output_text.insert(tk.END, f"Código da Inspeção: {inspecao_codigo}\n")
    output_text.insert(tk.END, f"Código do Cliente: {clientes_codigo}\n")
    output_text.insert(tk.END, f"Código do Equipamento: {equipamento_codigo}\n")
    output_text.insert(tk.END, f"Período De: {periodode}\n")
    output_text.insert(tk.END, f"Período Até: {periodoate}\n")
    output_text.insert(tk.END, f"Tipo de Inspeção: {tipoinspecao}\n")
    output_text.insert(tk.END, f"Data Realizada 1: {datarealizada1}\n")
    output_text.insert(tk.END, f"Data Realizada 2: {datarealizada2}\n")
    output_text.insert(tk.END, f"Data Realizada 3: {datarealizada3}\n")
    output_text.insert(tk.END, f"Código do Inspetor Executante: {inspetorexecutante_codigo}\n")
    output_text.insert(tk.END, f"Documento de Inspeção: {inspecaodocumento}\n")
    output_text.insert(tk.END, f"Introdução da Inspeção: {introducaoinspecao}\n")
    output_text.insert(tk.END, "\nFormulário preenchido com sucesso!\n\n")

# Configuração da interface gráfica
root = tk.Tk()  # Criar a janela principal
root.title("Formulário de Inspeção")  # Definir o título da janela
root.geometry("800x600")  # Definir o tamanho da janela

# Lista de campos do formulário com o nome das variáveis para criação dinâmica
fields = [
    ("Código da Inspeção", "entry_inspecao_codigo"),
    ("Código do Cliente", "entry_clientes_codigo"),
    ("Código do Equipamento", "entry_equipamento_codigo"),
    ("Período De (yyyy-mm-dd)", "entry_periodode"),
    ("Período Até (yyyy-mm-dd)", "entry_periodoate"),
    ("Tipo de Inspeção", "entry_tipoinspecao"),
    ("Data Realizada 1 (yyyy-mm-dd)", "entry_datarealizada1"),
    ("Data Realizada 2 (yyyy-mm-dd)", "entry_datarealizada2"),
    ("Data Realizada 3 (yyyy-mm-dd)", "entry_datarealizada3"),
    ("Código do Inspetor Executante", "entry_inspetorexecutante_codigo"),
    ("Documento de Inspeção", "entry_inspecaodocumento"),
    ("Introdução da Inspeção", "entry_introducaoinspecao")
]

# Criar dinamicamente as Labels (rótulos) e os Entry fields (campos de entrada)
entries = {}  # Dicionário para armazenar as entradas
for label_text, entry_name in fields:
    label = tk.Label(root, text=label_text)  # Criar um rótulo para cada campo
    label.pack()  # Exibir o rótulo na janela
    entry = tk.Entry(root)  # Criar um campo de entrada de texto
    entry.pack()  # Exibir o campo de entrada
    entries[entry_name] = entry  # Armazenar o campo de entrada no dicionário
    globals()[entry_name] = entry  # Criar uma variável global com o nome do campo de entrada

# Text area (área de texto) para mostrar a saída do formulário
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=10)
output_text.pack(padx=10, pady=10)  # Adiciona a área de texto com rolagem

# Botão para rodar a função que processa o formulário
run_button = tk.Button(root, text="Preencher Formulário", command=run_inspection_form)
run_button.pack(pady=10)  # Exibe o botão na janela

# Iniciar o loop da interface gráfica
root.mainloop()  # Iniciar o loop principal para manter a janela aberta
