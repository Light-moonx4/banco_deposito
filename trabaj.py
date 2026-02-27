saldo =float(input("digita tu saldo:"))
opcion=""

while opcion!="3":
    print("1.retirar dinero")
    print("2.depositar dinero")
    print("3.salir")

    opcion=input("elige una opcion:")

    if opcion == "1":
        retirar=float(input("cuanto desea retirar:"))
        if retirar<=saldo:
            saldo-=retirar
            print("tu saldo es:",saldo)
        else:
            print("saldo insuficiente")

    elif opcion == "2":
        depositar=float(input("cuanto desea depositar:"))
        saldo+=depositar
        print("tu saldo es:",saldo)
    
    elif opcion == "3":
        print("gracias por utilizar nuestro sistema")
    else:
        print("opcion invalidad")
  

    
