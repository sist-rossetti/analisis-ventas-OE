# AVR-2: Script de análisis de ventas
# Autor: Carolina Jennifer Rossetti
# Descripción: Importa el dataset de ventas, calcula indicadores clave
# y genera un gráfico de evolución mensual de ventas.

import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('datos/ventas.csv')
df['sales_date'] = pd.to_datetime(df['sales_date'])

ventas_totales = df['sales_amount'].sum()
promedio_diario = df['sales_amount'].mean()
venta_max = df['sales_amount'].max()
venta_min = df['sales_amount'].min()

print('=== INDICADORES DE VENTAS ===')
print(f'Ventas totales:    ${ventas_totales:,.2f}')
print(f'Promedio diario:   ${promedio_diario:,.2f}')
print(f'Venta máxima:      ${venta_max:,.2f}')
print(f'Venta mínima:      ${venta_min:,.2f}')

df['mes'] = df['sales_date'].dt.to_period('M')
ventas_por_mes = df.groupby('mes')['sales_amount'].sum()

print('\n=== VENTAS POR MES ===')
print(ventas_por_mes.to_string())

fig, ax = plt.subplots(figsize=(10, 5))
ventas_por_mes.plot(kind='bar', ax=ax, color='steelblue', edgecolor='white')
ax.set_title('Evolución Mensual de Ventas', fontsize=14, fontweight='bold')
ax.set_xlabel('Mes')
ax.set_ylabel('Monto de Ventas ($)')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()

os.makedirs('resultados', exist_ok=True)
plt.savefig('resultados/grafico_ventas.png', dpi=150)
plt.show()
print('Gráfico guardado en resultados/grafico_ventas.png')
