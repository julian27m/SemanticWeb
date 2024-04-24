import pandas as pd

'''
Este script lo utilizamos para generar dataframes de pruebas
'''

def main():
    csv_path = 'Entrega2/CSVs/metadatos.csv'

    df = pd.read_csv(csv_path)

    primeras_cinco_filas = df.head()

    nuevo_csv_path = 'test.csv'
    primeras_cinco_filas.to_csv(nuevo_csv_path, index=False)

    print("Archivo guardado:", nuevo_csv_path)

if __name__ == "__main__":
    main()
