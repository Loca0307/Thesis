    messages = {
        "Empty": "****WARNING - YOU ARE OUT OF GAS****\nCalling AAA...",
        "Low": f"Your gas tank is extremely low, checking GPS for the closest gas station...\n"
               f"The closest gas station is {gas_stations()} which is {miles_to_gas_station['Low']} miles away.",
        "Quarter Tank": f"Your gas tank is at a Quarter Tank, checking GPS for the closest gas station...\n"
                        f"The closest gas station is {gas_stations()} which is {miles_to_gas_station['Quarter Tank']} miles away.",
        "Half Tank": "Your gas tank is Half Full, plenty to get to your destination!",
        "Three Quarter Tank": "Your gas tank is Three Quarters Full!",
        "Full Tank": "Your gas tank is FULL, Vroom Vroom!"
    }

    print(messages[gas_level])

print("\n****************************************\n")
print("Gasoline Branch - Developer Linus Riddle\n")