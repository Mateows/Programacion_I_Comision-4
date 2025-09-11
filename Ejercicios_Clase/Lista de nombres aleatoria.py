
#Clase 11/9/2025
alumnos = [
    "Valentina De Los ángeles Albizú",
    "Pablo Andres Allende",
    "Luca Valentín Argumedo",
    "Pablo Avalos",
    "Lucas Avila",
    "Santino Barone",
    "Sofia Blangetti",
    "Nicolás Bohm",
    "Renzo Valentino Borello Canizo",
    "Juan Manuel Carrillo Taglio",
    "Facundo Gustavo Chacon Catalan",
    "Agustin Emiliano Contardi",
    "Jeronimo Coronel Alvarez",
    "Gabriel Emiliano Denis",
    "Facundo Gustavo Deseff",
    "Juan Martin García",
    "Enzo Giaquinta",
    "Sabrina Gimenez",
    "Joaquin Godoy",
    "Lucas Facundo Godoy",
    "Santino Alejo Godoy Galdeano",
    "Valentina Antonela Gordillo Moreno",
    "Lautaro Agustin Guardatti Esquivel",
    "Tiago Nahuel Guillot Duran",
    "Mateo Lautaro Liendo",
    "Juan Ignacio Martinez Quiroga",
    "Maximo Exequiel Monardez",
    "Tomas Agustin Mora Gonzalez",
    "Pablo Isaias Morinigo Lima",
    "Ares Martín Ocaña Martinez",
    "Thiago Santino Oviedo Saldaño",
    "Amanda Lucrecia Pagano",
    "Máximo Juan Cruz Quiroga",
    "Facundo Agustín Ramírez García",
    "Franco Agustin Rios Alzamora",
    "Leonel Enrique Rojas",
    "Matias Nicolas Ruiz Vargas",
    "Ramiro Ezequiel Salcedo",
    "Ismael Saleme Padolsky",
    "Ignacio Exequiel Sanchez",
    "Fabrizio Jonathan Simon Santos",
    "Cristian Gabriel Soto",
    "Giovanna Mercedes Suarez",
    "Ismael Mauricio Suarez",
    "Fernando Agustín Torrez",
    "Luca Nicolas Valdez",
    "Tiziano Ignacio Valentini",
    "Matias Nicolas Vargas",
    "Juan Ignacio Videla Continella",
    "Pablo Exequiel Avalos"]
# for i in range(len(alumnos)):
#     print (i)


#Se crea la lista de numeros del 1-49
lista_numero_alumnos = list(range(1,49))
# print (lista_numero_alumnos)
##Se recorre la lista desde 49 hasta 1 y se comienza a desordenar la lista por bucle
for i in range(len(lista_numero_alumnos)-1,0,-1):
    j =(i*7+3) % (i+1) #j quedara entre 0 y i
    lista_numero_alumnos[i],lista_numero_alumnos[j] = lista_numero_alumnos[j], lista_numero_alumnos[i]


for i in range(0, len(lista_numero_alumnos),4):
    for num in lista_numero_alumnos[i:i+4]:
        print(alumnos[num-1])
