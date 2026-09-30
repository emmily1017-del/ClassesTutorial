
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

}
#Avalibilty Function
def check_availabilty(item):
    if(shopping_items[item]):
        return True
    else:
        return False
#Shopping cart
empty_cart=(input("What do you want to do? Shop or Exit?"))
while True:
    if empty_cart == "Shop":
        print("Cart Options")
        print("1. Add items")
        print("2. Remove items")
        print("3. Clear Cart")
        print("4. Show list")
        print("5. Exit")
    #Shopping cart options
    option=int(input("Select an option:"))
    if option == 1:
        print(f"This is what we have: {shopping_items}")
        selection=input("Select what you want: ")
        if (check_availabilty(selection)):
            shopping_cart[selection]=shopping_items[selection]
            print(f"{selection} Added to cart")
        continue        
    elif option == 2:
        print ("Soda, Fruit, Chicken, Candy, Vegetable")
        withdraw_item=(input("What do you want to remove?"))
        if withdraw_item == "Soda":
            shopping_cart.pop('Soda')
        elif withdraw_item == "Fruit":
            shopping_cart.pop('Fruit')
        elif withdraw_item == "Chicken":
            shopping_cart.pop('Chicken')
        elif withdraw_item == "Candy":
            shopping_cart.pop('Candy')
        elif withdraw_item == "Vegetable":
            shopping_cart.pop('Vegetable')
        continue
    elif option == 3:
        print("Items cleared")
        continue
    elif option == 4:
        print(f"This is what your shopping cart has: {shopping_cart}")
        continue
    elif option == 5:
        print("Exiting...")
        break