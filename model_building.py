# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:53:16 2020

@author: errakho mohammed
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("../input/developer-data/software_enginners_data_cleaned.csv",engine = "python")
print(df.columns)

col_model = df[['Job Title', 'Salary Estimate', 'Job Description', 'Rating',
              'Company Name', 'Location', 'Size','Type of ownership', 'Industry', 
              'Sector', 'Revenue','Per Hour', 'avr_salary' ,'javascript','html', 
              'css', 'react', 'angular', 'git', 'node', 'php', 'mysql',
              'j2ee', 'net', 'new', 'Remote', 'State', 'age']]
col_model.dropna(inplace = True)
new_df = pd.get_dummies(col_model)
#print(new_df.isnull().sum())

X = new_df.drop("avr_salary", axis = 1)
Y = new_df.avr_salary.values
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

reg = LinearRegression()
reg.fit(X_train, y_train)

np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 4))

reg_1 = Lasso(alpha=.13)
reg_1.fit(X_train,y_train)
np.mean(cross_val_score(reg_1,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 4))

rf = RandomForestRegressor()
np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 4))

# tune models GridsearchCV 
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}
gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)

# best scores
gs.best_score_
gs.best_estimator_


pred_reg = reg.predict(X_test)
pred_reg_1 = reg_1.predict(X_test)

mean_absolute_error(y_test,pred_reg)
mean_absolute_error(y_test,pred_reg_1)