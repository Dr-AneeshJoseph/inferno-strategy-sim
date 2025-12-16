
# 🔥 I.N.F.E.R.N.O. (Strategy Simulator)

> **The 3rd-Order Consequence Engine.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## ⚠️ The Problem
Decisions are often made based on **Order 1** effects ("We save money now").
However, **Order 2 and 3** effects ("Customers leave later") often destroy the value created.

## 🛡️ The Solution
**I.N.F.E.R.N.O.** (Loop 5.5) is a decision support system that forces an LLM to hallucinate the future consequences of a decision across 3 time horizons. It then mathematically weighs the long-term risks heavier than short-term gains.

## 🚀 Quick Start
```python
from inferno.simulator import InfernoSimulator
# See examples/layoff_decision.py
