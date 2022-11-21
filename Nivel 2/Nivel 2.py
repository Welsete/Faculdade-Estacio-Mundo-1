while True:
    try:
        divisor = int(input("Digite um numero com sua base decimal para saber em base binária: "))
        base = divisor
        quociente = 1
        lista = []

        while quociente >= 1:
            resto = divisor % 2
            lista.insert(0, resto)
            quociente = divisor // 2
            divisor = quociente

        binario = ''.join([str(item) for item in lista])
        print("O número em base decimal é:", base)
        print("Corresponde a base binária:", binario)
        break

    except:
        print("Por favor, digite apenas números inteiros e positivos, letras e simbolos não funcionam.")
