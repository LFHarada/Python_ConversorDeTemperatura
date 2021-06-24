# Escreva um programa que converta temperaturas (Celcius, Fahrenheit e Kelvin)

while True:

    print("")
    print("-" * 25)
    print("CONVERSOR DE TEMPERATURAS")
    print("-" * 25)
    print("\nQual conversão deseja fazer?\n")

    print("1 - Kelvin")
    print("2 - Fahrenheit")
    print("3 - Celsius")

    print("\nDigite apenas o número correspondente.\n")

    try:

        option1 = int(input("Medida de temperatura de origem: "))

        if option1 == 1:  # Kelvin

            option2 = int(input("Medida de temperatura de destino: "))

            if option2 == 1:  # to Kelvin
                kelvin = float(input('Temperatura em K: '))
                print("\n{:.2f} K equivalem a {:.2f} K".format(kelvin, kelvin))

            elif option2 == 2:  # to Fahrenheit
                kelvin = float(input('Temperatura em K: '))
                temp = (((kelvin - 273.15) * 1.8) + 32)
                print("\n{:.2f} K equivalem a {:.2f} °F".format(kelvin, temp))

            elif option2 == 3:  # to Celsius
                kelvin = float(input('Temperatura em K: '))
                temp = kelvin - 273.15
                print("\n{:.2f} K equivalem a {:.2f} °C".format(kelvin, temp))

            else:
                print("Error")

        elif option1 == 2:  # Fahrenheit

            option2 = int(input("Medida de temperatura de destino: "))

            if option2 == 1:  # to Kelvin
                fahrenheit = float(input('Temperatura em °F: '))
                temp = (((fahrenheit - 32) * (5 / 9)) + 273.15)
                print("\n{:.2f} °F equivalem a {:.2f} K".format(fahrenheit, temp))

            elif option2 == 2:  # to Fahrenheit
                fahrenheit = float(input('Temperatura em °F: '))
                print("\n{:.2f} °F equivalem a {:.2f} °F".format(fahrenheit, fahrenheit))

            elif option2 == 3:  # to Celsius
                fahrenheit = float(input('Temperatura em °F: '))
                temp = (fahrenheit - 32) / 1.8
                print("\n{:.2f} °F equivalem a {:.2f} °C".format(fahrenheit, temp))

            else:
                print("Error")

        elif option1 == 3:  # Celsius

            option2 = int(input("Medida de temperatura de destino: "))

            if option2 == 1:  # to Kelvin
                celsius = float(input('Temperatura em °C: '))
                temp = celsius + 273.15
                print("\n{:.2f} °C equivalem a {:.2f} K".format(celsius, temp))

            elif option2 == 2:  # to Fahrenheit
                celsius = float(input('Temperatura em °C: '))
                temp = celsius * 1.8 + 32
                print("\n{:.2f} °C equivalem a {:.2f} °F".format(celsius, temp))

            elif option2 == 3:  # to Celsius
                celsius = float(input('Temperatura em °C: '))
                print("\n{:.2f} °C equivalem a {:.2f} °C".format(celsius, celsius))

            else:
                print("Error")

        else:
            print('\nErro, por favor, insira apenas o que se pede.')

    except:
        print('\nErro, por favor, insira apenas o que se pede.')
