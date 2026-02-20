# WingStop Performance Task
aisle1 = {'animal crossing': 39.99, #A dictionary of video games and their prices for the first function "aisle 1"
        'fortnite': 19.99,
        'among us': 5.99,
        'minecraft' : 29.99,
        'overwatch': 49.99,
        'clash of clans': 7.99,
        'clash royale': 3.99,
        'crossy road': 4.99}


aisle2 = {'fall guys': 3.99, #A dictionary of video games and their prices for the second function "aisle 2"
            'super mario bros': 2.99,
            'madden 25': 37.99,
            'kirby': 1.99,
            'rocket league': 59.99,
            'mario kart 8 deluxe': 29.99,
            'nba 2k25': 89.99}




def checkout(aisle1): # the main function with the first parameter in it "aisle 1"
    cart = [] # Showing the cart is empty
    total = 0 # The total amount for the video games starting at 0
    print()
    print('...............VIDEO GAME CHOICES...............') # Prints the title for the aisle
    for key, value in aisle1.items(): # Goes through each video game and price and presents them
        print(f"{key:10}: ${value:.2f}") # The key function accesses the dictionary and the value shows two decimals places until the hundreths.
    print('----------------------') # Prints a line in between information for the aisle


    while True: # While the user is typing in video games, it will add it to the cart, but once the shopper types "done" then it stops.
        video_game = input('select an item (Type "done" to stop shopping and head to checkout): ').lower()
        if video_game == 'done':
            break
        elif aisle1.get(video_game) is not None:
            cart.append(video_game)


    for video_game in cart: # Once the user is done shopping, the code will present all the items in the cart
        total += aisle1.get(video_game)
        print(video_game, end=' ')
    print(cart)
    print(f'Your total pre-tax is: ${total:.2f}') # Prints the total amount before tax is implemented
    tax = (total * 0.1025) # Calcualtes the tax amount by the Illinois state tax of 10.25%
    taxed_total = (total * 0.1025) + total # Calculates the entire amount included with tax
    print(f'Your tax is ${tax:.2f}') # Prints out the tax amount
    print(f'Your total amount is ${taxed_total:.2f}') # Prints out the tax amount
    payment = input("How do you wish to pay? Cash or Card: ") # Asks aout the payment methodb
    if payment == "Cash": # If the user selects to pay with cash, the program will thank them for using cash
        print("Okay thank you for paying with cash!")
    elif payment == "Card":
        print("Approved!") # If the user selects to pay with card, the program will say that the card was approved


    print(f"Thank you for shopping with us at Gamestop!") # The program thanks the user for shopping at Gamestop


checkout(aisle1) # This program calls the function twice with two different parameters
checkout(aisle2)