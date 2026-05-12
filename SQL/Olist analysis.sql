/* 1. TOP 10 CATEGORIES BY REVENUE */
SELECT ... (/* TOP 10 CATEGORIES BY REVENUE
This query helps identify the most profitable product categories.
*/
SELECT 
    product_category, 
    COUNT(order_id) AS total_orders,
    ROUND(SUM(price), 2) AS total_revenue,
    ROUND(AVG(price), 2) AS average_ticket
FROM olist_master_cleaned
GROUP BY product_category
ORDER BY total_revenue DESC
LIMIT 10;) ... ;

/* 2. DELIVERY PERFORMANCE ANALYSIS */
SELECT ... (/* DELIVERY PERFORMANCE ANALYSIS
Calculates the average delivery time vs the estimated time by state.
Helps identify logistics bottlenecks.
*/
SELECT 
    customer_state,
    ROUND(AVG(delivery_time_days), 2) AS avg_actual_delivery,
    ROUND(AVG(estimated_delivery_days), 2) AS avg_estimated_delivery,
    ROUND(AVG(estimated_delivery_days - delivery_time_days), 2) AS safety_margin
FROM olist_master_cleaned
WHERE delivery_time_days IS NOT NULL
GROUP BY customer_state
ORDER BY avg_actual_delivery DESC;) ... ;

/* 3. DELAY VS REVIEW SCORE */
SELECT ... (/* DELAY VS REVIEW SCORE
Shows how the review score drops when the product arrives after the estimated date.
*/
SELECT 
    CASE 
        WHEN delivery_time_days <= estimated_delivery_days THEN 'On Time / Early'
        ELSE 'Late'
    END AS delivery_status,
    ROUND(AVG(review_score), 2) AS avg_score,
    COUNT(*) AS total_orders
FROM olist_master_cleaned
WHERE delivery_time_days IS NOT NULL
GROUP BY delivery_status;) ... ;