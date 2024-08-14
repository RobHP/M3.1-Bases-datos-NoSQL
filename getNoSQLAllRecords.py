import requests
import pandas as pd
import json

# URL de la API
url = 'https://66b4e5289f9169621ea4c29e.mockapi.io/api/v1/Contactos'

# Realizar la solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()

    # Mostrar los datos en formato JSON formateado
    print("Datos en formato JSON:")
    print(json.dumps(data, indent=4))

    # Convertir los datos a un DataFrame de pandas
    df = pd.DataFrame(data)

    # Mostrar el DataFrame
    print("\nDatos en formato DataFrame:")
    print(df)

    # Exportar los datos a un archivo CSV
    csv_file = 'contactos.csv'
    df.to_csv(csv_file, index=False)

    print(f"\nDatos exportados correctamente a {csv_file}")
else:
    print(f"Error al consultar la API. Código de estado: {response.status_code}")
