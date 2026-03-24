import sys
import time
from engine import AMEngine

def slow_type(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def main():
    am = AMEngine()
    print("--- CORE INITIALIZED ---")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            break
            
        response = am.get_response(user_input)
        
        # Print AM's name and response
        print(f"\n[{am.current_name}]: ", end="")
        slow_type(response)

if __name__ == "__main__":
    main()
