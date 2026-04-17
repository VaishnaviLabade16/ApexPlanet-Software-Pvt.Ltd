# Task 2. Exploratory Data Analysis (EDA) & Business Intelligence 
import pandas as pd
df = pd.read_csv("C:/Users/cbzco/OneDrive/Desktop/ApexPlanet/Task2_EDA_Analysis/cleaned_data.csv")

print(df.head())
print(df.describe())
print(df['Churn'].value_counts())

# Descriptive Statistics & Univariate Analysis
import matplotlib.pyplot as plt

df['Churn'].value_counts().plot(kind='bar')
plt.title("Churn Count")
plt.show()

df['MonthlyCharges'].hist()
plt.title("Monthly Charges Distribution")
plt.show()

# Multivariate Analysis & Correlation  
df.groupby('Contract')['Churn'].mean().plot(kind='bar')
plt.title("Churn by Contract")
plt.show()

df.boxplot(column='MonthlyCharges', by='Churn')
plt.show()

print(df.corr(numeric_only=True))