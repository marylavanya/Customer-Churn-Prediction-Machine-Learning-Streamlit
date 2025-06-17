# Customer-Churn-Prediction-Machine-Learning-Streamlit
![image](https://github.com/user-attachments/assets/e36b8886-0a41-4dda-9cec-6dfc8bb9619a)
## What is  Customer Churn?
Customer churn refers to when a customer stops using a company’s service. In this project, churn prediction helps identify users who are likely to leave, allowing businesses to take proactive steps to retain them.
# Table of contents
## Project Overview
A machine learning project that predicts whether a customer is likely to churn based on key behavioral indicators. This solution includes an end-to-end pipeline from data cleaning and model training to interactive deployment via Streamlit.
## Objective
* Predict customer churn using machine learning to identify at-risk customers early.
* Analyze customer behavior and demographics to understand churn patterns.
* Build and compare multiple models to select the best-performing one.
* Deploy the final model using Streamlit for real-time, user-friendly predictions.
## Model Comparison for Churn Prediction
| Model                 | F1-Score (Churn=1) | Recall (Churn=1) | Precision (Churn=1) | Accuracy | AUC-ROC  |
| --------------------- | ------------------ | ---------------- | ------------------- | -------- | -------- |
| **Gradient Boosting** | 0.91               | 0.87             | 0.96                | 0.85     | 0.85     |
| **Random Forest**     | 0.90               | 0.84             | 0.97                | 0.83     | 0.86     |
| **CatBoost**          | 0.89               | 0.83             | 0.95                | 0.81     | 0.84     |
| **XGBoost**           | 0.87               | 0.81             | 0.95                | 0.79     | 0.84     |
| **Decision Tree**     | 0.86               | 0.79             | 0.95                | 0.78     | 0.78     |

The Gradient Boosting model achieved a high F1-score (0.91) and precision (0.96), ensuring accurate churn prediction with minimal false positives. Its strong accuracy (0.85) reflects reliable performance across both churned and retained customers.
### Final Model Selection: Gradient Boosting Classifier
🔗 **Live App:**  
[Click here to view the app on Streamlit Cloud](https://customer-churn-prediction-machine-learning-app-qx8zr32djftfbyz.streamlit.app/)
## Sample Screenshot 

## Sample Predictions
Use the following examples in the app to test behavior:
### Likely to Churn
- Age: 22  
- Tenure: 1  
- Monthly Charges: 95.00  
- Gender: Female
  
**Prediction**: Customer is likely to **Churn**

----
### Likely to Not Churned
- Age: 45  
- Tenure: 60  
- Monthly Charges: 40.00    
- Gender: Male
  
**Prediction**: Customer is likely to **Not Churned**
## Key Insights
* Customers with lower tenure  are more likely to churn, early engagement is critical.
* High monthly charges correlate with increased churn.
* Customers with high bills and short tenure are at highest risk.
* Senior Citizens show slightly higher churn rates than younger customers.
## Recommendations
* Churned customers pay higher charges. Reviewing pricing plans or providing promotions/discounts to retain these high-risk, high-paying customers.
* Churn increases with age; consider designing age-specific loyalty programs or promotions.
* Consider onboarding initiatives such as “welcome packages”, “quick start guides”, or “new-customer incentives” to help first-year customers find more value in your service.
* Offer gifts or discounts to celebrate tenure milestones at 3, 6, and 12 months.
