import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.experimental.enable_iterative_imputer import IterativeImputer

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
    
class Normalizador(TransformerMixin):
    def __init__(self) -> None:
        super().__init__()
        self.__normalizador = StandardScaler()

    def fit(self, 
            X: pd.DataFrame, 
            y: None = None) -> pd.DataFrame:    
        self.__normalizador.fit(X)
        return self

    def transform(self, 
                  X: pd.DataFrame,
                  y: None = None) -> pd.DataFrame:
        X_transformado = pd.DataFrame(self.__normalizador.transform(X))
        manter_colunas_nomes(X.columns, X_transformado)
        X_transformado.index = X.index
        return X_transformado
    
class PreencherValoresVazios(TransformerMixin):
    def __init__(self) -> None:
        super().__init__()
        self.__preenche = IterativeImputer()
    
    def fit(self,
            X: pd.DataFrame,
            y: None = None) -> pd.DataFrame:
        self.__preenche.fit(X)
        return self
    
    def transform(self,
                  X: pd.DataFrame,
                  y: None = None) -> pd.DataFrame:
        X_transformado = pd.DataFrame(self.__preenche.transform(X))
        manter_colunas_nomes(X.columns, X_transformado)
        X_transformado.index = X.index
        return X_transformado
    
def manter_colunas_nomes(colunas_originais: np.ndarray,
                         X_transformado: pd.DataFrame):
    for index_coluna in range(colunas_originais.shape[0]):
        X_transformado.rename(columns={
            index_coluna: colunas_originais[index_coluna]
        }, inplace=True)

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