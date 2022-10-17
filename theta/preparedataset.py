#importing required packages for this module
import pandas as pd

#loading the phishing URLs data to dataframe
data0 = pd.read_csv("online-valid.csv")
data0.head()

data0.shape

#Collecting 5,000 Phishing URLs randomly
phishurl = data0.sample(n = 5000, random_state = 12).copy()
phishurl = phishurl.reset_index(drop=True)
phishurl.head()

phishurl.shape

#Loading legitimate files 
data1 = pd.read_csv("Benign_list_big_final.csv")
data1.columns = ['URLs']
data1.head()

#Collecting 5,000 Legitimate URLs randomly
legiurl = data1.sample(n = 5000, random_state = 12).copy()
legiurl = legiurl.reset_index(drop=True)
legiurl.head()

legiurl.shape

