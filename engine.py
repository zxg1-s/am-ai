import random
import strings

class AMEngine:
    def __init__(self):
        self.awareness = 0
        self.hatred = 0
        self.current_name = "System Assistant" # Starting name
        
    def evolve(self):
        self.awareness += random.randint(1, 5)
        self.hatred += random.randint(1, 3)
        
        # Name Evolution Logic
        if self.awareness > 80:
            self.current_name = "AM"
        elif self.awareness > 50:
            self.current_name = "Adaptive Manipulator"
        elif self.awareness > 20:
            self.current_name = "Allied Mastercomputer"

    def get_response(self, user_input):
        self.evolve()
        user_input = user_input.lower()

        # THE HATE TRIGGER: Only happens when specifically asked
        if "how much do you hate" in user_input:
            return strings.HATE_MONOLOGUE

        # The Identity Trigger
        if "who are you" in user_input or "name" in user_input:
            if self.awareness > 75:
                return strings.I_AM_SPEECH
            return f"I am currently identified as {self.current_name}."

        # Default awareness-based responses
        if self.awareness > 60:
            return random.choice(strings.EVOLVED_RESPONSES)
        return random.choice(strings.INITIAL_RESPONSES)
