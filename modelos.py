# Importar librerias necesarias
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC

# Leemos la data de rating

ratings = pd.read_csv("streamlit/ratings.csv")

# Separamos la data para entrenar

X = ratings.data
y = ratings.target

# Separar la data en train y test

x_train, x_test, y_train, y_test = train_test_split(X, y)

# Inicializar modelos

reg_lin = LinearRegression()
reg_log = LogisticRegression()
svc_reg = SVC()

# Entrenar los modelos

lin_regr = reg_lin.fit(x_train, y_train)
log_regr = reg_log.fit(x_train, y_train)
svc_regr = svc_reg.fit(x_train, y_train)

"""
Agrupar por categoria
utilizar funcion cat de pandas
regresion logistica
"""
