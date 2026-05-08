import matplotlib.pyplot as plt
import numpy as np


np.random.seed(42)   # para resultados reproduzíveis
horas_estudo = np.random.uniform(1, 10, 30)
notas = horas_estudo * 0.8 + np.random.normal(0, 1, 30)
notas = np.clip(notas, 0, 10)   # limitar entre 0 e 10
 
plt.figure(figsize=(8, 5))
plt.scatter(horas_estudo, notas, color='#8E44AD', alpha=0.7, s=80)
 
plt.title('Horas de Estudo vs Nota Final', fontsize=14)
plt.xlabel('Horas de Estudo por Semana')
plt.ylabel('Nota Final')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
