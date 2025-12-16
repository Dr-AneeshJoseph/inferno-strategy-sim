from inferno.simulator import InfernoSimulator

sim = InfernoSimulator()

decision = "Pivot our software from a $500 One-Time License to a $20/month Subscription."

# MOCK LLM OUTPUT
# The AI predicts the 'Valley of Death' before the success.
mock_llm_json = """
[
  {
    "order": 1, 
    "stakeholder": "Cash Flow", 
    "impact": "Negative", 
    "description": "Immediate revenue crashes by 60% as large upfront payments stop."
  },
  {
    "order": 1, 
    "stakeholder": "Old Users", 
    "impact": "Negative", 
    "description": "Legacy users complain about 'renting' software."
  },
  {
    "order": 2, 
    "stakeholder": "Valuation", 
    "impact": "Positive", 
    "description": "Investors re-rate the company higher due to Recurring Revenue (ARR)."
  },
  {
    "order": 3, 
    "stakeholder": "Revenue", 
    "impact": "Positive", 
    "description": "Lifetime Value (LTV) per customer doubles; revenue stabilizes at 2x previous levels."
  }
]
"""

result = sim.run_simulation(decision, mock_llm_json)

print(f"DECISION: {result['decision']}")
print(f"VERDICT: {result['analysis']['verdict']}")
print(f"SCORE: {result['analysis']['net_strategic_score']}")
print("\n--- WARNINGS ---")
# Even though the outcome is good, Inferno will warn about the Order 1 risk
for w in result['analysis']['critical_warnings']:
    print(w)

# EXPECTED OUTPUT:
# VERDICT: SUSTAINABLE (Because Order 3 is highly positive)
# WARNING: [SHORT-TERM RISK] Revenue crashes... (The simulator flags the dangerous transition period)
