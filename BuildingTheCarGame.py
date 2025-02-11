command = ""

while command != "quit":
    command = input("> ").lower()
    if command.lower() == "help":
        print("Car started...")
    elif command.lower() == "stop":
        print("Car stopped.")
    elif command.lower() == "stop":
        print("Car stopped.")
    elif command.lower() == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    else:
        print("sorry i don't understand...")