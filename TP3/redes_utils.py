import numpy as np
import sklearn as sk
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from copy import deepcopy
import matplotlib.pyplot as plt
import tp0
import random
import warnings
warnings.filterwarnings("ignore")

def entrenar_red(red, evaluaciones, X_train, y_train, X_val, y_val, X_test, y_test, error_measure_func):
  best_red = None
  train_errors = []
  val_errors = []
  test_errors = []

  best_train_error = None
  best_val_error = None
  best_test_error = None
  for i in range(evaluaciones):
    red.fit(X_train, y_train)

    # Medimos los errores
    train_error_i = error_measure_func(red.predict(X_train), y_train)
    val_error_i = error_measure_func(red.predict(X_val), y_val)
    test_error_i = error_measure_func(red.predict(X_test), y_test)

    # Chequeo si la red es mejor que la candidata
    if best_val_error is None or val_error_i < best_val_error:
      best_val_error = val_error_i
      best_train_error = train_error_i
      best_test_error = test_error_i
      best_red = deepcopy(red)

    # Guardo los errores registrados en esta evaluacion
    train_errors.append(train_error_i)
    val_errors.append(val_error_i)
    test_errors.append(test_error_i)

  return best_red, train_errors, val_errors, test_errors, best_train_error, best_val_error, best_test_error


def graficar_predicciones(x, y, title):
  df = pd.DataFrame(x)
  df['Clase'] = y
  df.plot(x=0, y=1, kind='scatter', c = 'Clase', colormap='viridis', title = title)