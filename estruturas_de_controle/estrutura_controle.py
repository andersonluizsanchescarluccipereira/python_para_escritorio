def estrutura():
    # Exemplo completo de estruturas de controle em Python
    # Condicional
    idade = 17

    if idade >= 18:
        print("Você é maior de idade.")
    elif idade == 17:
        print("Quase lá!")
    else:
        print("Você é menor de idade.")

    print("-" * 30)

    # Loop for
    frutas = ["maçã", "banana", "laranja"]

    for fruta in frutas:
        print("Eu gosto de", fruta)

    print("-" * 30)

    # Loop while
    contador = 0

    while contador < 3:
        print("Contando:", contador)
        contador += 1

    print("-" * 30)

    # Uso de break e continue
    for i in range(5):
        if i == 3:
            print("Interrompendo no", i)
            break
        print("Loop com break:", i)

    print("-" * 30)

    for i in range(5):
        if i == 2:
            print("Pulando o", i)
            continue
        print("Loop com continue:", i)

if __name__ == '__main__':
    estrutura()