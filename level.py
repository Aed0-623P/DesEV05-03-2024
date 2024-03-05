def choose_level(n_pregunta, p_level):
    if n_pregunta >= 1 and n_pregunta < 3:
        p_level = "basicas"
    elif n_pregunta >= 3 and n_pregunta <= 4:
        p_level = "intermedias"
    elif n_pregunta > 4 and n_pregunta <= 9:
        p_level = "avanzadas"
    elif n_pregunta > 9:
        p_level = "nivel inválido"

    return p_level
    # Construir lógica para escoger el nivel
    ##################################################


if __name__ == "__main__":
    # verificar resultados
    print(choose_level(2, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias
