"""
Two-Player Pick Up Sticks game, allows two players to take turns and ends when no sticks are left.

"""
#setting up user input and player turn counter
player_turn = 1
starting_sticks = int(input("How many sticks to start with? (10-100): "))
if starting_sticks >= 10 and starting_sticks <= 100:
    print("Great! Let's play.")
    stick_counter = starting_sticks
    
#setting up the loop
while True:

    #if user gives valid input, run the loop and ask how many sticks they wanna take
    if starting_sticks >= 10 and starting_sticks <= 100:
        print()

        #keeping track of stick total and player turns                      
        if stick_counter != 1:
            print("Turn: Player", player_turn)
            player_turn += 1
            if player_turn == 3:
                player_turn -= 2
            print("There are", stick_counter, "sticks on the table.")
            
        if stick_counter == 1:
            print("Turn: Player", player_turn)
            print("There is", stick_counter, "stick on the table.")
        take_stick = int(input("How many sticks do you want to take? (1, 2, or 3): "))

        #check that the user entered good data with stick selection
        if take_stick < 1 or take_stick > 3:
            print("Sorry, that's not a valid number.")

        #make sure user can't take more than amount of sticks left on table
        if take_stick > stick_counter:
            print("There's not that many sticks left.")

        #keep running total of how many sticks are left on the table
        elif take_stick >= 1 and take_stick <= 3:
            stick_counter -= take_stick
        

        #end the game when no sticks are left            
        if stick_counter <= 0:
            print()
            print("There are no sticks left on the table! Game over.")
            print("Player", (player_turn - 1), "wins!")
            break

    #if the user gives invalid input, display error msg and ask user for better data
    else:

        if starting_sticks < 10:
            print("Sorry, that's too few sticks. Try again.")
            starting_sticks = int(input("How many sticks to start with? (10-100): "))
            stick_counter = starting_sticks

            if starting_sticks >= 10 and starting_sticks <= 100:
                print("Great! Let's play.")
                stick_counter = starting_sticks

        elif starting_sticks > 100:
            print("Sorry, that's too many sticks. Try again.")
            starting_sticks = int(input("How many sticks to start with? (10-100): "))
            stick_counter = starting_sticks

            if starting_sticks >= 10 and starting_sticks <= 100:
                print("Great! Let's play.")
                stick_counter = starting_sticks

