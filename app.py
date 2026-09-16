import streamlit as st
from overview import display_overview
from causal import display_causal_graph
from simulator import run_risk_simulator
from strategic import show_strategic_recommendations


# Page config
st.set_page_config(
    page_title="Fragrance Supply Chain Intelligence", layout="wide"
)

st.sidebar.image(
    "https://via.placeholder.com/150x50?text=Company+Logo", width=150
)

# Sidebar navigation
page = st.sidebar.selectbox(
    "Navigate to:",
    [
        "🌸 Overview",
        "🔗 Causal Analysis",
        "⚡ Risk Simulator",
        "💡 Strategic Actions",
    ],
)

if page == "🌸 Overview":
    display_overview()
elif page == "🔗 Causal Analysis":
    display_causal_graph()
elif page == "⚡ Risk Simulator":
    run_risk_simulator()
elif page == "💡 Strategic Actions":
    show_strategic_recommendations()
