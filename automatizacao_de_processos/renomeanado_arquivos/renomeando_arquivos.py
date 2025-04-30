import os

def renomear():
    # === CONFIGURAÇÃO ===
    # Caminho da pasta com os arquivos a serem renomeados
    pasta = "./meus_arquivos"  # Altere para o caminho da sua pasta local

    # Lê todos os arquivos da pasta
    arquivos = os.listdir(pasta)

    # Renomeia os arquivos com o padrão: arquivo_1.ext, arquivo_2.ext, etc.
    for i, nome_antigo in enumerate(arquivos, start=1):
        caminho_antigo = os.path.join(pasta, nome_antigo)
        nome_base, extensao = os.path.splitext(nome_antigo)
        nome_novo = f"arquivo_{i}{extensao}"
        caminho_novo = os.path.join(pasta, nome_novo)

        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_antigo} → {nome_novo}")

if __name__ == '__main__':
    renomear()