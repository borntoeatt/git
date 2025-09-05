import argparse
from datetime import datetime
import random
try:
    from pyfiglet import Figlet
except ImportError:
    Figlet = None

# Optional: fancy ASCII fonts if pyfiglet is installed
f = Figlet(font='slant') if Figlet else None

# Random greetings
greetings = ["Hello", "Howdy", "Yo", "Greetings", "Salutations", "Sup", "Ahoy", "Hiya"]

class Greeter:
    def __init__(self, name="World", greeting=None, build_number=None):
        self.name = name
        self.greeting = greeting or random.choice(greetings)
        self.build_number = build_number

    def greet(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f"[{current_time}] {self.greeting}, {self.name}!"
        if self.build_number:
            msg += f" 🚀 (Build #{self.build_number})"
        if f:
            msg = f.renderText(msg)
        return msg

def main():
    parser = argparse.ArgumentParser(description="A fancy Hello World program.")
    parser.add_argument("--name", type=str, default="World", help="Who to greet")
    parser.add_argument("--greeting", type=str, help="Custom greeting")
    parser.add_argument("--build-number", type=str, help="Jenkins build number")
    args = parser.parse_args()

    greeter = Greeter(args.name, args.greeting, args.build_number)
    print(greeter.greet())

if __name__ == "__main__":
    main()
# This file is for testing purposes only.