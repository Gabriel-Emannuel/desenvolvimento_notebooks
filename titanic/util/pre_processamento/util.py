import pandas as pd
from sklearn.base import TransformerMixin

class CategorizarParaDummies(TransformerMixin):
    def __init__(self) -> None:
        super().__init__()

    def fit(self, 
            X: pd.DataFrame, 
            y: None = None) -> pd.DataFrame:
        return self

    def transform(self, 
                  X: pd.DataFrame,
                  y: None = None) -> pd.DataFrame:
        X['faixa_etaria'] =  X['Age'].apply(func=definir_faixa_etaria)
        X['Pclass'].replace(to_replace=[1,2,3],
                            value=['alta', 'media', 'baixa'],
                            inplace=True)
        return X  

class DroparColunas(TransformerMixin):
    def __init__(self, colunas: list[str]) -> None:
        super().__init__()
        self.__colunas = colunas

    def fit(self, 
            X: pd.DataFrame, 
            y: None = None) -> pd.DataFrame:
        return self

    def transform(self, 
                  X: pd.DataFrame,
                  y: None = None) -> pd.DataFrame:
        return X.drop(columns=self.__colunas)

class GerarDummies(TransformerMixin):
    def __init__(self) -> None:
        super().__init__()

    def fit(self, 
            X: pd.DataFrame, 
            y: None = None) -> pd.DataFrame:
        return self

    def transform(self, 
                  X: pd.DataFrame,
                  y: None = None) -> pd.DataFrame:
        return pd.get_dummies(X)
    
def definir_faixa_etaria(idade: int | None) -> str:
        if 12 >= idade >= 0:
            return 'criança'
        elif 21 >= idade > 12:
            return 'adolescente'
        elif 60 >= idade > 21:
            return 'adulto'
        elif idade > 60:
            return 'idoso'
        return 'NA'