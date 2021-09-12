from crossvalidation import split_dataset
from arff import to_arff, get_attributes_types
from preprocessing import normalize
import pandas as pd


def main():
    # TODO: Falta rellenar la informacion sobre las k particiones y el nombre de la columna clasificadora
    dataset = 'data.csv'
    k = 5  # FIXME:
    class_col = 'num_imgs'  # FIXME:

    # Lectura de dataset original. Ya debe tener la columna clase
    print('Lectura de dataset...')
    df = pd.read_csv(dataset, skipinitialspace=True)

    # Normalizacion del df. Elimina las columnas con one hot encoding (surge nuevas columnas weekday y channel)
    # NOTA: Dura algunos segundos...
    print('Inicio de normalizacion (Dura algunos segundos)...')
    normalized_df = normalize(df)

    # Organiza las particiones y retorna una lista de tuplas [DataFrame traing, DataFrame test]
    print('Generacion de particiones...')
    validation_steps = split_dataset(normalized_df, k=k, class_col=class_col)

    print('Escritura de particiones...')
    attrs_description = get_attributes_types(df)
    for index, (df_train, df_test) in enumerate(validation_steps):
        to_arff(f'train_{index}.arff', df_train, attrs_description, 'News')
        to_arff(f'test_{index}.arff', df_test, attrs_description, 'News')


if __name__ == '__main__':
    main()
