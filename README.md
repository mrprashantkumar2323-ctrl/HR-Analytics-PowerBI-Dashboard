# 📊 Enterprise HR Analytics Power BI Dashboard & Machine Learning Predictor

[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/ML-Random%20Forest%20Classifier-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)

An end-to-end workforce intelligence platform uniting **Power BI interactive dashboards** with **Machine Learning predictive turnover modeling**.

---

## 📌 Repository Contents
1. **Interactive Power BI Template (`HR ANALYTICS DASHBOARD -1.pbit`)**:
   - Executive Summary, Attrition Deep-Dive, Departmental Headcount, and Salary Equity Analysis.
2. **Workforce Dataset (`HR_Analytics_Dataset.xlsx`)**:
   - Comprehensive employee demographics, compensation, satisfaction ratings, and retention indicators.
3. **Machine Learning Model (`hr_attrition_predictor.py`)**:
   - Random Forest model evaluating key drivers of turnover (overtime, job satisfaction, salary levels, tenure).
4. **Custom DAX Measures**:
   - `Total Employees = COUNTROWS(Employee)`
   - `Attrition Rate = DIVIDE(CALCULATE(COUNTROWS(Employee), Employee[Attrition]="Yes"), COUNTROWS(Employee), 0)`
   - `Average Salary = AVERAGE(Employee[Salary])`
   - `Overtime Attrition % = CALCULATE([Attrition Rate], Employee[Overtime]="Yes")`

---

## 🚀 Quickstart

```bash
git clone https://github.com/mrprashantkumar2323-ctrl/HR-Analytics-PowerBI-Dashboard.git
cd HR-Analytics-PowerBI-Dashboard

pip install -r requirements.txt
python hr_attrition_predictor.py
```

---

## 👨‍💻 Author
**Prashant Kumar**  
* [LinkedIn](https://www.linkedin.com/in/prashant-kumar-p453) • [GitHub](https://github.com/mrprashantkumar2323-ctrl)
