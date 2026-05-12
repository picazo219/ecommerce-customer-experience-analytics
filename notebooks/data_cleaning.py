import pandas as pd
import os

# Set the base path
path = r'C:\Users\dpip_\Documents\Académico\Data Scientist\Brazilian E-Commerce'

def load_and_clean_data(base_path):
    # 1. Load the datasets
    # Using raw strings for paths to avoid escape character issues
    orders = pd.read_csv(os.path.join(base_path, 'olist_orders_dataset.csv'))
    items = pd.read_csv(os.path.join(base_path, 'olist_order_items_dataset.csv'))
    products = pd.read_csv(os.path.join(base_path, 'olist_products_dataset.csv'))
    translation = pd.read_csv(os.path.join(base_path, 'product_category_name_translation.csv'))
    customers = pd.read_csv(os.path.join(base_path, 'olist_customers_dataset.csv'))
    reviews = pd.read_csv(os.path.join(base_path, 'olist_order_reviews_dataset.csv'))

    print("Files loaded successfully.")

    # 2. Translate product categories from Portuguese to English
    # Merging products with the translation table
    products = pd.merge(products, translation, on='product_category_name', how='left')
    
    # Drop the original Portuguese column and rename the English one
    products.drop(columns=['product_category_name'], inplace=True)
    products.rename(columns={'product_category_name_english': 'product_category'}, inplace=True)

    # 3. Handle missing values for categories
    products['product_category'] = products['product_category'].fillna('others')

    # 4. Data Type Conversion (Dates)
    # Converting string columns to datetime for accurate time analysis
    date_columns = [
        'order_purchase_timestamp', 
        'order_approved_at', 
        'order_delivered_carrier_date', 
        'order_delivered_customer_date', 
        'order_estimated_delivery_date'
    ]
    for col in date_columns:
        orders[col] = pd.to_datetime(orders[col])

    # 5. Merge Strategy: Creating a Master Dataframe
    # We join Items with Orders, then add Product details and Customer location
    master_df = pd.merge(items, orders, on='order_id', how='inner')
    master_df = pd.merge(master_df, products, on='product_id', how='left')
    master_df = pd.merge(master_df, customers, on='customer_id', how='left')
    
    # Adding review scores
    # We take the average review score per order to avoid duplicating rows if multiple reviews exist
    avg_reviews = reviews.groupby('order_id')['review_score'].mean().reset_index()
    master_df = pd.merge(master_df, avg_reviews, on='order_id', how='left')

    # 6. Final Cleaning
    # Calculating Delivery Time (Actual vs Estimated) in days
    master_df['delivery_time_days'] = (master_df['order_delivered_customer_date'] - master_df['order_purchase_timestamp']).dt.days
    master_df['estimated_delivery_days'] = (master_df['order_estimated_delivery_date'] - master_df['order_purchase_timestamp']).dt.days

    print(f"Master dataset created with {master_df.shape[0]} rows.")
    
    return master_df

# Execute the process
if __name__ == "__main__":
    df_final = load_and_clean_data(path)
    
    # Save the cleaned master file for SQL/Power BI
    output_file = os.path.join(path, 'olist_master_cleaned.csv')
    df_final.to_csv(output_file, index=False)
    print(f"Process complete. Cleaned file saved at: {output_file}")