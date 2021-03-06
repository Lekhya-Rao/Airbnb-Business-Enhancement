 import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pylab
import math
import sklearn
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
# reading datasets
london = pd.read_csv('Final_London_Dataset.csv')
nyc = pd.read_csv('Final_NY_Dataset.csv')
# formatting uniform types for numerical attributes
london['no_of_amenities'] = london['no_of_amenities'].astype(float)
london['accommodates'] = london['accommodates'].astype(float)
london['bedrooms'] = london['bedrooms'].astype(float)
london['beds'] = london['beds'].astype(float)
london['cluster'] = london['cluster'].astype(float)
london['host_response_rate'] = london['host_response_rate'].astype(float)
london['host_acceptance_rate'] = london['host_acceptance_rate'].astype(float)
nyc['no_of_amenities'] = nyc['no_of_amenities'].astype(float)
nyc['accommodates'] = nyc['accommodates'].astype(float)
nyc['bedrooms'] = nyc['bedrooms'].astype(float)
nyc['beds'] = nyc['beds'].astype(float)
nyc['cluster'] = nyc['cluster'].astype(float)
nyc['host_response_rate'] = nyc['host_response_rate'].astype(float)
nyc['host_acceptance_rate'] = nyc['host_acceptance_rate'].astype(float)
# preparing regression model
from sklearn.model_selection import train_test_split

reg = linear_model.LinearRegression()
reg1 = linear_model.LinearRegression()
# dividing datasets into training and test sets
# 'host_response_rate'
# 'host_acceptance_rate',
lx_train, lx_test, ly_train, ly_test = train_test_split(london[['no_of_amenities', 'accommodates', 'bedrooms', 'beds',
                                                        'cluster', 'host_response_rate', 'host_acceptance_rate']], london.price,
                                                        test_size=0.3, random_state=0)
nx_train, nx_test, ny_train, ny_test = train_test_split(nyc[['no_of_amenities', 'accommodates', 'bedrooms', 'beds',
                                                             'cluster', 'host_response_rate', 'host_acceptance_rate']],
                                                       nyc.price, test_size=0.3, random_state=0)
# building regression model
reg.fit(lx_train, ly_train)
reg1.fit(nx_train, ny_train)
# predicting values
l_pred = reg.predict(lx_test)
n_pred = reg1.predict(nx_test)
# computing r^2 score for regression model
print('london', reg.score(lx_test, ly_test))
print('nyc', reg.score(nx_test, ny_test))

# computing MSE for regression model

mse = sklearn.metrics.mean_squared_error(ly_test, l_pred)
math.sqrt(mse)
print(mse, math.sqrt(mse))

def mape(actual, predicted):
    return np.mean(np.abs((actual-predicted)/actual)) * 100


result = mape(ly_test, l_pred)
result1 = mape(ny_test, n_pred)
print("MAPE: London ", result)
print("MAPE: New York ", result1)