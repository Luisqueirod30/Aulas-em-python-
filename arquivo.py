import os
import platform

def verificar_arquivo(nome_arquivo):
    # 1. Verifica se o arquivo existe
    if os.path.isfile(nome_arquivo):
        print(f"O arquivo '{nome_arquivo}' existe.")

        # 2. Verifica se o arquivo não está vazio
        if os.path.getsize(nome_arquivo) > 0:
            print("O arquivo não está vazio.")

            # 3. Mostra o conteúdo do arquivo
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
                print("Conteúdo do arquivo:")
                print(conteudo)

            # 4. Conta a quantidade de linhas do arquivo
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                print(f"Quantidade de linhas: {len(linhas)}")
        else:
            print("O arquivo está vazio.")
    else:
        print(f"O arquivo '{nome_arquivo}' não existe.")
    nome_arquivo = 'exemplo csv'
# Exemplo de uso
nome_arquivo = input("Digite o nome do arquivo (exemplo: exemplo.csv): ")
verificar_arquivo(nome_arquivo)
 
