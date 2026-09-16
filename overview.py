import streamlit as st
from data import generate_fragrance_data


def display_overview():
    st.header("🌸 Fragrance Supply Chain Intelligence")
    st.subheader("Business Context and Current Challenges")
    st.write(
        """This dashboard demonstrates causal modelling for fragrance ingredient procurement, focusing on supply chain resilience and risk management."""
    )
    st.markdown(
        """
    **Key Ingredients:** Lavender, Rose, Sandalwood  
    **Challenges:** Weather volatility, political instability, export restrictions, logistics disruptions  
    **Recent Events:** COVID-19, Bulgaria crisis, India export ban
    """
    )
    df = generate_fragrance_data()
    st.dataframe(df.head(12))

    st.markdown("---")
    st.subheader("Data dictionary")
    st.markdown(
        """
        **Columns**

        - `date`: Month start date for the observation (monthly frequency).
        - `ingredient`: Fragrance ingredient (Lavender, Rose, Sandalwood).
        - `price_per_kg`: Observed price in Euros per kilogram (simulated realistic ranges).
        - `production_volume`: Estimated production volume (kg) for the month.
        - `weather_impact_score`: Simulated weather impact index (0 = no impact, 100 = severe impact).
        - `political_stability_score`: Political stability index (0 = unstable, 100 = stable).
        - `supply_countries`: Dict of supplier countries and percent contribution (sums to ~100).

        **Notes**

        - Harvest seasonality and named events (COVID spike March 2020, Bulgaria crisis Oct 2022, India restrictions Jan 2023) are injected into prices and volumes to mimic realistic shocks.
        - `price_per_kg` and `production_volume` are simulated and include noise; treat them as synthetic examples for demo purposes.
        """
    )
