from URLfeature import FeatureExtraction
import numpy as np
import pickle

file = open("model.pkl","rb")
gbc = pickle.load(file)

url = "https://www.twitch.tv/wtcn"
obj = FeatureExtraction(url)

print(obj.getFeaturesList())

x = np.array(obj.getFeaturesList()).reshape(1,30) 

y_pred =gbc.predict(x)[0]
#1 is safe       
#-1 is unsafe
y_pro_phishing = gbc.predict_proba(x)[0,0]
y_pro_non_phishing = gbc.predict_proba(x)[0,1]
# if(y_pred ==1 ):
pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)