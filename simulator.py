import os
import json
from .lens.forecaster import CascadeForecaster

class InfernoSimulator:
    def __init__(self):
        self.forecaster = CascadeForecaster()
        
        # Load Prompt
        prompt_path = os.path.join(os.path.dirname(__file__), 'prompts', 'cascade_kernel.md')
        with open(prompt_path, 'r') as f:
            self.system_prompt = f.read()

    def run_simulation(self, decision_text: str, llm_output_json: str):
        """
        Takes the LLM's predicted cascade and scores it.
        """
        try:
            # 1. Parse Simulation
            cascade = json.loads(llm_output_json)
            
            # 2. Score the Strategy
            analysis = self.forecaster.analyze_blast_radius(cascade)
            
            return {
                "decision": decision_text,
                "analysis": analysis,
                "raw_cascade": cascade
            }
        except Exception as e:
            return {"error": str(e)}

    def construct_prompt(self, decision: str):
        return f"{self.system_prompt}\n\nDECISION TO SIMULATE:\n{decision}"
      
