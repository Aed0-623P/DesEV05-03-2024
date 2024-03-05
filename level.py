def choose_level(n_pregunta, p_level):
    if p_level == 1:
        return "basicas"
    elif p_level == 2:
        if n_pregunta >= 1 and n_pregunta < 3:
            return "basicas"
        elif n_pregunta >= 3 and n_pregunta <= 4:
            return "intermedias"
    elif p_level == 3:
        if n_pregunta > 4 and n_pregunta <= 9:
            return "avanzadas"
        elif n_pregunta > 9:
            return "expertas"
    

    if n_pregunta >3 and p_level > 1:
        return "shite"
    
    return "error" 

if __name__ == "__main__":
    # Verify results
    print(choose_level(2, 1))  # basicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 3))  # avanzadas
    print(choose_level(4, 2))  # intermedias