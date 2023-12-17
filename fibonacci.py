def fibonacci(limite):
    num1 = 0
    num2 = 1
    fib = 0
    print(f'Número #1: {num2}')
    for i in range(limite-1):
        fib = num1 + num2
        num1 = num2
        num2 = fib
        print(f'Número #{i+2}: {fib}')
#------------------------------------------------
def main():
    limite = int(input("Defina um limite: "))
    fibonacci(limite)


if  __name__=="__main__":
    main()