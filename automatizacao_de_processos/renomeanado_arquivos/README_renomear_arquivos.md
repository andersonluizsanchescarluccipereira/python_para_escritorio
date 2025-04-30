
# 🔄 Script de Renomeação em Massa com Python

Este script automatiza o processo de **renomear arquivos em uma pasta**, útil para organização, uploads, backups e padronização de nomes.

---

## 📂 O Que o Script Faz

Ele percorre todos os arquivos de uma pasta e os renomeia seguindo o padrão:

```
arquivo_1.ext
arquivo_2.ext
arquivo_3.ext
...
```

O número é incremental e a extensão original dos arquivos é mantida.

---

## 🧠 Como Funciona

```python
pasta = "./meus_arquivos"
arquivos = os.listdir(pasta)

for i, nome_antigo in enumerate(arquivos, start=1):
    nome_novo = f"arquivo_{i}{extensao}"
    os.rename(caminho_antigo, caminho_novo)
```

---

## ⚙️ Como Usar

1. Coloque o script na mesma pasta dos arquivos OU configure o caminho na variável `pasta`.
2. Rode o script em um terminal ou IDE:
```bash
python renomear_arquivos.py
```
3. Os arquivos serão renomeados no formato `arquivo_1`, `arquivo_2`, etc.

---

## ⚠️ Cuidados

- **Faça backup antes de rodar o script.**
- O script sobrescreve nomes se já existirem arquivos com o mesmo nome novo.
- Funciona apenas para arquivos (não lida com pastas recursivamente).

---

## 🛠 Exemplo

### Antes:
```
foto.jpg
relatorio_final.docx
planilha.xlsx
```

### Depois de executar:
```
arquivo_1.jpg
arquivo_2.docx
arquivo_3.xlsx
```

---

## ✅ Requisitos

- Python 3.x
- Permissões de leitura e escrita na pasta alvo

---

## ✨ Personalizações Sugeridas

- Adicionar prefixos personalizados (`relatorio_`, `imagem_`, etc.)
- Incluir data e hora nos nomes
- Trabalhar com subpastas (recursivo)
