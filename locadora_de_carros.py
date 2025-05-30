def mostra_linha():

    """Mostra uma linha de separação"""
    print('-' * 50)

# Exemplo de uso da função mostra_linha
mostra_linha()

print("Aluguel de Carros com a maior frota do Brasil | Localiza")

mostra_linha()

print("Seja Bem Vindo!")

mostra_linha()

nome = input("Digite seu nome:")

print(f"Olá, {nome}! Estamos felizes em tê-lo conosco")

mostra_linha()

print("Selecione o carro que deseja alugar:")
print("1 - BMW M5 ")
print("2 - MUSTANG")
print("3 - HB20")
print("4 - FUSCA")
print("5 - CIVIC")
print("0 - SAIR")

codigo = int(input("Digite o codigo do veículo que deseja alugar:"))

match codigo:
    case 1:
        print("O veículo escolhido foi BMW M5 | Ele está por R$ 1000")
    case 2:
        print("O veículo escolhido foi MUSTANG | Ele está por R$ 1500")
    case 3:
        print("O veículo escolhido foi HB20 | Ele está por R$500")
    case 4:
        print("O veículo escolhido foi FUSCA | Ele está por R$ 100")
    case 5:
        print("O veículo escolhido foi CIVIC | Ele está por R$ 700")
    case 0:
        print("Saindo do Programa...")
        exit()
    case _:
        print("Codigo inválido. Por favor, tente novamente.") 

mostra_linha()
