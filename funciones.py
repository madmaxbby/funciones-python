import os
os.system("cls")

def agregar_nota(lista_notas):
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante (entre 1.0 y 7.0): "))
            if 1.0 <= nota <= 7.0:
                lista_notas.append(nota)
                print(f"Nota {nota} agregada exitosamente.")
                break
            else:
                print("Error: La nota debe estar entre 1.0 y 7.0.")
        except:
            print("Error: Debe ingresar un número válido.")

def mostrar_notas(lista_notas):
    if lista_notas:
        print("Notas ingresadas:")
        for i, nota in enumerate(lista_notas, start=1):
            print(f"Estudiante {i}: {nota}")
    else:
        print("No se han ingresado notas.")

def calcular_promedio(lista_notas):
    if lista_notas:
        promedio = sum(lista_notas) / len(lista_notas)
        print(f"El promedio de las notas es: {promedio:.2f}")
    else:
        print("No se han ingresado notas para calcular el promedio.")

def mostrar_max_min(lista_notas):
    if lista_notas:
        nota_max = max(lista_notas)
        nota_min = min(lista_notas)
        print(f"La nota más alta es: {nota_max}")
        print(f"La nota más baja es: {nota_min}")
    else:
        print("No se han ingresado notas para mostrar el máximo y mínimo.")

def main():
    lista_notas = []
    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar nota")
        print("2. Mostrar notas")
        print("3. Calcular promedio")
        print("4. Mostrar nota más alta y más baja")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            agregar_nota(lista_notas)
        elif opcion == '2':
            mostrar_notas(lista_notas)
        elif opcion == '3':
            calcular_promedio(lista_notas)
        elif opcion == '4':
            mostrar_max_min(lista_notas)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")