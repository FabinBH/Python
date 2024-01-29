def contador(quantia):
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]

    print("NOTAS:")
    for nota in notas:
        qntNotas = quantia // nota
        print(f'{qntNotas:.0f} nota(s) de R$ {nota:.2f}')
        quantia %= nota

    print("MOEDAS:")
    for moeda in moedas:
        qntMoedas = quantia // moeda
        print(f'{qntMoedas:.0f} moeda(s) de R$ {moeda:.2f}')
        quantia %= moeda
#------------------------------------------------
def main():
    qnt = float(input("Digite a quantia a ser contada: "))
    contador(qnt)


if  __name__=="__main__":
    main()