import random


def apostador():
    numeros = list()
    for i in range(6):
        while True:
            try:
                numero = int(input("Digite um número: "))
                if (1 <= numero <= 60):
                    if (numero in numeros):
                        print("Tente outro número.")
                    else:
                        numeros.append(numero)
                        break
                else:
                    print("Digite um número entre 0 e 60.")
            except ValueError:
                print("Digite um número válido.")

    return numeros
#------------------------------------------------
def validacao(aposta):
    pontos = int()
    numeros = random.sample(range(1,61), 6)

    for i in range(len(aposta)):
        for j in range(len(numeros)):
            if  (aposta[i] == numeros[j]):
                pontos += 1

    return pontos, numeros
#------------------------------------------------
def premiacao(pontos):
    if  (pontos < 4):
        return "Infelizmente você acertou nenhum número."
    elif  (pontos == 4):
        return "Parabéns! Você conseguiu acertar a quadra!"
    elif  (pontos == 5):
        return "Parabéns! Você conseguiu acertar a quina!"
    else:
        return "Parabéns! Você conseguiu acertar tudo!"
#------------------------------------------------
def main():
    num = apostador()
    aposta, sorteados = validacao(num)

    print(f'Os números escolhidos foram: {sorted(num)}')
    print(f'Os números sorteados foram: {sorted(sorteados)}')
    print(premiacao(aposta))


if  __name__=="__main__":
    main()