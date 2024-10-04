def main():
    menu = '''
    ***** MENU *****
    Brewed     $2.75
    Americano   3.25
    Cappuccino  3.50
    Latte       4.00
    Extra shot  0.75
    *****************
    '''
    drinks = { 'brewed':2.75, 'americano': 3.25, 'cappuccino':3.50, 'latte':4.00, 'extra shot':0.75 }
    print(menu)
    
    order = []
    total = 0.00
    coffee = input("What would you like to order? ")
    while coffee != "no":                           #Add coffee to order if it's on the menu
        if(coffee.lower() in drinks):
            total += drinks[coffee.lower()]
            order.append(coffee.lower())
            print("God it! One " + coffee + " coming right up!")
        else:                                       #Otherwise, prompt other order
            print("Sorry, that isn't on our menu :(")
        coffee = input("Anything else? ")

    print("Great! Your order is:")

    for drink in order:
        print("  " + drink.ljust(11) + " | $" + str(format(drinks[drink], ".2f")))
    
    print("TOTAL: $" + str(format(total, ".2f")))


    # TODO: print the itemized list of drinks and the total bill

main()
