import pandas
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from name_banker import NameBanker
from random_banker import RandomBanker

## Set up for dataset
features = ['checking account balance', 'duration', 'credit history',
            'purpose', 'amount', 'savings', 'employment', 'installment',
            'marital status', 'other debtors', 'residence time',
            'property', 'age', 'other installments', 'housing', 'credits',
            'job', 'persons', 'phone', 'foreign']
target = 'repaid'

df = pandas.read_csv('c:/git/ml-society-science/data/credit/german.data', sep=' ',
                     names=features+[target])


numerical_features = ['duration', 'age', 'residence time', 'installment', 'amount', 'duration', 'persons', 'credits']

quantitative_features = list(filter(lambda x: x not in numerical_features, features))

X = pandas.get_dummies(df, columns=quantitative_features, drop_first=True)

encoded_features = list(filter(lambda x: x != target, X.columns))

y = df["repaid"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

nb = NameBanker()
nb.fit(X_train, y_train)
nb.set_interest_rate(0.005)

#nb.model.predict_proba(X_test)[:,0]
#nb.model.predict(X_test)

#nb.model
# nb.predict_proba(X_test)
in_a = pandas.DataFrame(X_test.iloc[75]).T

print(in_a)

a = nb.predict_proba(in_a)

print("Prediction", nb.prediction, type(nb.prediction))
print("predict_proba", a, type(a))










