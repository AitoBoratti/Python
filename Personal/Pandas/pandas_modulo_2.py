import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Producto': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Ventas': [100, 150, 200, 300, 120, 130],
    'Cantidad': [1, 2, 3, 1, 2, 3]
}

df = pd.DataFrame(data)

# Calcular la suma de una columna
aux = df['Ventas'].sum()  # Suma total de las ventas
# print(aux)

# Calcular el promedio
aux = df['Ventas'].mean()  # Promedio de las ventas
# print(aux)

# Calcular suma agrupando
aux = df.groupby('Producto')['Ventas'].sum()
# print(aux)

resumen = df.groupby('Producto').agg({
    'Ventas': ['sum', 'mean'],
    'Cantidad': ['sum']
})
# print(resumen)

pivot = df.pivot_table(values='Ventas', index='Producto', columns='Cantidad', aggfunc='sum')
# print(pivot)

df['Ingresos'] = df['Ventas'] * df['Cantidad']
print(df)