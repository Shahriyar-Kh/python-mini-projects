import random

def roll_dice(num_sides, num_rolls):
    results = []
    for _ in range(num_rolls):
        roll = random.randint(1, num_sides)
        results.append(roll)
    return results

def main():
    # Ask the user for the number of sides on the dice
    num_sides = int(input("Enter the number of sides on the dice: "))
    # Ask the user for the number of rolls
    num_rolls = int(input("Enter the number of rolls: "))
    
    # Roll the dice and get the results
    results = roll_dice(num_sides, num_rolls)
    
    # Display the results
    print("Results of the dice rolls:")
    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")

if __name__ == "__main__":
    main()
