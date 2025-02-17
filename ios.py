def calculadora():
    while True:
        print("\n*** Calculadora ***")
        print("1. Soma | 2. Subtração | 3. Multiplicação | 4. Divisão | 5. Sair")

        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Até mais!")
            break

        if escolha not in ['1', '2', '3', '4', '5']:
            print("Opção inválida, tente novamente.")
            continue
            
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif escolha == '4':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida!")
                else:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        except ValueError:
            print("Erro: Digite valores numéricos válidos.")

calculadora()