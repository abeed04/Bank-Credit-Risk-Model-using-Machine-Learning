import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection  import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('Clean_Bank_Data')

label_encoder = LabelEncoder()
df['Approved_Flag'] = label_encoder.fit_transform(df['Approved_Flag'])

y = df['Approved_Flag']
x = df.drop(['Approved_Flag'],axis=1)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=786)

model = DecisionTreeClassifier(criterion='gini',splitter='best', max_depth=25)
model.fit(x_train,y_train)
y_pred= model.predict(x_test)

pickle.dump(model,open('model.pkl','wb'))