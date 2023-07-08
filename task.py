while True:
    # Receive user commands
    user_command = receive_user_command()

    if user_command == "fetch object":
        # Perform the action to fetch an object
        fetch_object()

    elif user_command == "do something else":
        # Perform some other action
        do_something_else()

    elif user_command == "exit":
        # Exit the program
        break