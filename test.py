import pickle
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# loaded_model = pickle.load(open("XGBoostClassifier.pickle.dat", "rb"))

data0 = pd.read_csv('DataFiles/5.urldata.csv')
data = data0.drop(['Domain'], axis = 1).copy()
y = data['Label']
X = data.drop('Label',axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)

xgb = XGBClassifier(learning_rate=0.4,max_depth=7)
xgb.fit(X_train, y_train)

_, X_test, __, y_test = train_test_split(X, y, test_size = 0.2, random_state = 10)

y_test_xgb = xgb.predict(X_test)
y_train_xgb = xgb.predict(X_train)

acc_train_xgb = accuracy_score(y_train,y_train_xgb)
acc_test_xgb = accuracy_score(y_test,y_test_xgb)

print("XGBoost: Accuracy on training Data: {:.3f}".format(acc_train_xgb))
print("XGBoost : Accuracy on test Data: {:.3f}".format(acc_test_xgb))