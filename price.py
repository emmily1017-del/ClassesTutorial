#Items avaible and the prices
shopping_items = {
    "Soda" : 5.99,
    "Fruit" : 2.99,
    "Chicken" : 8.99,
    "Candy" : 1.99,
    "Vegetables" : 3.99,
}
#shopping cart
shopping_cart = {
    "Mango" : 4.55

}
#Avalibilty Function
def check_availabilty(item):
    return item in shopping_items
#Shopping cart
while True:
    empty_cart = input("What do you want to do? Shop or Exit? ")
    if empty_cart.lower() == "exit":
        break
    if empty_cart.lower() != "shop":
        print("Please enter Shop or Exit.")
        continue

    while True:
        print("Cart Options")
        print("1. Add items")
        print("2. Remove items")
        print("3. Clear Cart")
        print("4. Show list")
        print("5. Back to Shop or Exit")

        option = input("Select an option: ")
        if option == "1":
            print(f"This is what we have: {shopping_items}")
            selection = input("Select what you want (or type Back): ")
            if selection.lower() == "back":
                continue
            if check_availabilty(selection):
                shopping_cart[selection] = shopping_items[selection]
                print(f"{selection} Added to cart")
            else:
                print("That item is not available.")
        elif option == "2":
            print(", ".join(shopping_items))
            withdraw_item = input("What do you want to remove (or type Back)? ")
            if withdraw_item.lower() == "back":
                continue
            if withdraw_item == "Soda":
                print("Soda removed")
            elif withdraw_item == "Fruit":
                print("Fruit removed")
            elif withdraw_item == "Chicken":
                print("Chicken removed")
            elif withdraw_item == "Candy":
                print("Candy removed")
            elif withdraw_item == "Vegetables":
                print("Vegetables removed")
        elif option == "3":
            print("Items cleared")
        elif option == "4":
            print(f"This is what your shopping cart has: {shopping_cart}")
        elif option == "5":
            break
        else:
            print("Please select an option from 1 to 5.")
