import random

from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd


random.seed(42)


# Basic settings
NUMBER_OF_CUSTOMERS = 300
NUMBER_OF_SALES = 2500

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_FOLDER = PROJECT_ROOT / "data" / "raw"

RAW_DATA_FOLDER.mkdir(parents=True, exist_ok=True)


# Customer source values
FIRST_NAMES = [
    "Ivan", "Maria", "Georgi", "Elena",
    "Daniel", "Sofia", "Martin", "Anna",
    "Nikolay", "Victoria", "Alex", "Sara",
    "Victor", "Laura", "Peter", "Emma"
]

LAST_NAMES = [
    "Ivanov", "Petrova", "Dimitrov", "Georgieva",
    "Nikolov", "Marin", "Popov", "Todorova",
    "Morgan", "Rossi", "Schmidt", "Carter",
    "Brown", "Miller", "Martin", "Wilson"
]

LOCATIONS = [
    ("Sofia", "Bulgaria"),
    ("Plovdiv", "Bulgaria"),
    ("Varna", "Bulgaria"),
    ("Burgas", "Bulgaria"),
    ("Bucharest", "Romania"),
    ("Cluj", "Romania"),
    ("Berlin", "Germany"),
    ("Milan", "Italy")
]


# Product catalogue
PRODUCTS = {
    "Electronics": [
        ("Wireless Mouse", 29.90),
        ("Keyboard", 49.90),
        ("Headphones", 79.90),
        ("USB-C Cable", 14.90),
        ("Laptop Stand", 44.90)
    ],

    "Home": [
        ("Coffee Maker", 89.90),
        ("Desk Lamp", 39.90),
        ("Water Bottle", 19.90),
        ("Storage Box", 24.90)
    ],

    "Sports": [
        ("Running Shoes", 99.90),
        ("Yoga Mat", 32.90),
        ("Football", 24.90),
        ("Training Bag", 54.90)
    ],

    "Clothing": [
        ("T-Shirt", 21.90),
        ("Hoodie", 54.90),
        ("Jeans", 64.90)
    ],

    "Office": [
        ("Notebook", 6.90),
        ("Pen Set", 12.90),
        ("Office Chair", 149.90),
        ("Desk Organizer", 18.90)
    ]
}


STORES = [
    (1, "Sofia Central", "Sofia", "Bulgaria"),
    (2, "Sofia South", "Sofia", "Bulgaria"),
    (3, "Plovdiv Store", "Plovdiv", "Bulgaria"),
    (4, "Varna Store", "Varna", "Bulgaria"),
    (5, "Bucharest Store", "Bucharest", "Romania")
]


PROMOTIONS = [
    (
        1,
        "Spring Sale",
        10.00,
        date(2024, 3, 1),
        date(2024, 3, 31)
    ),
    (
        2,
        "Summer Sale",
        15.00,
        date(2024, 7, 1),
        date(2024, 7, 31)
    ),
    (
        3,
        "Black Friday",
        25.00,
        date(2024, 11, 20),
        date(2024, 11, 30)
    ),
    (
        4,
        "Christmas Sale",
        20.00,
        date(2024, 12, 10),
        date(2024, 12, 31)
    ),
    (
        5,
        "Spring Sale 2025",
        10.00,
        date(2025, 3, 1),
        date(2025, 3, 31)
    ),
    (
        6,
        "Summer Sale 2025",
        15.00,
        date(2025, 7, 1),
        date(2025, 7, 31)
    ),
    (
        7,
        "Black Friday 2025",
        25.00,
        date(2025, 11, 20),
        date(2025, 11, 30)
    ),
    (
        8,
        "Christmas Sale 2025",
        20.00,
        date(2025, 12, 10),
        date(2025, 12, 31)
    )
]


def random_date(start_date, end_date):
    days_between = (end_date - start_date).days

    return start_date + timedelta(
        days=random.randint(0, days_between)
    )


def random_datetime(start_date, end_date):
    generated_date = random_date(start_date, end_date)

    hour = random.randint(9, 21)
    minute = random.randint(0, 59)

    return datetime.combine(
        generated_date,
        datetime.min.time()
    ).replace(
        hour=hour,
        minute=minute
    )


def generate_customers():
    rows = []

    for customer_id in range(1, NUMBER_OF_CUSTOMERS + 1):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)

        city, country = random.choice(LOCATIONS)

        registration_date = random_date(
            date(2023, 1, 1),
            date(2024, 6, 30)
        )

        email = (
            f"{first_name.lower()}."
            f"{last_name.lower()}."
            f"{customer_id}@example.com"
        )

        rows.append({
            "CustomerID": customer_id,
            "FirstName": first_name,
            "LastName": last_name,
            "Email": email,
            "City": city,
            "Country": country,
            "RegistrationDate": registration_date
        })

    customers = pd.DataFrame(rows)

    # Small raw-data issues for later cleaning practice
    customers.loc[9, "Email"] = None
    customers.loc[24, "City"] = "sofia"
    customers.loc[49, "City"] = " Varna "
    customers.loc[89, "Country"] = "bulgaria"

    duplicate_customer = customers.iloc[[39]].copy()

    customers = pd.concat(
        [customers, duplicate_customer],
        ignore_index=True
    )

    return customers


