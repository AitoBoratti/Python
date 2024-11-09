import numpy as np

# Función para multiplicar matrices
def matrix_mult(A, B):
    return np.dot(A, B)

# Función para elevar la matriz a una potencia de forma eficiente
def matrix_power(M, n):
    result = np.eye(len(M), dtype=int)  # Matriz identidad
    while n:
        if n % 2 == 1:
            result = matrix_mult(result, M)
        M = matrix_mult(M, M)
        n //= 2
    return result

# Función para calcular el término n usando exponenciación de matrices
def calculate_position_matrix(n):
    base_matrix = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0]], dtype=int)
    initial_values = np.array([2025, 2024, 2023], dtype=int)
    
    if n <= 3:
        return initial_values[n-3]
    
    result_matrix = matrix_power(base_matrix, n-3)
    result = np.dot(result_matrix, initial_values)
    return result[0]

# Solicitar la posición

pos = int(input("Ingrese el número de la posición que desea calcular: "))
while pos != -1:
    result = calculate_position_matrix(pos)
    print(f"El resultado de la posición {pos} es: {result}.")
    pos = int(input("Ingrese el número de la posición que desea calcular: "))
