#
# Jason
# Pandas
#
# Loading csv
import matplotlib.pyplot as plt
import pandas as pd
ti=pd.read_csv('titanic.csv')
print(ti)
# Data Exploration
print(ti.info())
print(ti.shape)
print(ti['Age'].mean())
print(ti['Age'].median())
print(ti['Age'].min())
print(ti['Age'].max())
print(sum(ti['Age']))
print(sum(ti['Age'])/len(ti['Age']))#Age average
print(ti['Fare'].mean())
print(ti['Fare'].median())
print(ti['Fare'].min())
print(ti['Fare'].max())
print(sum(ti['Fare'])/len(ti['Fare']))#Fare average

# Data Cleaning
print(ti.isnull().sum())
ti=ti.dropna(subset=["Embarked"])
ti['Cabin']=ti['Cabin'].fillna("NoCabin")
print(ti.shape)
print(ti.isnull().sum())
ti = ti.fillna(ti['Age'].median())
print(ti)
print(ti.isnull().sum())

# Data Analysis
print(ti['Sex'].value_counts())

print(sum(ti['Age']))
print(sum(ti['Age'])/len(ti['Age']))#average

print(ti['Survived'].value_counts(normalize=True))
print(ti['Pclass'].value_counts())
Sr=ti.groupby('Pclass')['Survived'].mean()
# Data Visualization
Sr.plot.bar()
plt.show()