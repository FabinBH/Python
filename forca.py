import random
import os

def palavra_secreta():
    batman = ["Batman", "Robin", "Coringa", "Arlequina", "Charada"]
    marvel = ["Pantera Negra", "Surfista Prateado", "Homem Aranha", "Punho de Ferro", "Homem de Ferro"]
    marcas = ["Garoto", "Nestle", "Cacau Show", "HIGH", "Hugo Boss"]
    escolha = list()

    print("Número 1 = lista de palavras relacionadas ao Batman")
    print("Número 2 = lista de palavras relacionadas à Marvel")
    print("Número 3 = lista de palavras relacionadas à marcas em geral")

    while True:
        try:
            opcao = int(input("Digite um número de 1 a 3: "))
            if  (opcao == 1):
                escolha = batman
                os.system("cls")
                print("A palavra escolhida está relacionada ao tema 'Batman'")
                break
            elif  (opcao == 2):
                escolha = marvel
                os.system("cls")
                print("A palavra escolhida está relacionada ao tema 'Marvel'")
                break
            elif  (opcao == 3):
                escolha = marcas
                os.system("cls")
                print("A palavra escolhida está relacionada ao tema 'Marcas em geral'")
                break
            else:
                print("Opção inválida! Digite 1, 2 ou 3!")
        except ValueError:
            print("Valor inválido! Digite apenas números.")
    
    escolha = escolha[random.randint(0, len(escolha))]

    return escolha
#------------------------------------------------
def segredo(palavra):
    sub = ""

    for i in range(len(palavra)):
        if  (palavra[i] != " "):
            sub += "_"
        elif  (palavra[i] == " "):
            sub += " "

    return sub
#------------------------------------------------
def jogador(palavra):
    palavra = palavra.upper()
    palavra_ainda = str()
    lista_letras = []
    segredo2 = segredo(palavra)

    print(segredo2)
    print("Você tem 6 chances para acertar a palavra secreta!")

    while  True:
        letra = input("Digite uma letra: ")
        letra = letra.upper()
        if not letra.isalpha() or len(letra) > 1:
            os.system('cls')
            print("Digite apenas letras! Tente novamente.")
            continue
        else:
            os.system('cls')
            print(f'Você digitou a letra {letra}')
            if (letra in lista_letras):
                print("Você já tentou essa letra! Tente outra.")
                print(f'Você já usou essas letras: {set(lista_letras)}')
                continue
            else:
                palavra_ainda = ""
                if  (letra not in palavra):
                    lista_letras.append(letra)
                for j in range(len(palavra)):
                    if  (palavra[j] == letra):
                        palavra_ainda += letra
                    elif  (segredo2[j] == "_"):
                        palavra_ainda += "_"
                    else:
                        palavra_ainda += segredo2[j]
                print(f'As letras que não fazem parte da palavra são: {lista_letras}')
                segredo2 = palavra_ainda
                print(segredo2)
                if  (len(lista_letras) == len(set(palavra.replace(" ", ""))) + 5):
                    os.system('cls')
                    print("Infelizmente você extrapolou o limite de chances. Tente novamente.")
                    print(f'A palavra secreta era {palavra}')
                    break
                if  (segredo2 == palavra):
                    os.system('cls')
                    print(f'Parabéns! Você acertou a palavra com {len(lista_letras)} erros!')
                    print(f'A palavra secreta era {palavra}')
                    break
#------------------------------------------------
def main():
    palavra = palavra_secreta()
    jogador(palavra)


if  __name__=="__main__":
    main()