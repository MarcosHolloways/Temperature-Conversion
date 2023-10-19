#2021 code

option = True
c = 0
f = 0
k = 0

while option:
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 -Celsius para Kelvin")
    print("4 -Kelvin para Celsius")
    print("5 - Fahrenheit para Kelvin")
    print("6 - Kelvin para Fahrenheit")
    print("0 - para sair")

    menu = int(input("Digite sua opção: "))

    if menu >= 0 and menu <= 6:
        if option == 1:
            #Celsius para Fahrenheit
            c = int(input("Digite a temperatura em c"))
            convert = (c * 9 / 5) + 32
            print(convert, "F")

        elif option == 2:
            #Fahrenheit para Celsius
            f = int(input("Digite a temperatura em f"))
            convert = (f - 32) * 5 / 9
            print(convert, "F")

        elif option == 3:
            #Celsius para Kelvin
            c = int(input("Digite a temperatura em c"))
            convert = c + 273.15
            print(convert, "K")

        elif option == 4:
            #Kelvin para Celsius
            k = int(input("Digite a temperatura em k"))
            convert = k - 273.15
            print(convert, "C")

        elif option == 5:
            #Fahrenheit para Kelvin
            f = int(input("Digite a temperatura em f"))
            convert = (f - 32) * 5 / 9 + 273.15
            print(convert, "K")

        elif option == 6:
            #Kelvin para Fahrenheit
            k = int(input("Digite a temperatura em k"))
            convert = (k - 273.15) * 9/5 + 32
            print(convert, "F")

        elif option == 0:
            #Sair
            print("Saindo..")

        else:
            print("-=-=-=-=-=-=-=-=-=Opção invalida-=-=-=-=-=-=-=-=-=")