import pandas as pd

# Cargar el archivo XML en un DataFrame de pandas
df = pd.read_xml('archivo.xml')

# Guardar el DataFrame en un archivo Excel
df.to_excel('archivo.xlsx', index=False)
