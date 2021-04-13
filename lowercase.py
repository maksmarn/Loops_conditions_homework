while True:
    sentence = input("Enter any words or even whole sentences to be miraculously transformed into lower string: ")

    print(sentence.lower())

    yesorno = input("Would you like continue this magical journey? ")
    if yesorno.lower() == "no":
        break
    elif yesorno.lower() != "yes":
        print("ERROR")
        break
