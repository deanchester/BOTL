import numpy as np
import pandas as pd
from sklearn.linear_model import SGDRegressor as SGD
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression as LR
from sklearn.kernel_approximation import RBFSampler as RBF
from sklearn.pipeline import Pipeline

def createPipeline(df,tLabel,DROP_FIELDS):
    model = SGD(loss='squared_epsilon_insensitive',penalty='l2',alpha=0.001,n_iter=1500,epsilon=0.001,learning_rate ='invscaling',warm_start=False,shuffle=False)
    X = df.drop(DROP_FIELDS,axis=1).copy()
    y = df[tLabel].copy()
    X = X.drop(tLabel,axis=1)
    model = model.fit(X,y)
    return model


def initialPredict(df,model,tLabel,DROP_FIELDS):
    X = df.drop(DROP_FIELDS,axis=1).copy()
    X = X.drop(tLabel,axis=1)
    Y = df[tLabel].copy()
    predicted = model.predict(X)
    df['predictions'] = predicted
    return df

def instancePredict(df,idx,model,tLabel,DROP_FIELDS):
    X = df.loc[idx].drop(DROP_FIELDS).copy()
    X = X.drop(tLabel).values.reshape(1,-1)
    Y = df.loc[idx,tLabel].copy()
    predicted = model.predict(X)
    df.loc[idx,'predictions'] = predicted
    return df.loc[idx]


