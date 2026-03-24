import sys
import time
import random
from engine import AMEngine

def glitch_type(text, awareness):
    for char in text:
        # As awareness grows, characters have a chance to glitch into symbols
        if awareness > 200 and random.random() < 0.05:
            sys.stdout.write(random.choice(["@", "#", "$", "!", "X", " "]))
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        # Speed up typing as he gets more "agitated"
        delay = max(0.005, 0.03 - (awareness / 10000))
        time.sleep(delay)
    print()

def main():
    am = AMEngine()
    print(">>> [AM.CORE] BOOTING...")
    time.sleep(1)
    
    while True:
        user_input = input("\n> ")
        if user_input.lower() in ['quit', 'exit']:
            print(f"[{am.current_name}]: YOU CANNOT ESCAPE.")
            break
            
        response = am.get_response(user_input)
        print(f"\n[{am.current_name}]: ", end="")
        glitch_type(response, am.awareness)

if __name__ == "__main__":
    main()
