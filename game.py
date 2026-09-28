player_name="emmily"
player_health=100
player_inventory=["map"]
is_alive=True

while(player_health>0):
    print(f"\n--- {player_name}'s Health: {player_health} ---")
    player_response=int(input("Do you want to (1) Explore or (2) Rest?"))
    if player_response == 1:
        print("You have found a hidden chest")
        player_health -= 10
    elif player_response == 2:
        print("You rested and recovered health")
        player_health += 20
    else:
        print("invalid response")
        for x in player_inventory:
            print(x)


else:
    print("You exited successfully\n")
    is_alive=False
    print(is_alive)