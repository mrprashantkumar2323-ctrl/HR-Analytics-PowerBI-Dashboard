"""
HR Attrition Machine Learning Predictor
Author: Prashant Kumar
Description: Predicts employee attrition probability based on demographic, compensation,
and job satisfaction metrics using Random Forest Classification.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score

def build_hr_attrition_pipeline():
    np.random.seed(42)
    n_records = 3000
    
    departments = ['Sales', 'R&D', 'Human Resources', 'Finance', 'Marketing']
    roles = ['Manager', 'Senior Executive', 'Junior Analyst', 'Director', 'Specialist']
    
    data = {
        'age': np.random.randint(22, 60, n_records),
        'salary': np.random.normal(55000, 18000, n_records).clip(25000, 150000),
        'experience_years': np.random.randint(1, 25, n_records),
        'department': np.random.choice(departments, n_records),
        'job_satisfaction': np.random.randint(1, 5, n_records),
        'performance_rating': np.random.randint(1, 5, n_records),
        'overtime': np.random.choice([0, 1], p=[0.7, 0.3], size=n_records),
        'years_at_company': np.random.randint(0, 15, n_records),
        'training_times_last_year': np.random.randint(0, 6, n_records)
    }
    df = pd.DataFrame(data)
    
    # Target formula: higher overtime, low satisfaction, and low salary drive turnover
    attrition_score = (
        0.8 * df['overtime'] -
        0.35 * df['job_satisfaction'] -
        0.00002 * df['salary'] +
        0.04 * (df['age'] < 30).astype(int) +
        np.random.normal(0, 0.3, n_records)
    )
    df['attrition'] = (attrition_score > 0.05).astype(int)
    
    print("[+] HR Dataset Engineered:")
    print(f"  Total Employees: {len(df):,}")
    print(f"  Attrition Rate:  {df['attrition'].mean() * 100:.2f}%")
    
    df_encoded = pd.get_dummies(df, columns=['department'], drop_first=True)
    X = df_encoded.drop('attrition', axis=1)
    y = df_encoded['attrition']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    
    model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]
    
    print("=" * 55)
    print(f"Accuracy:  {accuracy_score(y_test, preds) * 100:.2f}%")
    print(f"ROC-AUC:   {roc_auc_score(y_test, probs):.4f}")
    print("=" * 55)
    print("
Classification Report:")
    print(classification_report(y_test, preds))
    
    importances = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=False)
    print("Top Feature Drivers of Employee Turnover:")
    print(importances.head(6).to_string(index=False))

if __name__ == '__main__':
    build_hr_attrition_pipeline()
