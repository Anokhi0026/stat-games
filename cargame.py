import random
import time

def roll_die():
    """Simulate rolling a die."""
    return random.randint(1, 6)

def display_race_positions(positions):
    """Display the current positions of all players."""
    for i, pos in enumerate(positions):
        print(f"Car {i+1}: {'-' * pos}{'>'}")
    print("\n")

def race(num_cars, finish_line):
    """Simulate a race between multiple cars."""
    # Initialize positions
    positions = [0] * num_cars
    
    while True:
        for i in range(num_cars):
            input(f"Car {i+1}, press Enter to roll the die...")
            roll = roll_die()
            positions[i] += roll
            print(f"Car {i+1} rolled a {roll} and moved to position {positions[i]}.")
            
            # Display the current positions
            display_race_positions(positions)
            
            # Check for winner
            if positions[i] >= finish_line:
                print(f"Car {i+1} wins the race with a final position of {positions[i]}!")
                return
        
        # Small delay for better readability
        time.sleep(1)

def main():
    print("Welcome to the Car Racing Game!")
    num_cars = int(input("Enter the number of cars: "))
    finish_line = int(input("Enter the finish line position: "))
    
    race(num_cars, finish_line)

if __name__ == "__main__":
    main()
