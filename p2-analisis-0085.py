# importar librerias
import pandas as pd
import numpy as np

print("Selección y Filtrado de Vehículos (Filtrado / Regresión) Ricardo Lopez NC = 0085")

vehiculos = {
    "Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Coupe Sport"],
    "Tipo_Motor": ["Gasolina", "Hibrido", "Gasolina", "Diesel", "Electrico", "Gasolina"],
    "Autonomia_Km": [600, 800, 550, 700, 450, 500],
    "Precio_USD": [22000, 35000, 18000, 45000, 32000, 41000]
}

df = pd.DataFrame(vehiculos)

print("\n--- DataFrame Original ---")
print(df)

print("\n+-+-+-+- Agrupar por Tipo de Motor -+-+-+-+")
# Agrupamos por Tipo_Motor para analizar la autonomía y el precio según el motor
agrupado = df.groupby("Tipo_Motor")

print("\n+-+-+-+- Por agregación: Promedios -+-+-+-+")
# Calculamos el promedio de las columnas numéricas (Autonomía y Precio)
print(agrupado[['Autonomia_Km', 'Precio_USD']].mean())

print("\n+-+-+-+- Por agregación: Máximos -+-+-+-+")
# Calculamos el valor máximo de las columnas numéricas por tipo de motor
print(agrupado[['Autonomia_Km', 'Precio_USD']].max())

print("\n Ricardo----Segunda Parte-----0085")
print("agregaciones multiples")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")

# CORRECCIÓN 1: Se cambió "Modelo" por "Precio_USD" (no se puede sacar promedio/suma a textos) 
# y se corrigió el error de dedo "sun" por "sum".
resultado_agregado = agrupado["Precio_USD"].agg(["mean", "sum", "max", "min"])
print(resultado_agregado)

print("\nAgrupacion por varias columnas")
print("agrega columna al DataFrame")

# CORRECCIÓN 2: Se cambió el nombre a la columna de "team" a "equipo" para que coincida abajo.
df["equipo"] = ["A", "B", "A", "B", "A", "B"]

# CORRECCIÓN 3: Se eliminaron los espacios en blanco de los nombres de las columnas, 
# se usó "equipo" en lugar de "equipo " y se cambió "veces" por una columna numérica real ("Autonomia_Km").
agrupado_multiple = df.groupby(["Modelo", "equipo"])["Autonomia_Km"].mean()
print(agrupado_multiple)
