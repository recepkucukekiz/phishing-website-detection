from URLcompute import UrlCompute
import pickle
import pandas as pd

model = pickle.load(open("alpha/XGBoostClassifier.pickle.dat", "rb"))

#url = "https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwi89567w8L6AhUzj2gJHZqWC84YABAAGgJ3Zg&ohost=www.google.com&cid=CAESbeD2O1JTWXX1AZkgmEIG_1Ywz1zaveS7cjPzuEwJRylyniJcIroEc9PgqsI7b4QVUM5onCrILgY89HsUGD3Ky9RP4KXl6gXFl5lbGYJtxdPWVSlg9NmvJ62UQZEgbln_Am8FU975He5vJLkNgG0&sig=AOD64_1sfBniFbuuafZbiTywkGtP8FpuoA&q&adurl&ved=2ahUKEwilxpa7w8L6AhXPRvEDHWb5DxUQ0Qx6BAgGEAE"
url = "https://www.google.com"
print("url:", url)

obj = UrlCompute(url)
computed = obj.getFeaturesList()
print(computed)

computed.pop(0)
print(computed)

x = pd.DataFrame([computed], columns=['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
                      'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 
                      'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards'])
print(x)


result = model.predict(x)
print(result)
# print("result:" , str(result[0]))

# if result == 0:
#     print("SAFE")
# else:
#     print("PHISHING")
