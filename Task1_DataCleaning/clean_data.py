# Data Immersion & Wrangling
import pandas as pd
df = pd.read_excel("data.xlsx")
print(df.head())

print(df.info())
print(df.describe())
print(df.isnull().sum())

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].mean(), inplace=True)

df = df.drop_duplicates()
df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})
print(df.isnull().sum())

df.to_csv("cleaned_data.csv", index=False)