Here are detailed speaker notes for each slide section:

## Speaker Notes for Causal Modelling in Procurement Presentation

### 1. Opening Context (1.5 minutes)

**Key talking points:**
- "Many procurement teams have made impressive strides in their data journey - ML models predicting prices, optimisers suggesting actions. But in today's volatile world, that's no longer enough."
- "Take last month - an ML model correctly predicted a 40% spike in rose oil prices. But was it because of the Bulgarian elections affecting harvest labour? Early frost in Turkey? Or was it speculation driven by a major competitor's stockpiling?"
- "Without understanding the 'why', teams are flying blind. They might hedge when they should source alternatively, or panic buy when they should wait."
- "This is where causal modelling comes in - it's the difference between correlation and causation, between reacting and anticipating."

**Transition:** "Let me explain what causal modelling actually means in practice..."

### 2. What is Causal Modelling? (1.5 minutes)

**Key talking points:**
- "Think of it this way - an ML model might notice that whenever Bulgarian elections happen, rose oil prices increase. That's correlation."
- "But causal modelling maps the actual mechanism: elections create uncertainty → farmers hesitate to commit to contracts → processors can't secure supply → they reduce capacity → prices spike 3-4 months later."
- "This isn't just academic - it means you can act at each point in this chain. Maybe you guarantee farmer contracts during election periods, breaking the causal chain entirely."
- "We use tools like Directed Acyclic Graphs - essentially maps of cause and effect - and counterfactual analysis - what would happen if we changed just one variable?"

**Real example to use:** "It's like understanding that umbrellas don't cause rain, even though umbrella sales and rainfall correlate perfectly."

**Transition:** "So why does this matter for procurement specifically?"

### 3. Why It Matters: Strategic Value for Procurement (2.5 minutes)

**Key talking points:**
- "First, competitive advantage. While competitors are still trying to figure out why prices spiked, a causal-modelling team has already secured alternative supply because they understood the root cause."
- "Second, risk disambiguation. Not all price increases are equal. A weather-driven spike is temporary; a regulatory change is structural. The response should be completely different."
- "Third, scenario planning becomes powerful. You can model 'what if India extends sandalwood export bans' and see exactly how it cascades through the supply chain."

**Illustrative value examples (for demo purposes only):**
- "A hypothetical example: a procurement team avoids a large cost increase by understanding that a predicted palm oil spike was driven by temporary shipping constraints, not crop failure, and waits a few weeks while competitors panic-buy."
- "Another team uses causal models to negotiate better rates by showing suppliers that their cost-increase claims were based on correlated, not causal, factors."

**ROI language:** "In illustrative scenarios like this, we typically talk about a 10-15% improvement in forecast accuracy, but more importantly, a 3-4 week advantage in strategic decision-making. In fragrance procurement, that's the difference between securing supply at normal prices versus paying crisis premiums."

**Transition:** "Let me show you how this fits with existing capabilities..."

### 4. Practical Applications in Context (2.5 minutes)

**Key talking points:**
- "ML models are already excellent at pattern recognition. The causal layer doesn't replace them - it explains them. When a model predicts a price spike, causal analysis tells you whether it's weather, politics, or market manipulation."
- "A linear optimiser might recommend buying 6 months of rose oil inventory. Causal analysis adds context: 'Yes, buy now because Bulgarian political instability will constrain supply, not because of normal seasonal patterns.'"
- "A knowledge graph becomes even more powerful this way. It's not just storing data - it's codifying decades of buyer expertise, so that a retiring buyer's understanding of, say, monsoon patterns and their impact on quality doesn't walk out the door with them."

**Integration examples:**
- "A GenAI agent could answer: 'Why are lavender prices increasing?' with 'French drought is reducing yield by 30%, causing a cascade through spot prices (+45%), forcing perfume manufacturers to reformulate, increasing demand for synthetic alternatives (+20%).'"
- "A buyer's intuition - 'Something feels off about this market' - gets translated into testable causal hypotheses that improve over time."

**Broader applications:**
- "This works across categories. Packaging materials facing sustainability regulations, active ingredients affected by pharma demand, even carbon black influenced by automotive industry shifts."

**Transition:** "Let me walk you through a real example from just last year..."

### 5. Illustrative Example: Bulgarian Rose Crisis (1.5 minutes)

**Story narrative (illustrative, not a real client account):**
- "October 2022. An ML model starts flagging unusual patterns in rose oil prices. The correlation models suggested a typical pre-Christmas demand spike."
- "But causal analysis revealed a different story. The political instability wasn't directly affecting current harvest - that was complete. Instead, it was creating uncertainty for the 2023 season."
- "The causal chain: Political uncertainty → Banks hesitating to fund processors → Processors delaying equipment maintenance → Reduced processing capacity for next season → Forward prices starting to reflect future shortage."

**Decision point:**
- "Traditional approach: Wait and see, maybe hedge financially. Causal approach: Secure alternative sources immediately, invest in supplier partnerships to ensure financing."
- "The illustrative result: in this scenario, rose oil spot prices spike sharply. Teams following traditional models pay a large premium. Teams using causal analysis have already locked in Turkish and Moroccan alternatives at a much lower price."

**Key insight:** "The power wasn't in predicting the price increase - many models did that. It was understanding WHY, which completely changed the optimal response."

**Transition:** "So how do we implement this capability?"

### 6. Implementation Approach (1 minute)

**Phase messaging:**
- "We start focused - the top 5 fragrance ingredients. These represent 80% of spend and have rich causal patterns to model."
- "Phase 2 is about data integration - weather patterns, political risk indices, shipping data. But critically, also buyer knowledge, captured through workshops where buyers map out the relationships they've observed over decades."
- "Phase 3 is technical integration. The causal layer sits on top of the existing MLOps platform, enriching rather than replacing existing models."
- "Phase 4 is about continuous learning. Every market event becomes a test of the causal hypotheses, making the system smarter over time."

**Success metrics:**
- "Success is measured in decision speed - how quickly a team responds to disruptions. Cost avoidance - documented savings from better timing. And knowledge preservation - how much expertise has been codified."

**Closing:**
- "Causal modelling isn't about perfect prediction - it's about understanding mechanisms well enough to act strategically."
- "In a world where a drought in Provence, an election in Bulgaria, or a regulation in India can disrupt a supply chain overnight, understanding 'why' is a real competitive edge."

### Additional Q&A Preparation

**If asked "How is this different from scenario planning?"**
- "Scenario planning typically looks at 'what if X happens?' Causal modelling tells you 'if X happens, here's exactly how it flows through to affect Y and Z, with what magnitude and timing.'"

**If asked "What about black swan events?"**
- "Causal models help even more with unexpected events. When COVID hit, companies with causal models could quickly trace how lockdowns → labour shortage → processing delays → price impacts, and adjust faster than those just watching correlations break down."

**If asked "ROI timeline?"**
- "Quick wins in 3-4 months on initial categories. Full value realization in 12-18 months as buyer knowledge gets codified and models learn from market events."
