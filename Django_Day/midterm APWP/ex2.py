import threading

class Character:
    def __init__(self, name, level, experience, health):
        self.name = name
        self.level = level
        self.experience = experience
        self.health = health

class PlayerCharacter(Character):
    def __init__(self, name, level, experience, health, inventory):
        super().__init__(name, level, experience, health)
        self.inventory = inventory

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Level: {self.level}\n")
            file.write(f"Experience: {self.experience}\n")
            file.write(f"Health: {self.health}\n")
            file.write(f"Inventory: {', '.join(self.inventory)}\n")

    def save_in_background(self, filename):
        thread = threading.Thread(target=self.save_to_file, args=(filename,))
        thread.start()

# Example Usage
player_character = PlayerCharacter("Warrior", 5, 2, 80, ["Sword", "Shield"])
player_character.save_in_background("player.txt")

# Optionally, wait for the thread to complete
# thread.join()  # Uncomment if you want to wait for the background save to finish