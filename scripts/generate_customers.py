import pandas as pd
import random
from faker import Faker

fake = Faker()

age_groups = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56+"
]

genders = [
    "Male",
    "Female",
    "Other"
]

countries = [
    "Canada",
    "United States",
    "United Kingdom",
    "India",
    "Australia"
]

purchase_channels = [
    "Online Store",
    "Retail Store",
    "Carrier Store",
    "Third-Party Marketplace"
]

# Empty list to store customer records

customers = []

# Generate 5 sample customers

for customer_id in range(1, 50001):

    customers.append({

        "customer_id": f"CUST{customer_id:05d}",
        "customer_name": fake.name(),
        "age_group": random.choice(age_groups),
        "gender": random.choice(genders),
        "country": random.choice(countries),
        "purchase_channel": random.choice(purchase_channels)

    })

# Display generated customers

#print(customers)

# Convert list to DataFrame

customers_df = pd.DataFrame(customers)

# Save DataFrame as CSV

customers_df.to_csv(
    "data/raw/customers.csv",
    index=False
)

print(f"{len(customers_df)} customers generated successfully!")