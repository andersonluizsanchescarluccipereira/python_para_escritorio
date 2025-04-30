
# 📘 Exemplos de Funções e Módulos em Python

Este arquivo contém exemplos comentados e explicados sobre **funções** e **módulos** em Python, voltado para iniciantes.

---

## 🧩 1. Função simples

```python
def saudacao(nome):
    print(f"Olá, {nome}!")
```
> Cria uma função que imprime uma saudação personalizada.

---

## 🔁 2. Função com retorno

```python
def soma(a, b):
    return a + b
```
> Retorna a soma de dois números fornecidos.

---

## 🧰 3. Função com parâmetro opcional

```python
def mensagem(texto="Olá, mundo!"):
    print(texto)
```
> Exibe uma mensagem padrão se nenhum argumento for passado.

---

## 🧾 4. Função com docstring

```python
def multiplicar(a, b):
    """Multiplica dois números."""
    return a * b
```
> Usa docstring para descrever a funcionalidade da função.

---

## 🗂️ 5. Simulando um módulo

```python
def dobro(x):
    return x * 2

def saudacao_personalizada(nome):
    return f"Bem-vindo, {nome}!"
```
> Estas funções simulam o conteúdo de um módulo que pode ser importado.

---

## 📦 6. Usando *args e **kwargs

```python
def imprimir_nomes(*args, **kwargs):
    for nome in args:
        print(f"Nome: {nome}")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
```
> `*args` recebe múltiplos argumentos posicionais.  
> `**kwargs` recebe múltiplos argumentos nomeados.

---

## 🧠 7. Bloco `__main__`

```python
def main():
    print("Este código está sendo executado diretamente.")

if __name__ == "__main__":
    main()
```
> Garante que o bloco de código só seja executado quando o arquivo for executado diretamente, e não quando importado como módulo.

---

## ✅ Conclusão

Esse arquivo é ideal para praticar os conceitos básicos de funções e módulos.  
Você pode copiar cada trecho e testar em um ambiente como o VSCode, PyCharm ou Jupyter Notebook.
