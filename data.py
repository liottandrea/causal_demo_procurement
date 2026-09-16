import pandas as pd
import numpy as np


def generate_fragrance_data():
    # Date range: monthly from Jan 2019 to Dec 2024
    dates = pd.date_range(start="2019-01-01", end="2024-12-01", freq="MS")
    n_months = len(dates)
    ingredients = {
        "Lavender": {
            "price_range": (40, 80),
            "countries": {"France": 60, "Bulgaria": 30, "Spain": 10},
        },
        "Rose": {
            "price_range": (4000, 7000),
            "countries": {"Bulgaria": 70, "Turkey": 20, "Morocco": 10},
        },
        "Sandalwood": {
            "price_range": (1500, 3000),
            "countries": {"India": 80, "Australia": 20},
        },
    }
    data = []
    np.random.seed(42)
    for ingr, props in ingredients.items():
        base_price = np.random.uniform(*props["price_range"], n_months)
        production = (
            np.random.normal(1000, 200, n_months)
            if ingr != "Rose"
            else np.random.normal(300, 50, n_months)
        )
        weather = np.clip(np.random.normal(70, 15, n_months), 0, 100)
        political = np.clip(np.random.normal(80, 10, n_months), 0, 100)
        # Event adjustments
        for i, dt in enumerate(dates):
            # Harvest seasons
            if ingr == "Rose" and dt.month in [5, 6]:
                base_price[i] *= 0.85
            if ingr == "Lavender" and dt.month in [7, 8]:
                base_price[i] *= 0.88
            # COVID impact
            if dt.year == 2020 and dt.month == 3:
                base_price[i] *= 1.3
            # Bulgaria political crisis
            if ingr == "Rose" and dt.year == 2022 and dt.month == 10:
                political[i] -= 30
                production[i] *= 0.7
            # India sandalwood restrictions
            if ingr == "Sandalwood" and dt.year == 2023 and dt.month == 1:
                production[i] *= 0.6
                base_price[i] *= 1.25
        # Supply countries
        countries = props["countries"]
        for i, dt in enumerate(dates):
            data.append(
                {
                    "date": dt,
                    "ingredient": ingr,
                    "price_per_kg": round(base_price[i], 2),
                    "production_volume": max(0, round(production[i], 1)),
                    "weather_impact_score": round(weather[i], 1),
                    "political_stability_score": round(political[i], 1),
                    "supply_countries": countries,
                }
            )
    df = pd.DataFrame(data)
    return df
