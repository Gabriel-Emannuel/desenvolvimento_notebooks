# Pré-processamento para Classificação

* As informações identificadas como úteis são:
    1. Gênero;
    2. Classe Social;
    3. Idade;

* A partir destas informações, o pré processamento irá realizar os seguintes passos:

1. Categorizar as informações, A classe Social se tornará uma coluna categórica, além que será criada uma coluna de faixa etária, que categorizará as idades;

2. Retirar as colunas não importantes;

3. Gerar Colunas Dummies* das colunas categóricas;
    * Coluna Dummie significa uma coluna que apenas contenha True e False, representando a validade da característica da coluna, por exemplo o "é mulher", significaria que representaria se o indivíduo da linha fosse uma mulher.

4. Retirar colunas que repetem informações, por exemplo uma coluna que diz "é mulher" e outra "é homem", como uma é o espelho da outra, pode ocorrer a retirada;

5. Preencher Valores Ausentes;

6. Normaliza os Valores, para as diferentes escalas e intervalos não criar distorções no momento de gerar features.