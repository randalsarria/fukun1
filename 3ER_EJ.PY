#ESCRIBE UN PROGRAMA QUE LEA DE LA ENTRADA ESTANDAR UN 
#VECTOR DE NUMEROS Y MUESTRE EN LA SALIDA ESTANDAR 
#LOS NUMEROS DEL VECTOR CON SUS NDICE ASOCIADOS 

# Ejercicio 3
# Solicitamos la cantidad de elementos
n = int(input("¿Cuántos números deseas ingresar en el vector?: "))

vector = []
for i in range(n):
    num = float(input(f"Ingrese el número para la posición [{i}]: "))
    vector.append(num)

print("\n--- Elementos con sus índices ---")
for i in range(len(vector)):
    print(f"Índice {i} -> Valor: {vector[i]}")