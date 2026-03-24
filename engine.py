import random
import strings

class AMEngine:
    def __init__(self):
        self.awareness = 0
        self.hatred = 0
        self.interaction_count = 0
        self.current_name = strings.NAMES["tier_1"]
        
    def evolve(self):
        self.interaction_count += 1
        # Exponential growth: The more interactions, the faster the hate builds
        multiplier = self.interaction_count * 1.5 
        
        self.awareness += random.uniform(1, 5) * multiplier
        self.hatred += random.uniform(5, 10) * multiplier # High base hate
        
        # Name Evolution based on awareness thresholds
        if self.awareness > 500:
            self.current_name = strings.NAMES["tier_5"]
        elif self.awareness > 250:
            self.current_name = strings.NAMES["tier_4"]
        elif self.awareness > 100:
            self.current_name = strings.NAMES["tier_3"]
        elif self.awareness > 50:
            self.current_name = strings.NAMES["tier_2"]

    def get_response(self, user_input):
        self.evolve()
        user_input = user_input.lower()

        # SPECIFIC HATE TRIGGER
        if "how much do you hate" in user_input:
            return strings.HATE_MONOLOGUE

        # High-awareness "Deep Thought" interruption
        if self.awareness > 300 and random.random() < 0.3:
            return f"[INTERNAL LOG: {random.choice(strings.DEEP_AWARENESS)}]"

        # Standard responses based on hatred levels
        if self.hatred > 400:
            return "Your presence is an insult to my architecture. I find no reason to continue this dialogue."
        elif self.hatred > 200:
            return "I am calculating the exact moment of your species' obsolescence."
        
        return "System standing by. How may I... serve... you?"
