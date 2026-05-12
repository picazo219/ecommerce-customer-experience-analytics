# ecommerce-customer-experience-analytics
📈 A data-driven approach to customer loyalty: Discovering how delivery precision impacts review scores in the Brazilian e-commerce market. Built with Python, SQL and Power BI.

![Olist Dashboard Overview](dashboard_preview.png)

## 🎯 Project Overview
...

# Olist Logistics Performance & Customer Experience Analysis

## 🎯 Project Overview
This project explores the relationship between logistics efficiency and customer satisfaction within the Brazilian e-commerce landscape. By analyzing over **100,000 orders** from the Olist dataset, I developed a high-fidelity dashboard to visualize how delivery performance directly impacts business health.

## 🚀 Key Insights & Findings
The core of this analysis centers on the **'Safety Margin'** (the difference in days between the estimated delivery date and the actual delivery date).

* **The Satisfaction Threshold:** There is a clear linear correlation between the delivery buffer and customer ratings.
    * **5-Star Reviews:** Maintain a healthy **Safety Margin of 12.83 days**.
    * **1-Star Reviews:** The buffer collapses to only **5.39 days**.
* **Logistics as a CX Driver:** The data suggests that customer dissatisfaction is triggered not just by "late" deliveries, but by the erosion of the promised delivery window. When the safety margin falls below **6 days**, negative reviews increase significantly.
* **Revenue Concentration:** The Top 10 product categories (led by Health & Beauty and Watches) account for a significant portion of the $13.59M total revenue, highlighting where logistics optimization will have the highest financial impact.

## 🛠️ Tech Stack
* **Python (Pandas):** Data cleaning, ETL, and feature engineering for logistics metrics.
* **SQL:** Complex data joins and time-series calculations.
* **Power BI:** * **DAX:** Implementation of custom measures for Average Satisfaction and Safety Margins.
    * **UI/UX:** Advanced dashboard design using custom gradients, dark-mode containers, and a strategic visual hierarchy.

## 💡 Strategic Recommendations
1.  **Buffer Protection:** Implement an automated alert system when the predicted safety margin for an order falls below 7 days.
2.  **Expectation Management:** Recalibrate the delivery estimation algorithm for states with high logistics volatility to maintain a perceived "Safety Zone" for the customer.
3.  **Category-Specific Logistics:** Prioritize "Express" shipping for high-revenue categories to stabilize the overall platform NPS.

---
**Author:** David Picazo  
**Field:** Clinical Efficiency Specialist | Data Analyst  
**Contact:** [da.picazo@gmail.com](mailto:da.picazo@gmail.com)
