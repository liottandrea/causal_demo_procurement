import streamlit as st


def causal_inference_engine(scenario):
    effects = {}
    if scenario == "🌪️ Extreme Weather in Provence":
        effects = {
            "harvest_yield": -40,
            "labour_costs": 20,
            "processing_delays": 15,
            "final_price": 65,
            "confidence_interval": (55, 75),
        }
    elif scenario == "🏛️ Bulgarian Political Crisis":
        effects = {
            "harvest_yield": -30,
            "labour_costs": 10,
            "processing_delays": 10,
            "final_price": 40,
            "confidence_interval": (30, 50),
        }
    elif scenario == "📜 India Export Ban Extension":
        effects = {
            "harvest_yield": -50,
            "labour_costs": 25,
            "processing_delays": 20,
            "final_price": 80,
            "confidence_interval": (70, 90),
        }
    elif scenario == "🚢 Suez Canal Disruption":
        effects = {
            "harvest_yield": -10,
            "labour_costs": 5,
            "processing_delays": 30,
            "final_price": 20,
            "confidence_interval": (10, 30),
        }
    return effects


def generate_recommendations(scenario, effects):
    recs = []

    def add(rec):
        recs.append(rec)

    # Map scenario -> targeted recommendations
    if scenario == "🌪️ Extreme Weather in Provence":
        target = "Lavender"
        add(
            {
                "type": "Immediate (0-1 month)",
                "action": f"Activate alternative suppliers in Spain and Bulgaria for {target}",
                "cost": 60000,
                "risk_mitigation": 85,
                "time": "2 weeks",
                "success_prob": 0.75,
            }
        )
        add(
            {
                "type": "Immediate (0-1 month)",
                "action": "Draw from strategic inventory (warehouse release)",
                "cost": 25000,
                "risk_mitigation": 65,
                "time": "Immediate",
                "success_prob": 0.9,
            }
        )
        add(
            {
                "type": "Short-term (1-6 months)",
                "action": f"Establish dual sourcing agreements in Spain (and smaller volumes from France) for {target}",
                "cost": 140000,
                "risk_mitigation": 75,
                "time": "3 months",
                "success_prob": 0.6,
            }
        )
        add(
            {
                "type": "Short-term (1-6 months)",
                "action": "Accelerate testing of synthetic lavender alternatives",
                "cost": 70000,
                "risk_mitigation": 55,
                "time": "4 months",
                "success_prob": 0.5,
            }
        )
        add(
            {
                "type": "Long-term (6+ months)",
                "action": "Invest in controlled-environment lavender cultivation (greenhouse trials)",
                "cost": 600000,
                "risk_mitigation": 90,
                "time": "1-2 years",
                "success_prob": 0.6,
            }
        )
    elif scenario == "🏛️ Bulgarian Political Crisis":
        target = "Rose"
        add(
            {
                "type": "Immediate (0-1 month)",
                "action": f"Activate alternative suppliers in Turkey and Morocco for {target}",
                "cost": 80000,
                "risk_mitigation": 80,
                "time": "2-3 weeks",
                "success_prob": 0.7,
            }
        )
        add(
            {
                "type": "Immediate (0-1 month)",
                "action": "Implement customer allocation matrix prioritising key SKUs",
                "cost": 15000,
                "risk_mitigation": 60,
                "time": "1 week",
                "success_prob": 0.85,
            }
        )
        add(
            {
                "type": "Short-term (1-6 months)",
                "action": "Lock forward contracts with Turkey suppliers and options in Morocco",
                "cost": 100000,
                "risk_mitigation": 70,
                "time": "2 months",
                "success_prob": 0.7,
            }
        )
        add(
            {
                "type": "Long-term (6+ months)",
                "action": "Develop supplier partnerships in climate-resilient regions and diversify processing capacity",
                "cost": 350000,
                "risk_mitigation": 85,
                "time": "1-2 years",
                "success_prob": 0.65,
            }
        )
    elif scenario == "📜 India Export Ban Extension":
        target = "Sandalwood"
        add(
            {
                "type": "Immediate (0-1 month)",
                "action": f"Activate alternative suppliers in Australia and source existing stockpiles for {target}",
                "cost": 90000,
                "risk_mitigation": 78,
                "time": "2 weeks",
                "success_prob": 0.7,
            }
        )
        add(
            {
                "type": "Short-term (1-6 months)",
                "action": "Accelerate synthetic sandalwood alternatives and formulation testing",
                "cost": 150000,
                "risk_mitigation": 60,
                "time": "4-6 months",
                "success_prob": 0.55,
            }
        )
        add(
            {
                "type": "Long-term (6+ months)",
                "action": "Invest in plantations/partnerships in Australia and Australia-Pacific sourcing",
                "cost": 800000,
                "risk_mitigation": 88,
                "time": "2+ years",
                "success_prob": 0.6,
            }
        )
    elif scenario == "🚢 Suez Canal Disruption":
        target = "Shipping"
        add(
            {
                "type": "Immediate (0-1 month)",
                "action": "Reroute critical shipments, consider air freight for high-value SKU",
                "cost": 120000,
                "risk_mitigation": 70,
                "time": "Immediate",
                "success_prob": 0.6,
            }
        )
        add(
            {
                "type": "Short-term (1-6 months)",
                "action": "Increase regional sourcing and build short-term warehousing closer to demand",
                "cost": 200000,
                "risk_mitigation": 65,
                "time": "3 months",
                "success_prob": 0.6,
            }
        )
        add(
            {
                "type": "Long-term (6+ months)",
                "action": "Nearshoring and strategic inventory buffers for critical ingredients",
                "cost": 700000,
                "risk_mitigation": 90,
                "time": "1-2 years",
                "success_prob": 0.7,
            }
        )
    else:
        add(
            {
                "type": "Immediate (0-1 month)",
                "action": "Activate alternative suppliers and release strategic inventory",
                "cost": 50000,
                "risk_mitigation": 70,
                "time": "2 weeks",
                "success_prob": 0.7,
            }
        )
        add(
            {
                "type": "Long-term (6+ months)",
                "action": "Diversify suppliers and invest in resilience",
                "cost": 300000,
                "risk_mitigation": 80,
                "time": "1 year",
                "success_prob": 0.6,
            }
        )

    severity_factor = min(max(effects.get("final_price", 0) / 100.0, 0.2), 1.5)
    for r in recs:
        base = r.get("success_prob", 0.6)
        adjusted = max(
            0.05, min(0.95, base * (1.0 - (severity_factor - 0.6) * 0.2))
        )
        r["success_prob"] = round(adjusted, 2)

    return recs


