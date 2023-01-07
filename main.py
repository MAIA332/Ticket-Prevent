import numpy as np, os, sys, time, pandas as pd, pickle,logging,json
from tqdm.notebook import tqdm_notebook
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from random import randint
from yahooquery import Ticker
import plotly.graph_objs as go
import plotly.offline as py
import plotly

class prevent_st:

    def __init__(self,x_train,y_train,x_test,y_test,features,features_scale,labels,data_preg,res,qtd_linha_teste,qtd_linha,scaler):
        
        lr = LinearRegression()
        lr.fit(x_train, y_train)

        #==========================================================================
        
        #valor_novo = features.tail(1)
        
        previsao =  features_scale[qtd_linha_teste:qtd_linha] #scaler.transform(valor_novo)
        pred = lr.predict(previsao)
        """ 
        print(pred) 
        print(features.tail(1)) """

        self.sec_frame =  pd.DataFrame({'data_pregao':data_preg,'real':res,'previsao':pred})

        self.sec_frame['real'] = self.sec_frame['real'].shift(+1)

        self.sec_frame.set_index('data_pregao',inplace=True)

        print(self.sec_frame)
        self.accureance_graph() 
        os.system('pause')

    def m_f(self,features_list,labels,features):

        k_best_features = SelectKBest(k='all')
        k_best_features.fit_transform(features,labels)
        k_best_features_scores = k_best_features.scores_
        raw_pairs =  zip(features_list[1:], k_best_features_scores)
        ordered_pairs = list(reversed(sorted(raw_pairs, key=lambda x:x[1])))

        k_best_features_final = dict(ordered_pairs[:15])
        best_features = k_best_features_final.keys()

        print('')
        print('melhores features')
        print(k_best_features_final)
        print(best_features)

    def linear_regression_coef_test(self,x_train,y_train,x_test,y_test):
        
        lr = LinearRegression()
        lr.fit(x_train, y_train)
        pred = lr.predict(x_test)

        cd = r2_score(y_test,pred)

        print(f'Coeficiente de determinação: {cd * 100:.2f}')

    def accureance_graph(self):
        
        plt.figure(figsize=(16,8))
        plt.title('Preço das ações')
        plt.plot(self.sec_frame['real'],label='real',color='blue',marker='o' )
        plt.plot(self.sec_frame['previsao'],label='previsão',color='red',marker='o')
        plt.xlabel('Data pregão')
        plt.ylabel('Preço de fechamento')
        plt.legend()
        plt.show()
   


def Main_exec(ticker):
        
    str_op = ticker + '.SA'
    ticker_scrapp = Ticker(str_op)                             # extrai os dados e coloca num dataframe
    frame = pd.DataFrame(ticker_scrapp.history(period='max'))

    frame = frame.droplevel('symbol')

    frame['Date']= pd.to_datetime(frame.index.get_level_values(0)) #inclui os dados da indexação em um campo data convertido em datetime

    frame['variation'] = frame['close'].sub(frame['open']) #cria o campo variation, que contém a variação do preço

    frame['mm5d'] = frame['close'].rolling(5).mean() # cria um campo da media de 5 dias
    frame['mm21d'] = frame['close'].rolling(21).mean() # cria um campo da media de 21 dias

    frame['close'] = frame['close'].shift(-1) #baseado na prevenção de um dia após a exec. pula os dados de hoje para um dia atrás

    frame.dropna(inplace=True) #exclui dados nulos

    qtd_linha = len(frame)

    qtd_linha_treino = qtd_linha - 700
    qtd_linha_teste = qtd_linha - 15            #definição da separação do dataset

    qtd_linha_valiidacao = qtd_linha - qtd_linha_teste

    frame = frame.reset_index(drop=True)        #resetando a indexação

    features = frame.drop(['Date','close','adjclose','dividends','low','mm21d'],1)# definindo as features (baseado na seleção feita mais abaixo)
    labels = frame['close']
            
    
    features_list = ('open','volume','mm5d','mm21d','high','low','variation')

    #self.m_f(features_list,labels,features) -- define as melhores features 

    scaler = MinMaxScaler().fit(features)
    features_scale = scaler.transform(features)

    #print('Features: ', features_scale.shape)   # normalizando os dados de entrada(features)
    #print(features_scale)

    x_train = features_scale[:qtd_linha_treino]
    x_test = features_scale[qtd_linha_treino:qtd_linha_teste]

    y_train = labels[:qtd_linha_treino]         #separando em dados de treino e dados de teste
    y_test =labels[qtd_linha_treino:qtd_linha_teste]

    #self.linear_regression_coef_test(x_train,y_train,x_test,y_test) coef det = 95.47

    #print(len(x_train), len(y_train))
    #print(len(x_test),len(y_test))

    #print(frame.tail())


    data_preg_full = frame['Date']
    data_preg = data_preg_full[qtd_linha_teste:qtd_linha]

    res_full = frame['close']
    res = res_full[qtd_linha_teste:qtd_linha]

    prevent_st(x_train,y_train,x_test,y_test,features,features_scale,labels,data_preg,res,qtd_linha_teste,qtd_linha,scaler)
        
Main_exec('ENAT3')