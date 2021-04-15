print("Hello and welcome to Unit Converter!")
km_to_miles_factor = 0.621371

while True:
    km = int(input("Please enter a number you wish to convert from km to miles: "))

    print(f"{km} kilometres is equal to {km * km_to_miles_factor} miles.")
    should_convert_again_string = input("Would you like to convert some more? (yes/no) ")
    should_convert_again = should_convert_again_string.lower() == "yes"
    if should_convert_again:
        print("All right then.")
    else:
        print("Thank you for using Unit Converter.")
        break
