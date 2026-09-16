# Causal Inference for Procurement

A Streamlit demo showing how causal modelling can add a "why" layer on top of
traditional predictive procurement analytics, using a synthetic fragrance
ingredient supply chain as the example.

## What it does

- **Overview** — business context and a preview of the synthetic dataset
- **Causal Analysis** — interactive causal graph of the factors driving
  ingredient prices (weather, labour, political stability, export
  regulations, transport, currency)
- **Risk Simulator** — model supply disruption scenarios (e.g. extreme
  weather, political crisis, export bans) and see the impact on price and
  supply availability
- **Strategic Actions** — prescriptive, cost/risk-scored recommendations
  generated from the simulated scenario

All data is synthetically generated in `data.py` (`numpy.random`, fixed seed)
— there is no real vendor, pricing, or client data behind this demo.

## Running it

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project structure

| File | Purpose |
|---|---|
| `app.py` | Entry point / page routing |
| `data.py` | Synthetic fragrance ingredient dataset generator |
| `overview.py` | Overview page |
| `causal.py` | Causal graph visualization |
| `simulator.py` | Risk/disruption simulator |
| `strategic.py` | Causal inference engine + recommendation generator |
| `deck.md`, `notes.md` | Illustrative presentation deck and speaker notes |
| `app_instructions.md` | Original scaffolding prompt used to generate the app |

## License

MIT — see [LICENSE](LICENSE).
