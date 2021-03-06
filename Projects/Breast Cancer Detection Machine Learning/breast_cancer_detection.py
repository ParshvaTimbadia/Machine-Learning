# -*- coding: utf-8 -*-
"""Breast Cancer Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EyiMPe8a5z2Bipkm_RdRNKnG0vqeneim
"""

#Imporing the Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#importing the Dataset 

dataset = pd.read_csv('data.csv')
dataset.head()

dataset.describe()

dataset.shape

#Checking for the missing value in our dataset.
dataset.isna().sum()

#Now we can see that there is not data in the last Unmaed Column. So we will drop that.

dataset =dataset.dropna(axis=1)
dataset.head()

dataset['diagnosis'].value_counts()

sns.countplot(x= dataset['diagnosis'])

dataset.dtypes

#Encoding the categorical Data

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dataset.iloc[:, 1]=le.fit_transform(dataset.iloc[:,1].values)


dataset.head()

#Creating a PAir Plot 

sns.pairplot(dataset.iloc[:,1:6], hue='diagnosis')

#Lets Understand Correlations

dataset.iloc[:, 1:12].corr()

#Visualize the Correlation
plt.figure(figsize=(10,10))
sns.heatmap(dataset.iloc[:,1:12].corr(), annot=True, fmt='.0%')

#Spliting Data into Independent and Dependent

x= dataset.iloc[:, 2:].values
y= dataset.iloc[:, 1].values

#Spliting the DataSet into Training Set and Test Set

x_train, x_test, y_train , y_test= train_test_split(x, y, test_size=0.25, random_state=0)

#Feature Scaling the Data

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

#Creating the Classification Models

def models(x_train, y_train):

  #Logistic Regression:
  Logistic_classifier= LogisticRegression(random_state=0)
  Logistic_classifier.fit(x_train, y_train)

  #Decision Tree:
  tree_classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
  tree_classifier.fit(x_train, y_train)

  #Random Forest:
  forest_classifier= RandomForestClassifier(n_estimators=10 ,criterion='entropy', random_state=0)
  forest_classifier.fit(x_train,y_train)

  #Accuracy:
  print("Logistic Regression Accuracy:", Logistic_classifier.score(x_train, y_train))
  print("Decision Tree Classifier Accuracy:", tree_classifier.score(x_train, y_train))
  print("Random Forest Classifier Accuracy:", forest_classifier.score(x_train, y_train))

  return [Logistic_classifier, tree_classifier, forest_classifier]

model = models(x_train,y_train)

#Accuracy on the testing data.


for i in range( len(model)):
  print("Model",i)

  cm= confusion_matrix(y_test, model[i].predict(x_test))

  TP=cm[0][0]
  TN=cm[1][1]
  FN=cm[1][0]
  FP=cm[0][1]

  print(cm)
  print("Testing Accuracy:", (TP+TN)/(TP+TN+FN+FP))
  print()

#Accuracy Using Sklearn
for i in range( len(model)):
  print("Model",i)
  print(classification_report(y_test, model[i].predict(x_test), digits=4))

  print("Testing Accuracy:",accuracy_score(y_test, model[i].predict(x_test)))
  print()

