import requests
import pandas as pd
import psycopg2
import csv
import http.client
import json

print("All libraries are successfully imported!")

url = "https://real-time-amazon-data.p.rapidapi.com/product-details"

querystring = {"asin":"B07ZPKBL9V","country":"US"}

headers = {
	"x-rapidapi-key": "60749743a2msh4219878febd6d25p116eadjsnd65c0c398a27",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


#print(response.json())

data = response.json()

#Save the data to a file
filename = 'amazon_customer_review.json'
with open(filename, 'w') as file:
    json.dump(data, file)

# Read into a dataframe

amazon_customer_review = pd.read_json('amazon_customer_review.json')

amazon_customer_review

# Assuming you've already loaded the response into 'data' variable
with open('amazon_customer_review.json') as f:
    data = json.load(f)

structured_data = {}
for key, value in data.items():
    if isinstance(value, dict) and 'data' in value:
        structured_data[key] = value['data']
    else:
        structured_data[key] = value  # or handle differently if needed

# Assuming 'data' contains your API response
reviews_data = structured_data['data']['reviews']  # Extract the actual reviews list

# Create DataFrame and clean data
df = pd.json_normalize(reviews_data)

# Convert star ratings to numeric
df['review_star_rating'] = pd.to_numeric(df['review_star_rating'], errors='coerce')

# Use raw string literal (prefix with r)
df['helpful_votes'] = df['helpful_vote_statement'].str.extract(r'(\d+)').fillna(0).astype(int)

clean_df = df.loc[:, [
    'review_date', 'review_title', 'review_comment',
    'review_star_rating', 'is_verified_purchase', 'helpful_votes',
    'review_author', 'review_images', 'reviewed_product_asin'
]]

clean_df.loc[:, 'review_date'] = pd.to_datetime(
    clean_df['review_date'].str.replace('Reviewed in the United States on ', ''),
    errors='coerce'
)

# Save to CSV
clean_df.to_csv('amazon_reviews_clean.csv', index=False)