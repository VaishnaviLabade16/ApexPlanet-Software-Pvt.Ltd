-- SQL for Business Questions
USE churn_analysis;

-- 1. Total customers
SELECT COUNT(*) FROM cleaned_data;

-- 2. How many customers churned?
SELECT Churn, COUNT(*) 
FROM cleaned_data
GROUP BY Churn;

-- 3. Which contract has highest churn?
SELECT Contract, AVG(Churn)
FROM cleaned_data
GROUP BY Contract;

-- 4. Avg monthly charges
SELECT AVG(MonthlyCharges) FROM cleaned_data;

-- 5. Do high paying customers churn more?
SELECT Churn, AVG(MonthlyCharges)
FROM cleaned_data
GROUP BY Churn;