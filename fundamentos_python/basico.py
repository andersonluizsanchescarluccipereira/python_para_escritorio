def basico_sintaxe():
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


if __name__ == '__main__':
    basico_sintaxe()