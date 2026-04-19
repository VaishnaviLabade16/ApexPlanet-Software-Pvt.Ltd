# Hypothesis Testing
import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv(r"C:\Users\cbzco\OneDrive\Desktop\ApexPlanet\Task2_EDA_Analysis\cleaned_data.csv")

churn_yes = df[df['Churn'] == 1]['MonthlyCharges']
churn_no = df[df['Churn'] == 0]['MonthlyCharges']

t_stat, p_value = ttest_ind(churn_yes, churn_no)

print("P-value:", p_value)