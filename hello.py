import argparse
from datetime import datetime

class Greeter:
    def __init__(self, name="World"):
        self.name = name

    def greet(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{current_time}] Hello, {self.name}!"

def main():
    parser = argparse.ArgumentParser(description="A fancy Hello World program.")
    parser.add_argument("--name", type=str, help="Who to greet", default="Jenkins Majstora")
    args = parser.parse_args()

    greeter = Greeter(args.name)
    print(greeter.greet())

if __name__ == "__main__":
    main()