def generate_products():
    rows = []
    product_id = 1

    for category, products in PRODUCTS.items():
        for product_name, price in products:
            rows.append({
                "ProductID": product_id,
                "ProductName": product_name,
                "Category": category,
                "UnitPrice": price
            })

            product_id += 1

    return pd.DataFrame(rows)


def generate_stores():
    return pd.DataFrame(
        STORES,
        columns=[
            "StoreID",
            "StoreName",
            "City",
            "Country"
        ]
    )


def generate_promotions():
    return pd.DataFrame(
        PROMOTIONS,
        columns=[
            "PromotionID",
            "PromotionName",
            "DiscountPercent",
            "StartDate",
            "EndDate"
        ]
    )


def get_active_promotion(sale_date, promotions):
    active = promotions[
        (promotions["StartDate"] <= sale_date) &
        (promotions["EndDate"] >= sale_date)
    ]

    if active.empty:
        return None

    # Not every customer uses an active promotion
    if random.random() > 0.55:
        return None

    return random.choice(
        active["PromotionID"].tolist()
    )


def generate_sales(customers, promotions):
    rows = []

    start_date = date(2024, 1, 1)
    end_date = date(2025, 12, 31)

    for sale_id in range(1, NUMBER_OF_SALES + 1):
        sale_datetime = random_datetime(
            start_date,
            end_date
        )

        sale_date = sale_datetime.date()

        # Customer should already be registered before making a purchase
        eligible_customers = customers[
            customers["RegistrationDate"] <= sale_date
        ]

        customer_id = random.choice(
            eligible_customers["CustomerID"]
            .drop_duplicates()
            .tolist()
        )

        sales_channel = random.choices(
            ["Store", "Online"],
            weights=[65, 35],
            k=1
        )[0]

        if sales_channel == "Store":
            store_id = random.randint(1, len(STORES))
        else:
            store_id = None

        promotion_id = get_active_promotion(
            sale_date,
            promotions
        )

        rows.append({
            "SaleID": sale_id,
            "CustomerID": customer_id,
            "StoreID": store_id,
            "SaleDate": sale_datetime,
            "SalesChannel": sales_channel,
            "PromotionID": promotion_id
        })

    return pd.DataFrame(rows)


def generate_sale_items(sales, products):
    rows = []
    sale_item_id = 1

    product_ids = products["ProductID"].tolist()

    price_by_product = dict(
        zip(
            products["ProductID"],
            products["UnitPrice"]
        )
    )

    for sale_id in sales["SaleID"]:
        number_of_products = random.randint(1, 4)

        selected_products = random.sample(
            product_ids,
            number_of_products
        )

        for product_id in selected_products:
            quantity = random.choices(
                [1, 2, 3],
                weights=[75, 20, 5],
                k=1
            )[0]

            rows.append({
                "SaleItemID": sale_item_id,
                "SaleID": sale_id,
                "ProductID": product_id,
                "Quantity": quantity,
                "UnitPrice": price_by_product[product_id]
            })

            sale_item_id += 1

    return pd.DataFrame(rows)


def generate_returns(sale_items, sales):
    rows = []
    return_id = 1

    reasons = [
        "Damaged",
        "Wrong size",
        "Changed mind",
        "Not as expected",
        "Ordered by mistake"
    ]

    sale_dates = dict(
        zip(
            sales["SaleID"],
            sales["SaleDate"]
        )
    )

    for _, item in sale_items.iterrows():
        # Around 7% of purchased items are returned
        if random.random() < 0.07:
            original_sale_date = sale_dates[
                item["SaleID"]
            ]

            return_date = (
                original_sale_date +
                timedelta(days=random.randint(1, 30))
            )

            rows.append({
                "ReturnID": return_id,
                "SaleItemID": item["SaleItemID"],
                "ReturnDate": return_date,
                "ReturnQuantity": random.randint(
                    1,
                    int(item["Quantity"])
                ),
                "ReturnReason": random.choice(reasons)
            })

            return_id += 1

    return pd.DataFrame(rows)


def save_csv(dataframe, file_name):
    file_path = RAW_DATA_FOLDER / file_name

    dataframe.to_csv(
        file_path,
        index=False
    )

    print(
        f"{file_name}: {len(dataframe)} rows"
    )


def main():
    print("Generating retail data...")
    print()

    customers = generate_customers()
    products = generate_products()
    stores = generate_stores()
    promotions = generate_promotions()

    sales = generate_sales(
        customers,
        promotions
    )

    sale_items = generate_sale_items(
        sales,
        products
    )

    returns = generate_returns(
        sale_items,
        sales
    )

    save_csv(customers, "customers.csv")
    save_csv(products, "products.csv")
    save_csv(stores, "stores.csv")
    save_csv(promotions, "promotions.csv")
    save_csv(sales, "sales.csv")
    save_csv(sale_items, "sale_items.csv")
    save_csv(returns, "returns.csv")

    print()
    print("Done.")


if __name__ == "__main__":
    main()