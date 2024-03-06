def validate(opciones, eleccion):
    opciones2 = opciones
    sub = [sublist[0] for sublist in opciones2]
    while eleccion not in sub:
        eleccion = input(
            "Opción no válida, ingrese una de las opciones válidas: "
        ).lower()
    return eleccion


if __name__ == "__main__":
    eleccion = input("Ingresa una Opción: ").lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = [["a", "b"],["c","d"]]
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
