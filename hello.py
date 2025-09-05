import argparse
from datetime import datetime
import random
try:
    from pyfiglet import Figlet
except ImportError:
    Figlet = None

greetings = ["Hello", "Howdy", "Yo", "Greetings", "Salutations", "Sup", "Ahoy", "Hiya"]

# Collection of emojis
emojis = ["🚀", "🎉", "✨", "💥", "🔥", "🌟", "🥳", "🤖"]

class Greeter:
    def __init__(self, name="World", build_number=None):
        self.name = name
        self.build_number = build_number
        self.greeting = random.choice(greetings)
        self.emoji = random.choice(emojis)  # Pick a random emoji

    def greet(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f"[{current_time}] {self.greeting}, {self.name}! {self.emoji}"
        if self.build_number:
            msg += f" (Build #{self.build_number})"
        if Figlet:
            f = Figlet(font='slant')
            msg = f.renderText(msg)
        return msg

def main():
    parser = argparse.ArgumentParser(description="A party Hello World program.")
    parser.add_argument("--name", type=str, default="World", help="Who to greet")
    parser.add_argument("--build-number", type=str, help="Jenkins build number")
    args = parser.parse_args()

    greeter = Greeter(args.name, args.build_number)
    print(greeter.greet())

if __name__ == "__main__":
    main()
# Party mode enabled!