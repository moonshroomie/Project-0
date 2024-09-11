import sys
import time

class Character:
    """
    Represents a character in the game.
    """
    
    class Colors:
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        BRIGHT_BLACK = '\033[90m'
        BRIGHT_RED = '\033[91m'
        BRIGHT_GREEN = '\033[92m'
        BRIGHT_YELLOW = '\033[93m'
        BRIGHT_BLUE = '\033[94m'
        BRIGHT_MAGENTA = '\033[95m'
        BRIGHT_CYAN = '\033[96m'
        BRIGHT_WHITE = '\033[97m'
        RESET = '\033[0m'  # Resets the color to default

    def __init__(self, name, health, inventory, dialogue):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.dialogue = dialogue

    def typewriter_effect(self, text, delay=0.1, color=Colors.RESET):
        # Ensure delay is a float and not a string
        try:
            delay = float(delay)
        except ValueError:
            print("Invalid delay value.")
            return
        
        for char in text:
            sys.stdout.write(f"{color}{char}{self.Colors.RESET}")
            sys.stdout.flush()  # Ensures the output is displayed immediately
            time.sleep(delay)  # Sleep for the given delay
        print()  # Move to the next line after the text is printed

    def talk_to_player(self, message_key):
        if message_key in self.dialogue:
            # Ensure the tuple contains text, color, and delay
            try:
                text, color, delay = self.dialogue[message_key]
                self.typewriter_effect(text, delay, color)
            except (ValueError, TypeError):
                print(f"Error: Incorrect dialogue format for '{message_key}'")
        else:
            print("I don't know what to say.")

    def show_inventory(self):
        if not self.inventory:
            print()
            self.typewriter_effect("Your inventory is empty.", delay=0.04, color=self.Colors.CYAN)
            print()
        else:
            print()
            self.typewriter_effect("Your inventory contains:", delay=0.04, color=self.Colors.CYAN)
            for item in self.inventory:
                self.typewriter_effect(f"- {item.name}: {item.description}", delay=0.04, color=self.Colors.CYAN)
                print()

    def receive_item(self, item):
        self.inventory.append(item)