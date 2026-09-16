import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import networkx as nx


def display_causal_graph():
    st.subheader("🔗 Causal Analysis")
    st.write("Explore the causal relationships in the fragrance supply chain.")
    # Define nodes and edges
    nodes = [
        Node(id="Weather", label="Weather Events", color="blue"),
        Node(id="Harvest", label="Harvest Yield", color="green"),
        Node(id="Labour", label="Labour Availability", color="green"),
        Node(id="Processing", label="Processing Capacity", color="green"),
        Node(id="Transport", label="Transportation Costs", color="green"),
        Node(id="Currency", label="Currency Fluctuations", color="blue"),
        Node(id="Political", label="Political Stability", color="blue"),
        Node(id="Export", label="Export Regulations", color="blue"),
        Node(id="Price", label="Final Ingredient Price", color="orange"),
    ]
    edges = [
        Edge(source="Weather", target="Harvest", label="0.7"),
        Edge(source="Harvest", target="Processing", label="0.6"),
        Edge(source="Labour", target="Harvest", label="0.5"),
        Edge(source="Processing", target="Transport", label="0.4"),
        Edge(source="Transport", target="Price", label="0.5"),
        Edge(source="Currency", target="Price", label="0.3"),
        Edge(source="Political", target="Export", label="0.8"),
        Edge(source="Export", target="Price", label="0.6"),
        Edge(source="Harvest", target="Price", label="0.7"),
    ]
    config = Config(
        width=900,
        height=500,
        directed=True,
        nodeHighlightBehavior=True,
        highlightColor="#F7A7A6",
        collapsible=True,
    )
    selected = agraph(nodes=nodes, edges=edges, config=config)
    if selected:
        if isinstance(selected, dict):
            node_id = selected.get("id") or selected.get("key") or ""
            node_label = selected.get("label") or selected.get("id") or node_id
        else:
            node_id = selected
            node_label = next(
                (n.label for n in nodes if n.id == node_id), node_id
            )

        st.sidebar.markdown(f"**Node Selected:** {node_label}")
        explanations = {
            "Weather Events": "Weather impacts harvest yield and supply reliability.",
            "Harvest Yield": "Determines available volume and price.",
            "Labour Availability": "Affects harvest and processing speed.",
            "Processing Capacity": "Limits throughput and can cause delays.",
            "Transportation Costs": "Influences final price and delivery.",
            "Currency Fluctuations": "Affects international pricing.",
            "Political Stability": "Can disrupt supply and export.",
            "Export Regulations": "May restrict ingredient flow.",
            "Final Ingredient Price": "Result of all upstream factors.",
        }
        st.sidebar.info(
            explanations.get(
                node_label, "No detailed explanation available for this node."
            )
        )

    # Trace causal path feature
    st.markdown("---")
    st.markdown("**Trace Causal Path**")
    start_node = st.selectbox("Start Node", [n.label for n in nodes])
    end_node = st.selectbox("End Node", [n.label for n in nodes])
    if st.button("Trace Path"):
        G = nx.DiGraph()
        for e in edges:
            src = (
                getattr(e, "source", None)
                or getattr(e, "from", None)
                or getattr(e, "start", None)
            )
            tgt = (
                getattr(e, "target", None)
                or getattr(e, "to", None)
                or getattr(e, "end", None)
            )
            if src is None and isinstance(e, (tuple, list)) and len(e) >= 2:
                src, tgt = e[0], e[1]
            if src is None or tgt is None:
                try:
                    src = e.get("source") if hasattr(e, "get") else src
                    tgt = e.get("target") if hasattr(e, "get") else tgt
                except Exception:
                    pass
            if src and tgt:
                G.add_edge(src, tgt)
        try:
            path = nx.shortest_path(
                G,
                source=[n.id for n in nodes if n.label == start_node][0],
                target=[n.id for n in nodes if n.label == end_node][0],
            )
            st.success(
                " → ".join(
                    [
                        next(n.label for n in nodes if n.id == pid)
                        for pid in path
                    ]
                )
            )
        except Exception:
            st.error("No path found.")
