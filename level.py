def choose_level(n_pregunta, p_level):
    p_level = str(p_level)
    if p_level == "1":
        return "basicas"
    elif p_level == "2":
        return "intermedias"
    elif p_level == "3":
        return "avanzadas"
    else:
        print("filler, tengo que pillar como devolver")

if __name__ == "__main__":
    # Verify results
    print(choose_level(2, 1))  # basicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 3))  # avanzadas
    print(choose_level(4, 2))  # intermedias