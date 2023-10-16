from sklearn.experimental.enable_iterative_imputer import IterativeImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from util.pre_processamento.util import (
    CategorizarParaDummies,
    DroparColunas,
    GerarDummies
)

pre_processador = Pipeline(steps=[
    ('Categorizar Para Dummies', CategorizarParaDummies()),
    ('Dropar Colunas sem função para classificação', DroparColunas(colunas=[
        'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin'
        ])),
    ('Gerar Dummies', GerarDummies()),
    ('Dropar Colunas Dummies Sem função', DroparColunas(colunas=[
        'Sex_male', 'faixa_etaria_NA'
    ])),
    ('Imputando valores ausentes', IterativeImputer()),
    ('Normalizando Valores', StandardScaler())
])