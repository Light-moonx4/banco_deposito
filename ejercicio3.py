saldo = 100000
saldo2 = 50000
opcion = ""

while opcion != "3":
    print("\n1. Retirar dinero")
    print("2. Depositar dinero")
    print("3. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":  # RETIRAR
        print("\nElige tu cuenta:")
        print("1. Cuenta 1 - Saldo:", saldo)
        print("2. Cuenta 2 - Saldo:", saldo2)

        cuenta = input("Ingrese su numero de cuenta (1 o 2): ")

        if cuenta != "1" and cuenta != "2":
            print("Cuenta invalida")
            continue

        retirar = float(input("Cuanto desea retirar: "))
        comision = (retirar // 4000) * 1000

        if cuenta == "1":
            if saldo >= retirar:
                saldo -= retirar

                if saldo >= comision:
                    saldo -= comision
                elif saldo2 >= comision:
                    saldo2 -= comision
                    print("Comisión cobrada desde Cuenta 2")
                else:
                    saldo += retirar
                    print("No hay saldo suficiente para cobrar la comisión")
                    continue

                print("Retiro exitoso.")
                print("Comision cobrada:", comision)
                print("Saldo Cuenta 1:", saldo)
                print("Saldo Cuenta 2:", saldo2)
            else:
                print("Saldo insuficiente para retirar")

        else:  # Cuenta 2
            if saldo2 >= retirar:
                saldo2 -= retirar

                if saldo2 >= comision:
                    saldo2 -= comision
                elif saldo >= comision:
                    saldo -= comision
                    print("Comisión cobrada desde Cuenta 1")
                else:
                    saldo2 += retirar
                    print("No hay saldo suficiente para cobrar la comisión")
                    continue

                print("Retiro exitoso.")
                print("Comision cobrada:", comision)
                print("Saldo Cuenta 1:", saldo)
                print("Saldo Cuenta 2:", saldo2)
            else:
                print("Saldo insuficiente para retirar")

    elif opcion == "2":  # DEPOSITAR
        print("\nElige tu cuenta:")
        print("1. Cuenta 1 - Saldo:", saldo)
        print("2. Cuenta 2 - Saldo:", saldo2)

        cuenta = input("Ingrese su numero de cuenta (1 o 2): ")

        if cuenta != "1" and cuenta != "2":
            print("Cuenta invalida")
            continue

        depositar = float(input("Cuanto desea depositar: "))

        if cuenta == "1":
            saldo += depositar
            print("Deposito exitoso.")
            print("Saldo Cuenta 1:", saldo)
        else:
            saldo2 += depositar
            print("Deposito exitoso.")
            print("Saldo Cuenta 2:", saldo2)

    elif opcion == "3":
        print("Gracias por utilizar nuestro sistema")

    else:
        print("Opcion invalida")