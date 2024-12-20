def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if es_primo(numero):
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")