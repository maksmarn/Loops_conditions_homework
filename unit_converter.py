print("Hello and welcome to Unit Converter!")

while True:
    km = int(input("Please enter a number you wish to convert from km to miles: "))

    print(str(km) + " kilometres is equal to "
          + str(km * 0.621371) + " miles.")
    yesorno = input("Would you like to convert some more? (yes/no) ")
    if yesorno.lower() == "no":
        break
    elif yesorno.lower() != "yes":
        print("ERROR")
        break
