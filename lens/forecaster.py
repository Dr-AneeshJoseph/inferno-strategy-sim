class CascadeForecaster:
    """
    Implements Loop 5.5: 3rd Order Consequence Analysis.
    """
    
    def analyze_blast_radius(self, cascade_data: list):
        """
        Calculates the Net Strategic Value (NSV).
        """
        score = 0
        warnings = []
        
        for event in cascade_data:
            # Weighting: Long term (Order 3) is HEAVIER than short term.
            # Most people ignore Order 3, so we double its weight to force attention.
            weight = 1.0
            if event['order'] == 2: weight = 1.5
            if event['order'] == 3: weight = 2.0
            
            impact_val = 1 if event['impact'] == "Positive" else -1
            score += (impact_val * weight)

            # Flag Critical Risks
            if event['order'] >= 2 and event['impact'] == "Negative":
                warnings.append(f"[LONG-TERM RISK] {event['description']}")

        verdict = "SUSTAINABLE" if score > 0 else "FRAGILE"
        
        return {
            "net_strategic_score": score,
            "verdict": verdict,
            "critical_warnings": warnings
        }
      
