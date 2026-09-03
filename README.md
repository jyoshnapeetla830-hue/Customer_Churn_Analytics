\# Customer Churn Analytics



\## Project Overview



This project analyzes telecom customer churn using Python and Streamlit.



The goal is to identify customer segments with high churn rates and understand the factors that may contribute to customer cancellations.



\## Dataset



The project uses the Telco Customer Churn dataset containing customer information such as:



\- Customer demographics

\- Contract type

\- Internet service

\- Payment method

\- Monthly charges

\- Total charges

\- Customer tenure

\- Churn status



\## Data Cleaning



The dataset was cleaned using Python and Pandas.



Steps included:



\- Checking missing values

\- Converting `TotalCharges` to numeric format

\- Removing rows with missing `TotalCharges`

\- Creating customer tenure groups



After cleaning, the dataset contains \*\*7,032 customers\*\*.



\## Key Findings



\- Overall churn rate: \*\*26.58%\*\*

\- Month-to-month customers have the highest churn rate: \*\*42.71%\*\*

\- Two-year contract customers have the lowest churn rate: \*\*2.85%\*\*

\- Fiber optic customers have a churn rate of \*\*41.89%\*\*

\- Electronic check customers have a churn rate of \*\*45.29%\*\*

\- Customers with 0–12 months tenure have the highest churn rate: \*\*47.68%\*\*



\## Dashboard



The Streamlit dashboard displays:



\- Total customers

\- Churned customers

\- Overall churn rate

\- Churn by contract type

\- Churn by internet service

\- Churn by payment method

\- Churn by senior citizen status

\- Churn by tenure group



\## Technologies Used



\- Python

\- Pandas

\- Matplotlib

\- Seaborn

\- Streamlit



\## Project Structure



```text

Customer\_Churn\_Analytics/

│

├── data/

│   ├── WA\_Fn-UseC\_-Telco-Customer-Churn.csv

│   └── cleaned\_churn\_data.csv

│

├── churn\_analysis.py

├── dashboard.py

├── README.md

├── churn\_distribution.png

├── churn\_by\_contract.png

├── churn\_by\_internet\_service.png

├── churn\_by\_payment\_method.png

├── churn\_by\_senior\_citizen.png

└── churn\_by\_tenure\_group.png
### Dashboard Preview

![Customer Churn Analytics Dashboard](dashboard_preview.png)

## Business Insights & Recommendations

### Key Business Insights

1. **Month-to-month customers are at the highest risk of churn**
   - Churn rate: 42.71%
   - Customers with longer contracts show significantly lower churn.

2. **New customers are more likely to churn**
   - Customers with 0–12 months tenure have a 47.68% churn rate.
   - Churn decreases as customer tenure increases.

3. **Electronic check customers have the highest churn**
   - Churn rate: 45.29%
   - This segment requires closer retention analysis.

4. **Fiber optic customers show high churn**
   - Churn rate: 41.89%
   - Service quality, pricing, or customer expectations may need further investigation.

### Recommendations

- Encourage month-to-month customers to move to one-year or two-year contracts.
- Create onboarding and retention programs for customers in their first 12 months.
- Investigate the reasons for high churn among electronic check customers.
- Review pricing and service experience for fiber optic customers.
- Offer targeted retention discounts or loyalty benefits to high-risk customers.

