while True:
    # Receive movement commands
    command = receive_movement_command()

    if command == "forward":
        # Move robot forward
        move_forward()

    elif command == "backward":
        # Move robot backward
        move_backward()

    elif command == "turn left":
        # Turn robot left
        turn_left()

    elif command == "turn right":
        # Turn robot right
        turn_right()

    elif command == "stop":
        # Stop robot
        stop_robot()

    elif command == "exit":
        # Exit the program
        break