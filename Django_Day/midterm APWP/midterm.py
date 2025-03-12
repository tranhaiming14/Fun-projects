import threading

class Tank:
    def __init__(self, damage, hp, armor, price, id):
        self.damage = damage
        self.hp = hp
        self.armor = armor
        self.price = price
        self.id = id

    def __repr__(self):
        return f'Tank(ID: {self.id}, Damage: {self.damage}, HP: {self.hp}, Armor: {self.armor}, Price: {self.price})'

def read_tanks_from_file(filename):
    tanks = []
    with open(filename, 'r') as file:
        num_tanks = int(file.readline().strip())
        for i in range(num_tanks):
            line = file.readline().strip().split()
            damage, hp, armor = map(int, line[:3])
            price = int(line[3])
            tanks.append(Tank(damage, hp, armor, price, i + 1))
    return tanks

def sort_tanks(tanks):
    # Sort by price
    tanks_sorted_by_price = sorted(tanks, key=lambda x: (x.price, -x.damage))
    # Sort by damage
    tanks_sorted_by_damage = sorted(tanks, key=lambda x: (-x.damage, x.price))
    return tanks_sorted_by_price, tanks_sorted_by_damage

def write_results_to_file(tanks_price, tanks_damage, output_filename):
    with open(output_filename, 'w') as file:
        file.write("Sorted by Price:\n")
        for tank in tanks_price:
            file.write(f'{tank.id}\n')
        
        file.write("\nSorted by Damage:\n")
        for tank in tanks_damage:
            file.write(f'{tank.id}\n')

def process_tanks(input_filename, output_filename):
    tanks = read_tanks_from_file(input_filename)
    tanks_sorted_by_price, tanks_sorted_by_damage = sort_tanks(tanks)
    write_results_to_file(tanks_sorted_by_price, tanks_sorted_by_damage, output_filename)

# Main thread
if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = 'output.txt'

    # Create a thread to process tanks
    tank_thread = threading.Thread(target=process_tanks, args=(input_file, output_file))
    tank_thread.start()
    tank_thread.join()  # Wait for the thread to finish

    print(f'Tank processing completed. Results written to {output_file}.')