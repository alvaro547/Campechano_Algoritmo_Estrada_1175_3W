print(" ")
print("Alvaro Campechano Estrada 3W")
print(" ")

def main():
    # Leer tres valores
    A = float(input("Introduce el primer valor (A): "))
    B = float(input("Introduce el segundo valor (B): "))
    C = float(input("Introduce el tercer valor (C): "))

    # Verificar que los valores son distintos
    if A == B or A == C or B == C:
        print("¡Alerta! Los valores introducidos no deben ser iguales.")
    else:
        # Encontrar el mayor y el menor
        mayor = max(A, B, C)
        menor = min(A, B, C)

        # Imprimir los resultados
        print(f"El valor mayor es: {mayor}")
        print(f"El valor menor es: {menor}")

# Ejecutar el algoritmo
if __name__ == "__main__":
    main()

