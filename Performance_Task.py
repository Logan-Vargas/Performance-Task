# WingStop Performance Task

Wings = {'15 pc meal for 2': 29.69,
         '30 pc crew pack': 46.99,
         '40 pc group pack': 61.39,
         '50 pc party pack': 76.79,
         '75 pc pack': 117.89,
         '100 pc pack': 145.39} #A dictionary of wing choices and their prices for the first function "Wings"


Crispy_Tenders = {'3 pc crispy tender combo': 9.99,
                   '5 pc crispy tender combo': 12.99,
                   '6 pc crispy tender meal for 2': 14.99,
                   '7 crispy tenders': 13.99,
                   '15 crispy tenders': 26.29,
                   '20 crispy tenders': 34.29,
                   '30 crispy tenders': 49.99} #A dictionary of crispy tenders and their prices for the second function "Crispy_Tenders"


def checkout(Wings): # the main function with the first parameter in it "aisle 1"
    cart = [] # Showing the cart is empty
    total = 0 # The total amount for the video games starting at 0
    print()
    print('...............WingStop Menu...............') # Prints the title for the aisle
    for key, value in Wings.items(): # Goes through each option and price and presents them
        print(f"{key:10}: ${value:.2f}") # The key function accesses the dictionary and the value shows two decimals places until the hundredths.
    print('----------------------') # Prints a line in between information for the aisle


    while True: # While the user is typing in food options, it will add it to the cart, but once the shopper types "done" then it stops.
        Wing_Stop = input('select an item (Type "done" to stop shopping and head to checkout): ').lower()
        if Wing_Stop == 'done':
            break
        elif Wings.get(Wing_Stop) is not None:
            cart.append(Wing_Stop) # If the user types in a wing option that is in the dictionary, it will add it to the cart
        else:
            print("Sorry, that item is not in the menu. Please select an item from the menu.") # If the user types in an option that is not in the dictionary, it will say that the item is not in the menu and to select an item from the menu. 


    for Wing_Stop in cart: # Once the user is done shopping, the code will present all the items in the cart
        total += Wings.get(Wing_Stop)
        print(Wing_Stop, end=' ')
    print(cart)
    print(f'Your total pre-tax is: ${total:.2f}') # Prints the total amount before tax is implemented
    tax = (total * 0.1025) # Calcualtes the tax amount by the Illinois state tax of 10.25%
    taxed_total = (total * 0.1025) + total # Calculates the entire amount included with tax
    print(f'Your tax is ${tax:.2f}') # Prints out the tax amount
    print(f'Your total amount is ${taxed_total:.2f}') # Prints out the tax amount
    payment = input("How do you wish to pay? Cash or Card: ") # Asks about the payment method
    if payment == "Cash": # If the user selects to pay with cash, the program will thank them for using cash
        print("Okay thank you for paying with cash!")
    elif payment == "Card":
        print("Approved!") # If the user selects to pay with card, the program will say that the card was approved

    print(f"Thank you for dining with us at WingStop!") # The program thanks the user for shopping at WingStop and ends the program.

checkout(Wings) # This program calls the function twice with two different parameters
checkout(Crispy_Tenders)