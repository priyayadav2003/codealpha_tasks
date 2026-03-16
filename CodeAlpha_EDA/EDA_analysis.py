import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#loading of dataset
df=pd.read_csv("titanic.csv")

#showing the first rows..
print(df.head())

#Dataset information...
print("\n Dataset info:")
print(df.info())

#checking the missing values...
print("\nMissing values are:")
print(df.isnull().sum())

#Statistical Summary...
print("\nStatistical Summary are : ")
print(df.describe())

# 01 Survival count...
plt.figure()
sns.countplot(x='Survived',data=df)
plt.title("Survival count are :")
plt.xlabel("survived(0=No,1=yes)")
plt.ylabel("Number of passengers")
plt.show()

# 02 Survival on the basis of gender..
plt.figure()
sns.countplot(x='Sex',hue='Survived',data=df)
plt.title("Survival on the basis gender")
plt.xlabel("gender")
plt.ylabel("count")
plt.show()

# 03 Age distribution of passengers
plt.figure()
sns.histplot(df['Age'],bins=30)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("frequency")
plt.show()

#04 Correlation heatmap between numerical variables
plt.figure()
sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.title("Correlation heatmap")
plt.show()

#05 Survival based on passenger class
plt.figure()
sns.countplot(x='Pclass',hue='Survived',data=df)
plt.title("Survival by passenser Class")
plt.xlabel("Passenger Class")
plt.ylabel("count")
plt.show()

print("\nEDA Analysis has been Completed Successfully")





