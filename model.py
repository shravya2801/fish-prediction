# -*- coding: utf-8 -*-
"""model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MgMhoYS9CQUlYXXfI8gykM9y4voUfMKK
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('Fish.csv')
dataset.to_numpy()

final_df=dataset.drop(['Species'],axis=1)
X=final_df.drop(['Weight'],axis=1)
y=final_df['Weight']

from sklearn import linear_model

model=linear_model.LinearRegression()
model.fit(X,y)

# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[27.6, 30,35.1,14.0049, 4.8438]]))