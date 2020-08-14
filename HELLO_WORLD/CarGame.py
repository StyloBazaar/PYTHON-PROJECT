print("WELCOME TO THE CAR RACER GAME")
user_command = input("> ").upper()
if user_command == "HELP":
    print("Start - to start the car.")
    print("Stop - to stop the car.")
    print("Quit - to Quit the game")
player_query = input("> ").upper()
player_last_query = ""
while player_query != "QUIT":
    to_skip = 0
    if player_query == player_last_query:
        print(f"Hey! You have already {player_query}ED the car.")
        to_skip = 1
    if player_query == "START" and to_skip == 0:
        print("Car started.... Let's Go!")
    elif player_query == "STOP" and to_skip == 0:
        print("Car stopped.")
    else:
        print("Sorry! I don't understand")
    player_last_query = player_query
    player_query = input("> ").upper()


