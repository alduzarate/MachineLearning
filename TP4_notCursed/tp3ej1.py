import tp0
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

def obtainBayesDimData():
    # Valores de d
    d_iterable = [2, 4, 8, 16, 32]

    # Datos a guardar pedidos
    train_errors_d = []
    test_errors_d = []

    train_errors_p = []
    test_errors_p = []

    # Guardo la dimension que va teniendo d para poder armar el dataframe a la hora de analizar
    dimensions = []

    for d in d_iterable:
        # Conjuntos de test
        # Diagonal
        d_test = tp0.generate_dataframe_ej_a(d, 10000, 0.78)
        cols = range(0, d)
        X_d_test = d_test[cols]
        y_d_test = d_test['Clase']

        # Paralelo
        p_test = tp0.generate_dataframe_ej_b(d, 10000, 0.78)
        X_p_test = p_test[cols]
        y_p_test = p_test['Clase']
        
        for i in range(0,20):
            # Longitud del conjunto de entrenamiento
            dimensions.append(d)

            # Conjuntos de entrenamiento diagonal
            train_set_d = tp0.generate_dataframe_ej_a(d, 250, 0.78)
            X_d_train = train_set_d[cols]
            y_d_train = train_set_d['Clase']

            # Conjuntos de entrenamiento paralelo
            train_set_p = tp0.generate_dataframe_ej_b(d, 250, 0.78)
            X_p_train = train_set_p[cols]
            y_p_train = train_set_p['Clase']

            # Modelos y entrenamiento diagonal
            clf_d = GaussianNB()
            clf_d.fit(X_d_train, y_d_train)

            # Modelos y entrenamiento paralelo
            clf_p = GaussianNB()
            clf_p.fit(X_p_train, y_p_train)

            # Probamos sobre los conjuntos de testeo
            predicted_d = clf_d.predict(d_test[cols])
            predicted_p = clf_p.predict(p_test[cols])

            # Guardamos errores sobre el conjunto de entrenamiento y de testeo.
            # Error = 1 - accuracy
            train_errors_d.append(1 - accuracy_score(y_d_train, clf_d.predict(X_d_train)))
            test_errors_d.append(1 - accuracy_score(y_d_test, predicted_d))

            train_errors_p.append(1 - accuracy_score(y_p_train, clf_p.predict(X_p_train)))
            test_errors_p.append(1 - accuracy_score(y_p_test, predicted_p))

    # Armo dataframe con los datos colectados anteriormente
    temp_dataframe_d = pd.DataFrame({})
    temp_dataframe_d['D'] = dimensions
    temp_dataframe_d['TrainError'] = train_errors_d
    temp_dataframe_d['TestError'] = test_errors_d

    temp_dataframe_p = pd.DataFrame({})
    temp_dataframe_p['D'] = dimensions
    temp_dataframe_p['TrainError'] = train_errors_p
    temp_dataframe_p['TestError'] = test_errors_p

    # Dataframes finales a usar para la gráfica
    df_errors_d = pd.DataFrame({})
    df_errors_d['Dimension'] = d_iterable
    df_errors_d['TrainError'] = temp_dataframe_d.groupby('D')['TrainError'].mean().to_numpy()
    df_errors_d['TestError'] = temp_dataframe_d.groupby('D')['TestError'].mean().to_numpy()

    df_errors_p = pd.DataFrame({})
    df_errors_p['Dimension'] = d_iterable
    df_errors_p['TrainError'] = temp_dataframe_p.groupby('D')['TrainError'].mean().to_numpy()
    df_errors_p['TestError'] = temp_dataframe_p.groupby('D')['TestError'].mean().to_numpy()

    return df_errors_d, df_errors_p