# Escreva um programa que converta temperaturas (Celcius, Fahrenheit e Kelvin)

print("")
print("-"*25)
print("CONVERSOR DE TEMPERATURAS")
print("-"*25)
print("\nQual conversão deseja fazer?\n")

print("1 - Kelvin")
print("2 - Fahrenheit")
print("3 - Celsius")

print("\nDigite apenas o número correspondente.\n")

option1 = int(input("Medida de temperatura de origem: "))



if option1 == 1:  # Kelvin 

    option2 = int(input("Medida de temperatura de destino: ")) 

    if option2 == 1:  # to Kelvin
        kelvin = float(input('Temperatura em K: '))
        print("{} K equivalem a {} K".format(kelvin, kelvin))

    elif option2 == 2:  # to Fahrenheit
        kelvin = float(input('Temperatura em K: '))
        temp = (((kelvin - 273)*1.8) + 32)
        print("{} K equivalem a {} °F".format(kelvin, temp))

    elif option2 == 3: # to Celsius
        kelvin = float(input('Temperatura em K: '))
        temp = kelvin - 273
        print("{} K equivalem a {} °C".format(kelvin, temp))

    else:
        print("Error")



elif option1 == 2: # Fahrenheit

    option2 = int(input("Medida de temperatura de destino: "))

    if option2 == 1:  # to Kelvin
        fahrenheit = float(input('Temperatura em °F: '))
        temp = (((fahrenheit - 32) * (5 / 9)) + 273)
        print("{} °F equivalem a {} K".format(fahrenheit, temp))

    elif option2 == 2:  # to Fahrenheit
        fahrenheit = float(input('Temperatura em °F: '))
        print("{} °F equivalem a {} °F".format(fahrenheit, fahrenheit))

    elif option2 == 3: # to Celsius
        fahrenheit = float(input('Temperatura em °F: '))
        temp = (fahrenheit - 32) / 1.8
        print("{} °F equivalem a {} °C".format(fahrenheit, temp))

    else:
        print("Error")



elif option1 == 3:  # Celsius

    option2 = int(input("Medida de temperatura de destino: "))  

    if option2 == 1:  # to Kelvin
        celsius = float(input('Temperatura em °C: '))
        temp = celsius + 273
        print("{} °C equivalem a {} K".format(celsius, temp))

    elif option2 == 2:  # to Fahrenheit
        celsius = float(input('Temperatura em °C: '))
        temp = celsius * 1.8 + 32
        print("{} °C equivalem a {} °F".format(celsius, temp))

    elif option2 == 3: # to Celsius
        celsius = float(input('Temperatura em °C: '))
        print("{} °C equivalem a {} °C".format(celsius, celsius))
        
    else:
        print("Error")
