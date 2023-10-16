import pickle
import pandas as pd
from sklearn.pipeline import Pipeline

from util.pre_processamento.pre_processador import pre_processador

with open('../deploys/classificador_weight.pkl', 'rb') as f:
    modelo_final = pickle.load(f)

amostra_treino = pd.read_csv('../datasets/train.csv', index_col=0)
X = amostra_treino.drop(columns='Survived')
pre_processador.fit(X)

classificador = Pipeline(steps=[
    ('Pré Processador', pre_processador),
    ('Classificação', modelo_final)
])