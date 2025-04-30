
# 🐍 Introdução à Sintaxe Básica do Python

Este projeto contém um exemplo prático de como usar **variáveis**, **tipos de dados** e **operadores** em Python.

## 📘 O que está incluído

- Declaração de variáveis
- Tipos primitivos (`str`, `int`, `float`, `bool`)
- Operações matemáticas
- Condições com `if`, `and`, `<`
- Impressão formatada com `print()`

## 🧠 Exemplo de Código

```python
# Variáveis e tipos
nome = "Ana"
idade = 25
altura = 1.68
estudante = True

# Operações com números
ano_nascimento = 2025 - idade
imc = 60 / (altura ** 2)  # peso fictício: 60 kg

# Condição usando operadores lógicos e de comparação
if estudante and imc < 25:
    status = "Saudável e estudando"
else:
    status = "Atenção à saúde ou estudos"

# Exibindo tudo
print("Nome:", nome)
print("Ano de nascimento:", ano_nascimento)
print("IMC:", round(imc, 2))
print("Status:", status)
```

## ▶️ Como executar

1. Instale o Python (versão 3.8+ recomendada).
2. Salve o código acima em um arquivo `main.py`.
3. No terminal, execute:
   ```bash
   python basico.py
   ```

## ✅ Saída esperada

```
Nome: Ana
Ano de nascimento: 2000
IMC: 21.26
Status: Saudável e estudando
```

## 🛠️ Requisitos

- Python 3.8 ou superior

---

Sinta-se à vontade para modificar o código e explorar mais possibilidades da linguagem!
