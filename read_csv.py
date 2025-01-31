import csv
import matplotlib.pyplot as plt

# Ruta al archivo CSV
archivo_csv = 'stream.csv'

# Inicializar variables
total_views = 0
conteo = 0
views_por_stream = [] 
# Leer el archivo CSV
with open(archivo_csv, mode='r') as archivo:
    lector = csv.reader(archivo)
    next(lector)  # Saltar la cabecera
    for fila in lector:
        # Asumiendo que la media de espectadores está en la segunda columna
        if fila[1]:
            total_views += int(fila[1])
            conteo += 1
            views_por_stream.append(int(fila[1]))

# Calcular la media
media_views = total_views / conteo if conteo else 0
print(f"Media de espectadores: {media_views}")
# Crear un gráfico de barras
plt.bar(range(len(views_por_stream)), views_por_stream, color='blue')
plt.axhline(media_views, color='green', linestyle='--', label=f'Media: {media_views:.2f}')
plt.xlabel('Stream')
plt.ylabel('Espectadores')
plt.title('Espectadores por Stream')
plt.legend()
plt.show()