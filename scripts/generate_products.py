import pandas as pd
import random

#Smartphone features
brands = {
    "Apple": [
        "iPhone 15",
        "iPhone 15 Pro",
        "iPhone 16",
        "iPhone 16 Pro"
    ],

    "Samsung": [
        "Galaxy S24",
        "Galaxy S24 Ultra",
        "Galaxy S25",
        "Galaxy Z Fold 7"
    ],

    "Google": [
        "Pixel 9",
        "Pixel 9 Pro",
        "Pixel 10",
        "Pixel Fold"
    ],

    "OnePlus": [
        "OnePlus 13",
        "OnePlus Open",
        "OnePlus Nord 5"
    ],

    "Xiaomi": [
        "Xiaomi 15",
        "Xiaomi 15 Ultra",
        "Redmi Note 14"
    ]
}

colors = [
    "Black",
    "White",
    "Blue",
    "Silver",
    "Green",
    "Purple"
]

storage_options = [128, 256, 512, 1024]
ram_options = [8, 12, 16]

products = []

product_id = 1

for brand, models in brands.items():

    for model in models:

        products.append({

            "product_id": f"PROD{product_id:04d}",
            "brand": brand,
            "model_name": model,
            "launch_year": random.randint(2024, 2026),
            "storage_gb": random.choice(storage_options),
            "ram_gb": random.choice(ram_options),
            "price": round(random.uniform(699, 1999), 2),
            "operating_system": "iOS" if brand == "Apple" else "Android",
            "color": random.choice(colors)

        })

        product_id += 1

# Converting list to DataFrame

products_df = pd.DataFrame(products)

# Saving dataset

products_df.to_csv(
    "data/raw/products.csv",
    index=False
)

print(f"{len(products_df)} products generated successfully!")