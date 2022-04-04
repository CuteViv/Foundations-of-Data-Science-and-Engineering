import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

from statsmodels.formula.api import ols

df = pd.read_excel("bikerental.xlsx")

results_c = ols("casual ~ mnth + holiday + workingday + atemp + hum + windspeed", data=df).fit()

results_r = ols("registered ~ mnth + holiday + workingday + atemp + hum + windspeed", data=df).fit()

c_influencers = df.drop(["casual", "registered", "cnt", "mnth"], axis=1)

r_influencers = df.drop(["casual", "registered", "cnt", "holiday"], axis=1)

x = df.drop(["casual", "registered", "cnt"], axis=1)

y_c = df.casual

y_r = df.registered

x_train_c,x_test_c,y_train_c,y_test_c = train_test_split(x,y_c,test_size=0.2,random_state=20)

x_train_r,x_test_r,y_train_r,y_test_r = train_test_split(x,y_r,test_size=0.2,random_state=20)

bike_mod_c = LinearRegression()
bike_mod_c.fit(x_train_c, y_train_c)

bike_mod_r = LinearRegression()
bike_mod_r.fit(x_train_r, y_train_r)

predicted_y_c = bike_mod_c.predict(x_test_c)
predicted_y_r = bike_mod_r.predict(x_test_r)

