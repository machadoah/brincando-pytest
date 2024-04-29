def brincadeira(num) -> any:
    if num > 3:
        return num
    if num % 3 == 0 and num % 5 == 0:
        return "romeu e julieta"
    elif num % 3 == 0:
        return "queijo"
    elif num % 5 == 0:
        return "goiabada"
