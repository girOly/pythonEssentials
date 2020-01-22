command = ''
car_running = False
while True:
    command = input("> ").lower()
    if command == "start":
        if car_running is True:
            print("She's a runnin!")
        else:
            print("Vroom.. Vroom..")
            car_running = True
    elif command == "stop":
        if car_running is False:
            print("Hey it's stopped!")
        else:
            print("Car stopped")
            car_running = False
    elif command == "help":
        print('''
start - to start the Car
stop - to stop the Car
quit - quit

        ''')
    elif command == "quit":
        break
    else:
        print("I don't understand")
