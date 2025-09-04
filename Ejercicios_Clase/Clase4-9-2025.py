# Hacer un programa que el usuario introduzca un numero para saber en cuanto se va a incrementar la patente
# por ejemplo si el usuario ingresa 1000 la patente debe de quedar como AAB000

patente_letra="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n_patente= int(input("Ingrese el nùmero que quiera para generar una patente\n "))
contador = 0
for i in (patente_letra):
    for j in (patente_letra):
        for k in (patente_letra):
            for x in range(10):
                for y in range(10):
                    for z in range(10):
                        if contador == n_patente:
                            print(i,j,k,"",x,y,z)
                            exit()
                        contador += 1
