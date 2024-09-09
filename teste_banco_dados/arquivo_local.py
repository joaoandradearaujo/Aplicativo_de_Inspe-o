# Variáveis pré-definidas
nome = "Bruno"
idade = 22
cidade = "Curitiba"

# Conteúdo a ser escrito no arquivo
conteudo = f"{nome}|{idade}|{cidade}\n"

# Abrindo (ou criando) o arquivo .txt e escrevendo as informações
with open("informacoes.txt", "w") as arquivo:
    arquivo.write(conteudo)

print("Arquivo criado e preenchido com sucesso!")