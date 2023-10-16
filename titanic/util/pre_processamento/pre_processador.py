from sklearn.pipeline import Pipeline

from util.pre_processamento.util import (
    CategorizarParaDummies,
    DroparColunas,
    GerarDummies,
    Normalizador,
    PreencherValoresVazios
)

pre_processador = Pipeline(steps=[
    ('Categorizar Para Dummies', CategorizarParaDummies()),
    ('Dropar Colunas sem função para classificação', DroparColunas(colunas=[
        'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'
        ])),
    ('Gerar Dummies', GerarDummies()),
    ('Dropar Colunas Dummies Sem função', DroparColunas(colunas=[
        'Sex_male', 'faixa_etaria_NA'
    ])),
    ('Imputando valores ausentes', PreencherValoresVazios()),
    ('Normalizando Valores', Normalizador())
])