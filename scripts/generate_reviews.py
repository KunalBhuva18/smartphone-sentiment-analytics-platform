import pandas as pd
import random
from faker import Faker

fake = Faker()

# Sentiment categories

sentiments = [
    "Positive",
    "Neutral",
    "Negative"
]

# Sentiment distribution weights

sentiment_weights = [
    64.2,   # Positive
    21.3,   # Neutral
    14.5    # Negative
]

positive_reviews = [

    "Excellent battery life and amazing camera quality.",
    "The display is bright and vibrant. Very satisfied.",
    "Performance is extremely smooth and fast.",
    "The phone exceeded my expectations in every way.",
    "Great design, excellent camera, and long battery life.",
    "Fast charging works perfectly and battery lasts all day.",
    "Outstanding performance for gaming and multitasking.",
    "Very impressed with the build quality and display.",
    "The camera takes stunning photos in all lighting conditions.",
    "Very happy with this purchase and would highly recommend it."

]

neutral_reviews = [

    "The phone performs as expected.",
    "Overall the device is decent for daily use.",
    "Battery life is average but acceptable.",
    "Camera quality is fine but could be improved.",
    "The phone works well although nothing stands out.",
    "Performance is satisfactory for the price.",
    "The device is good, but there are better options available.",
    "Display quality is decent but not exceptional."

]

negative_reviews = [

    "Battery drains very quickly and needs frequent charging.",
    "The phone overheats during gaming sessions.",
    "Camera quality is disappointing in low light.",
    "Screen became unresponsive after a few weeks.",
    "Device experiences frequent app crashes.",
    "Charging speed is slower than expected.",
    "Poor build quality and disappointing performance.",
    "The phone lags during normal usage.",
    "Battery performance is far below expectations.",
    "Very disappointed with the overall experience."

]

# Empty list to store reviews

reviews = []


# Generate 5 sample reviews

for review_id in range(1, 128001):

    # Select sentiment based on weighted distribution
    sentiment = random.choices(
        sentiments,
        weights=sentiment_weights,
        k=1
    )[0]

    # Select review text based on sentiment
    if sentiment == "Positive":
        review_text = random.choice(positive_reviews)
        rating = random.choice([4, 5])

    elif sentiment == "Neutral":
        review_text = random.choice(neutral_reviews)
        rating = 3

    else:
        review_text = random.choice(negative_reviews)
        rating = random.choice([1, 2])

    # Create review record
    reviews.append({

        "review_id": f"REV{review_id:06d}",
        "customer_id": f"CUST{random.randint(1, 50000):05d}",
        "product_id": f"PROD{random.randint(1, 18):04d}",
        "review_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "rating": rating,
        "verified_purchase": random.choice(["Yes", "No"]),
        "review_text": review_text

    })

    # Convert reviews list to DataFrame

reviews_df = pd.DataFrame(reviews)

# Save reviews dataset

reviews_df.to_csv(
    "data/raw/reviews.csv",
    index=False
)

print(f"{len(reviews_df)} reviews generated successfully!")