personas = 5
dificultad = input("Elige dificultad (facil, media, dificil): ")
#recursos  y consumos segun dificultad

if dificultad == "facil":
    comida = 100
    agua = 100
    energia = 100
    comida_consumida = 1
    consumo_agua = 1
    consumo_energia = 1
elif dificultad == "media":
    comida = 50
    agua = 50
    energia = 50
    comida_consumida = 1
    consumo_agua = 1
    consumo_energia = 1    
elif dificultad == "dificil":
    comida = 20
    agua = 20
    energia = 20
    comida_consumida = 1
    consumo_agua = 1
    consumo_energia = 1     

salud = 100
dia = 1

while salud > 0:

    print("Día", dia)

    #consumo de recursos diarios
    total_comida_consumida = personas * comida_consumida
    total_agua_consumida = personas * consumo_agua
    total_energia_consumida = personas * consumo_energia    
    
    if comida < total_comida_consumida:
        salud -= 10
        print("No hay suficiente comida. Salud disminuida a", salud)
    else:
        comida -= total_comida_consumida
        agua -= total_agua_consumida
        energia -= total_energia_consumida
        print("Comida consumida:", total_comida_consumida, "Restante:", comida)
        print("Agua consumida:", total_agua_consumida, "Restante:", agua)
        print("Energía consumida:", total_energia_consumida, "Restante:", energia)
    
    dia += 1