#Ejercicio 6
parciales = input("Ingrese la notas de los 3(tres) parciales separado por comas: ")
nota_parcial1, nota_parcial2, nota_parcial3 = map(int, parciales.split(","))
total_parciales = nota_parcial1 + nota_parcial2 + nota_parcial3
nota_final = total_parciales / 3
examen_final = 0
trabajo_final = 0
calificacion_final = 0


if (nota_parcial1 < 0 or nota_parcial1 > 10) or (nota_parcial2 < 0 or nota_parcial2 > 10) or (nota_parcial3 < 0 or nota_parcial3 > 10):
    print("Error: Las notas deben estar entre 0 y 10.")
else:
    if nota_final >= 7:
        print("Parcial aprobado")

examen_final = int(input("Ingrese la nota del examen final: "))
if examen_final < 0 or examen_final > 10:
    print("Error: La nota del examen final debe estar entre 0 y 10.")
else:
    if examen_final >= 4:
        print("Examen final aprobado")

trabajo_final = int(input("Ingrese la nota del trabajo final: "))
if trabajo_final < 0 or trabajo_final > 10:
    print("Error: La nota del trabajo final debe estar entre 0 y 10.")  
else:
    if trabajo_final >= 4:
        print("Trabajo final aprobado")

calificacion_final = (nota_final * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print("Calificacion final:", calificacion_final)


#Ejercicio 7
ingreso_dolares = float(input("Ingrese la cantidad de dolares que quiera convertir "))
tasa_fija_peso_argentino = 1358.97
tasa_fija_peso_colombiano = 1250.54
tasa_fija_euros = 1600.50

peso_argentino = ingreso_dolares * tasa_fija_peso_argentino
peso_colombiano = ingreso_dolares * tasa_fija_peso_colombiano
euros = ingreso_dolares * tasa_fija_euros

print("Dolares convertidos a pesos argentinos: ", peso_argentino)
print("Dolares convertidos a pesos colombianos: ", peso_colombiano)
print("Dolares convertidos a euros: ", euros)

#km/3600
#Ejercicio 8
km_a_recorrer = int(input("Cuantos kilometros desea recorrer? "))
precio_gasolina = int(input("Cuanto cuesta la gasolina por litro? "))
litros_necesarios = (km_a_recorrer * 8/100)
precio_gasolina = litros_necesarios * precio_gasolina
horas_necesarios=round(km_a_recorrer/60)

print({f"Para recorrer {km_a_recorrer} kilometros, se necesitan {litros_necesarios} litros de gasolina, que costaran {precio_gasolina} pesos y el viaje tardara {horas_necesarios} horas."})

#Ejercicio 9
prestamo = int(input("Ingrese el monto que desea pedir: "))
interes = 0.02
interes_mensual = prestamo * (1 + interes)**12
monto_mensual= round(interes_mensual)
monto_final = round(interes_mensual * 12)
print(f"El monto a pagar mensualmente es de {monto_mensual} y el monto total a pagar es de {monto_final}")





