#Ryan Pool
#9.11.24


import random

def eliminateOptions(options, count):
    # While there is more than one option in the list, keep eliminating
    index = 0
    while len(options) > 1:
        # Calculate the index of the option to eliminate using the count
        index = (index + count - 1) % len(options)
        eliminated = options.pop(index)
        print(f"Eliminated: {eliminated}")


def mashGame():
    # Default MASH options for housing
    mashOptions = ["Mansion", "Apartment", "Shack", "House"]

    # Collecting user input for different categories
    print("Welcome to the MASH Game!")

    # Asking for custom options in categories
    jobs = [input(f"Enter job option {i + 1}: ") for i in range(4)]
    spouses = [input(f"Enter spouse name option {i + 1}: ") for i in range(4)]
    cars = [input(f"Enter car option {i + 1}: ") for i in range(4)]
    money = [input(f"Enter amount of money option {i + 1}: ") for i in range(4)]
    kids = [input(f"Enter a number of kids option {i + 1}: ") for i in range(4)]

    # Add the default MASH housing options to the game
    categories = {
        "House": mashOptions,
        "Job": jobs,
        "Spouse": spouses,
        "Car": cars,
        "Money": money,
        "Kids": kids
    }

    # Ask the user for a number to use for elimination
    count = int(input("\nPick a number for the elimination process: "))

    print("\nEliminating options...\n")

    # Eliminate options in each category based on the user's number
    for category, options in categories.items():
        print(f"\nEliminating from {category}:")
        eliminateOptions(options, count)

    # Final result after elimination
    house = mashOptions[0]
    job = jobs[0]
    spouse = spouses[0]
    car = cars[0]
    money = money[0]
    numKids = kids[0]

    # Display the final result
    print("\nYour MASH results are in:")
    print(f"You will live in a {house}.")
    print(f"You will work as a {job}.")
    print(f"You will marry {spouse}.")
    print(f"You will drive a {car}.")
    print(f"You will have {money} money.")
    print(f"You will have {numKids} kids.")


# Run the game
mashGame()