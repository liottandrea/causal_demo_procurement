import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from data import generate_fragrance_data


def run_risk_simulator():
    st.subheader("⚡ Risk Simulator")
    st.write("Simulate supply chain disruptions and visualize impacts.")
    scenarios = {
        "🌪️ Extreme Weather in Provence": "Lavender",
        "🏛️ Bulgarian Political Crisis": "Rose",
        "📜 India Export Ban Extension": "Sandalwood",
        "🚢 Suez Canal Disruption": "All",
    }
    scenario = st.selectbox("Select Scenario", list(scenarios.keys()))
    severity = st.slider("Severity", 1, 10, 5)
    duration = st.slider("Duration (months)", 1, 24, 6)
    probability = st.slider("Probability of Occurrence (%)", 0, 100, 50)
    df = generate_fragrance_data()

    def simulate_disruption(df, scenario, severity, duration):
        df = df.copy()
        affected = scenarios[scenario]
        for ingr in df["ingredient"].unique():
            if affected == "All" or ingr == affected:
                idx = df[
                    (df["ingredient"] == ingr)
                    & (
                        df["date"]
                        >= df["date"].max() - pd.DateOffset(months=duration)
                    )
                ].index
                df.loc[idx, "price_per_kg"] *= 1 + 0.05 * severity
                df.loc[idx, "production_volume"] *= 1 - 0.04 * severity
        return df

    # Run simulation
    disrupted_df = simulate_disruption(df, scenario, severity, duration)

    ingr = scenarios[scenario] if scenarios[scenario] != "All" else "Lavender"
    base_df = df[df["ingredient"] == ingr].set_index("date").sort_index()
    full_df = (
        disrupted_df[disrupted_df["ingredient"] == ingr]
        .set_index("date")
        .sort_index()
    )

    dates_series = base_df.index
    baseline_prices = base_df["price_per_kg"]
    full_prices = full_df["price_per_kg"]

    delta = full_prices.values - baseline_prices.values
    expected_delta = delta * (probability / 100.0)
    spread = 3 * (1.0 - probability / 100.0) + 0.05
    lower = baseline_prices.values + expected_delta * (1.0 - spread)
    upper = baseline_prices.values + expected_delta * (1.0 + spread)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=dates_series,
            y=upper,
            line=dict(color="rgba(255,165,0,0)"),
            showlegend=False,
        )
    )
    fig.add_trace(
        go.Scatter(
            x=dates_series,
            y=lower,
            fill="tonexty",
            fillcolor="rgba(255,165,0,0.2)",
            line=dict(color="rgba(255,165,0,0)"),
            name="Uncertainty band",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=dates_series,
            y=baseline_prices.values + expected_delta,
            name="Expected disrupted",
            line=dict(color="orange", width=2),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=dates_series,
            y=baseline_prices.values,
            name="Baseline",
            line=dict(color="gray"),
        )
    )
    fig.update_layout(
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
        )
    )
    st.plotly_chart(fig, use_container_width=True)

    # Supply availability
    st.markdown("**Supply Availability by Country**")
    base = df[df["ingredient"] == ingr].iloc[-1]["supply_countries"]
    countries = list(base.keys())
    base_vals = [base[c] for c in countries]
    disrupted_vals = [max(0, v - severity * 2) for v in base_vals]
    fig2 = go.Figure(
        [
            go.Bar(
                x=countries,
                y=base_vals,
                name="Baseline",
                marker=dict(color="gray", line=dict(color="black", width=1)),
            ),
            go.Bar(
                x=countries,
                y=disrupted_vals,
                name="Disrupted",
                marker=dict(
                    color="#FFA500", line=dict(color="black", width=1)
                ),
            ),
        ]
    )
    fig2.update_layout(barmode="group")
    st.plotly_chart(fig2, use_container_width=True)

    # Cost impact
    st.markdown("**Cost Impact Calculator**")
    st.markdown(
        """
        **How this calculator works**

        - Full Direct Cost Increase (€): estimated as (average disrupted price - average baseline price) * total disrupted production volume. This represents the incremental cost the company would incur if the disruption happens at full severity over the affected window.
        - Expected Direct Cost (€): the above full direct cost scaled by the user-provided probability of occurrence (Probability of Occurrence %). This is the probability-weighted expected cost used for planning and risk accounting.
        - Expected Reformulation Costs (€): a heuristic share of expected direct cost (15%) representing costs to reformulate products or adjust sourcing temporarily.
        - Expected Lost Sales Risk (€): a heuristic share of expected direct cost (25%) representing potential revenue loss from stockouts, allocation, or delayed shipments.

        Assumptions & notes:
        - Prices and production volumes are averages over the recent affected window and are simulated for demo purposes. Real-world calculations should use item-level SKUs, margins, lead times, and inventory buffers.
        - This calculator uses a simple probability-weighting approach (expected value). It does not model tail-risk, optionality, or cascading indirect costs.
        - Use these figures as directional planning inputs; replace heuristics (15% / 25%) with your finance team's estimates for accuracy.
        """
    )

    full_direct_cost = (
        disrupted_df[disrupted_df["ingredient"] == ingr]["price_per_kg"].mean()
        - df[df["ingredient"] == ingr]["price_per_kg"].mean()
    ) * disrupted_df[disrupted_df["ingredient"] == ingr][
        "production_volume"
    ].sum()
    expected_direct_cost = full_direct_cost * (probability / 100.0)
    expected_reformulation_cost = expected_direct_cost * 0.15
    expected_lost_sales = expected_direct_cost * 0.25
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Full Direct Cost Increase (€)", f"{full_direct_cost:,.0f}")
    col2.metric("Expected Direct Cost (€)", f"{expected_direct_cost:,.0f}")
    col3.metric("Probability (%)", f"{probability}")
    col4.metric(
        "Expected Reformulation Costs (€)",
        f"{expected_reformulation_cost:,.0f}",
    )
    col5.metric("Expected Lost Sales Risk (€)", f"{expected_lost_sales:,.0f}")
