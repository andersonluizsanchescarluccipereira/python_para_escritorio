# ============================
# Exemplos de Funções em Python
# ============================

# Função simples
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Anderson")

# Função com retorno
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("Resultado da soma:", resultado)

# Função com parâmetro opcional
def mensagem(texto="Olá, mundo!"):
    print(texto)

mensagem()
mensagem("Olá, Python!")

# Função com docstring
def multiplicar(a, b):
    """Multiplica dois números"""
    return a * b

print("Multiplicação:", multiplicar(4, 7))

# ============================
# Simulando um módulo simples
# ============================

# Normalmente o código abaixo estaria em outro arquivo (meumodulo.py)
def dobro(x):
    return x * 2

def saudacao_personalizada(nome):
    return f"Bem-vindo, {nome}!"

# Usando as funções como se fossem importadas
print(dobro(8))

print(saudacao_personalizada("Maria"))

# ============================
# Função com *args e **kwargs
# ============================

def imprimir_nomes(*args, **kwargs):
    for nome in args:
        print(f"Nome: {nome}")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprimir_nomes("Ana", "Carlos", idade=30, cidade="São Paulo")

# ============================
# Função main e proteção __name__
# ============================

def main():
    print("Este código está sendo executado diretamente.")

if __name__ == "__main__":
    main()