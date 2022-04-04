import pandas as pd

# needed for spliting data into train and test data
from sklearn.model_selection import train_test_split
# needed for using logistic Regression model
from sklearn.linear_model import LogisticRegression

# dataframe variable/read excel file
df = pd.read_excel("/autograder/source/bankmarketing.xlsx")

# remove column y
x = df.drop('y',axis=1)

# since job, marital, edu, default, house, loan columns are categorical columns, we need to changed them to 
# dummy variables so they can used to do analysis
x = pd.get_dummies(x, prefix=['job', 'marital', 'edu', 'default', 'house', 'loan'],drop_first=True)

# form a dataframe only containing column y
y = df.y

# variables to store training and test data
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2,random_state=20)

# Create a LogisticRegression object instance and name it log_model
log_model = LogisticRegression(solver="liblinear")
# Perform logistic regression using the fit method with the training data
log_model.fit(x_train,y_train)

# Obtain predicted y values
predicted_y = log_model.predict(x_test)

# Return the mean accuracy
mod_score = log_model.score(x_test, y_test)

