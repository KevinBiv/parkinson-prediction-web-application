import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import os



def prediction(a,b,c,d,e,f,g):
    
    park = pd.read_csv('parkinson1.csv')
    X=park.drop (columns=['status'])
    y=park['status']
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

    model=DecisionTreeClassifier()
    model.fit(X_train,y_train)

    md=model.predict([[a,b,c,d,e,f,g]])
    return md


    




