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