def show_strategic_recommendations():
    st.subheader("💡 Strategic Actions")
    st.write("Prescriptive recommendations for supply chain resilience.")
    scenario = st.selectbox(
        "Scenario",
        [
            "🌪️ Extreme Weather in Provence",
            "🏛️ Bulgarian Political Crisis",
            "📜 India Export Ban Extension",
            "🚢 Suez Canal Disruption",
        ],
    )

    effects = causal_inference_engine(scenario)
    st.markdown(
        """
        **Downstream Effects (what these numbers mean)**

        - `harvest_yield` (%): estimated percent change in harvest yield relative to baseline (negative means reduced yield).
        - `labour_costs` (%): expected percent change in labour-related costs (positive means higher costs).
        - `processing_delays` (%): expected percent increase in processing lead times or delays.
        - `final_price` (%): estimated percent change in final ingredient price used to quantify severity.
        - `confidence_interval` (low, high): plausible range for the `final_price` estimate.

        Interpretation & usage:
        - These outputs are scenario-level, directional estimates from the demo causal engine. Use them to prioritise mitigations and to inform the Cost Impact Calculator.
        - `final_price` and its confidence interval are particularly useful when scaling cost or revenue impact estimates.
        - For production planning, combine these estimates with SKU-level margins, inventory buffers, and contractual terms.
        """
    )
    st.write("**Downstream Effects:**")
    st.json(effects)

    recs = generate_recommendations(scenario, effects)
    for r in recs:
        st.markdown(f"**{r['type']}**: {r['action']}")
        st.write(f"- Implementation cost: €{r['cost']:,.0f}")
        st.write(f"- Risk mitigation score: {r['risk_mitigation']}")
        st.write(f"- Time to implement: {r['time']}")
        st.write(f"- Success probability: {int(r['success_prob']*100)}%")
        st.markdown("---")
