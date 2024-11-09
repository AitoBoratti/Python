
# Pandas Learning Path

## Módulo 1: Fundamentos de Pandas

### 1. Instalación y Configuración de Pandas

Para instalar Pandas, ejecuta el siguiente comando:

```bash
pip install pandas
```

Para verificar la instalación, usa:

```python
import pandas as pd
print(pd.__version__)
```

---

### 2. Series y DataFrames

#### Creación de Series

1. **Desde una lista:**
   ```python
   serie_lista = pd.Series([10, 20, 30, 40, 50])
   ```

2. **Desde un diccionario:**
   ```python
   serie_diccionario = pd.Series({'a': 10, 'b': 20, 'c': 30})
   ```

3. **Con un valor escalar:**
   ```python
   serie_escalar = pd.Series(5, index=[0, 1, 2, 3, 4])
   ```

4. **Cambiar el índice de una Serie:**
   - Al crear la Serie:
     ```python
     serie_con_indice = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
     ```
   - Después de crear la Serie:
     ```python
     serie_lista.index = ['a', 'b', 'c', 'd', 'e']
     ```

---

#### Creación de DataFrames

1. **Desde un diccionario de listas:**
   ```python
   df = pd.DataFrame({
       'Nombre': ['Ana', 'Luis', 'Carlos'],
       'Edad': [23, 25, 22],
       'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
   })
   ```

2. **Desde una lista de diccionarios:**
   ```python
   df = pd.DataFrame([
       {'Nombre': 'Ana', 'Edad': 23, 'Ciudad': 'Madrid'},
       {'Nombre': 'Luis', 'Edad': 25, 'Ciudad': 'Barcelona'},
       {'Nombre': 'Carlos', 'Edad': 22, 'Ciudad': 'Valencia'}
   ])
   ```

3. **Desde una lista de listas (con etiquetas de columna):**
   ```python
   df = pd.DataFrame([
       ['Ana', 23, 'Madrid'],
       ['Luis', 25, 'Barcelona'],
       ['Carlos', 22, 'Valencia']
   ], columns=['Nombre', 'Edad', 'Ciudad'])
   ```

4. **DataFrame vacío y añadir columnas:**
   ```python
   df = pd.DataFrame()
   df['Nombre'] = ['Ana', 'Luis', 'Carlos']
   df['Edad'] = [23, 25, 22]
   df['Ciudad'] = ['Madrid', 'Barcelona', 'Valencia']
   ```

---

### 3. Selección e Indexación de Datos

#### Selección en Series

1. Acceder a un valor específico:
   ```python
   serie[0]  # Primer elemento de la serie
   ```

#### Selección en DataFrames

1. Acceder a una columna:
   ```python
   df['Nombre']
   ```

2. Acceder a una fila usando `loc[]` (por etiqueta) o `iloc[]` (por posición):
   ```python
   df.loc[0]   # Primera fila por etiqueta
   df.iloc[0]  # Primera fila por posición
   ```

---

### 4. Manipulación de Datos Faltantes

1. **Identificar datos nulos:**
   ```python
   df.isnull()
   ```

2. **Eliminar filas con valores nulos:**
   ```python
   df.dropna()
   ```

3. **Rellenar valores faltantes:**
   ```python
   df.fillna(0)
   ```

---

## Módulo 2: Operaciones con Datos

### 1. Métodos de Agregación y Resumen

1. **Suma y promedio:**
   ```python
   df['Ventas'].sum()   # Suma total
   df['Ventas'].mean()  # Promedio
   ```

2. **Agrupación con `groupby()`:**
   ```python
   df.groupby('Producto')['Ventas'].sum()  # Agrupar por producto y sumar ventas
   ```

3. **Tabla dinámica con `pivot_table()`:**
   ```python
   df.pivot_table(values='Ventas', index='Producto', columns='Cantidad', aggfunc='sum')
   ```

---

### 2. Operaciones con Columnas y Filas

1. **Crear una nueva columna:**
   ```python
   df['Ingresos'] = df['Ventas'] * df['Cantidad']
   ```

2. **Aplicar funciones con `apply()`:**
   ```python
   df['Ventas_k'] = df['Ventas'].apply(lambda x: x / 1000)
   ```

3. **Asignar valores con `map()`:**
   ```python
   precios = {'A': 10, 'B': 15, 'C': 20}
   df['Precio'] = df['Producto'].map(precios)
   ```

---

### 3. Combinación y Fusión de DataFrames

1. **Fusión con `merge()`:**
   ```python
   df_combinado = pd.merge(df, productos, on='Producto')
   ```

2. **Concatenación con `concat()`:**
   ```python
   df_concatenado = pd.concat([df, ventas_adicionales], ignore_index=True)
   ```

---

## Pandas Cheatsheet

| **Descripción**                          | **Comando**                                               |
|------------------------------------------|----------------------------------------------------------|
| Crear una Serie desde una lista         | `pd.Series([lista])`                                     |
| Crear una Serie desde un diccionario    | `pd.Series({diccionario})`                               |
| Crear una Serie con valor escalar       | `pd.Series(valor_escalar, index=[índice])`              |
| Crear un DataFrame desde un diccionario de listas | `pd.DataFrame({diccionario de listas})`       |
| Crear un DataFrame desde una lista de diccionarios | `pd.DataFrame([lista de diccionarios])`         |
| Acceder a columnas                       | `df['columna']`                                         |
| Acceder a filas (por etiqueta)          | `df.loc[]`                                              |
| Acceder a filas (por posición)          | `df.iloc[]`                                             |
| Identificar datos nulos                 | `df.isnull()`                                           |
| Eliminar filas con datos nulos          | `df.dropna()`                                          |
| Rellenar valores faltantes               | `df.fillna(valor)`                                      |
| Agrupar datos                           | `df.groupby('columna')`                                 |
| Crear tabla dinámica                     | `df.pivot_table()`                                      |
| Fusionar DataFrames                      | `pd.merge()`                                           |
| Concatenar DataFrames                    | `pd.concat()`                                           |

