import requests
import pandas as pd
import json

url = "https://real-time-amazon-data.p.rapidapi.com/product-reviews"

querystring = {
    "asin": "B0D32V79QW",
    "country": "US",
    "page": "1",
    "sort_by": "TOP_REVIEWS",
    "star_rating": "ALL",
    "verified_purchases_only": "false",
    "images_or_videos_only": "false",
    "current_format_only": "false"
}

headers = {
    "x-rapidapi-key": "60749743a2msh4219878febd6d25p116eadjsnd65c0c398a27",
    "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Save the data to a file
with open('amazon_customer_review.json', 'w') as f:
    json.dump(data, f, indent=2)

# Load the data
with open('amazon_customer_review.json') as f:
    data = json.load(f)

# Debug: Print the JSON structure
print(json.dumps(data, indent=2))  # Check the structure in your console

# Extract reviews correctly
reviews_data = data.get('data', {}).get('reviews', [])  # Fix this line

if not reviews_data:
    print("No reviews found in the data.")
    reviews_data = []  # Ensure it's a list to avoid errors

# Create DataFrame and clean data
df = pd.json_normalize(reviews_data)

if df.empty:
    print("DataFrame is empty. No reviews to process.")
else:
    # Data cleaning steps
    df['review_star_rating'] = pd.to_numeric(df['review_star_rating'], errors='coerce')
    df['helpful_votes'] = df['helpful_vote_statement'].str.extract(r'(\d+)').fillna(0).astype(int)
    
    # Select relevant columns
    columns_to_keep = [
        'review_date', 'review_title', 'review_comment',
        'review_star_rating', 'is_verified_purchase', 'helpful_votes',
        'review_author', 'review_images', 'reviewed_product_asin'
    ]
    
    clean_df = df[columns_to_keep].copy()

    # Clean review dates
    clean_df['review_date'] = pd.to_datetime(
        clean_df['review_date'].str.replace('Reviewed in the United States on ', '', regex=True),
        errors='coerce'
    )

    # Save to CSV
    clean_df.to_csv('amazon_reviews_clean.csv', index=False)
    print("Data successfully processed and saved to CSV.")
