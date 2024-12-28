#!/usr/bin/env python3
"""
Make a terminal program that shows to the user a list of available rooms to rent and the price of each room.
This information is stored in a txt file separated by commas.

'quartos.txt'
```
# code, name, price
1, master suite, 500
2, family room, 200
3, single room, 100
4, simple room, 50
```

The program asks the user a name, which room code he wants to rent and for how many days.
In the end, the program shows the total price of the reservation.

The program should store the reservations in a txt file separated by commas.

'reservas.txt'
```
# client, room, days
Bruno, 3, 12
```

If another client tries to rent the same room, the program should show a message that the room is already rented.
"""
__author__ = "Bruno Chiconato"
__version__ = "0.2"

import time

rooms_txt = {
    "code": [1, 2, 3, 4],
    "name": ["master suite", "family room", "single room", "simple room"],
    "price": [500, 200, 100, 50],
    "available": [True, True, True, True],
}
availabe_rooms = {"code": [], "name": [], "price": [], "available": []}

while True:
    try:
        with open("quartos.txt", "r") as file:
            for line in file:
                code, name, price, available = line.strip().split(", ")
                availabe_rooms["code"].append(int(code))
                availabe_rooms["name"].append(name)
                availabe_rooms["price"].append(int(price))
                availabe_rooms["available"].append(available)
        break
    except FileNotFoundError:
        with open("quartos.txt", "w") as file:
            for i in range(len(rooms_txt["code"])):
                file.write(
                    f"{rooms_txt['code'][i]}, "
                    f"{rooms_txt['name'][i]}, "
                    f"{rooms_txt['price'][i]}, "
                    f"{rooms_txt['available'][i]}\n"
                )

while True:
    try:
        if all(room == "False" for room in availabe_rooms["available"]):
            print("There are no available rooms.")
            break

        print("Available rooms:")

        for i in range(len(availabe_rooms["code"])):
            if availabe_rooms["available"][i] == "True":
                print(
                    f"{availabe_rooms['code'][i]} - {availabe_rooms['name'][i]} - R${availabe_rooms['price'][i]}"
                )

        print("#" * 30)

        client = input("Enter your name: ").strip()

        if not client or any(
            letter.isdigit() or letter.isnumeric() for letter in client
        ):
            raise ValueError

        room = int(input("Enter the room code you want to rent: "))

        if room not in availabe_rooms.get("code"):
            raise ValueError

        if availabe_rooms["available"][room - 1] == "False":
            print("This room is already rented.")
            continue

        days = int(input("Enter the number of days you want to rent: "))

        print(
            f"The total price for the reservation is R${availabe_rooms['price'][room-1] * days}"
        )

        with open("quartos.txt", "w") as file:
            for i in range(len(availabe_rooms["code"])):
                if availabe_rooms["code"][i] == room:
                    availabe_rooms["available"][i] = "False"
                file.write(
                    f"{availabe_rooms['code'][i]}, "
                    f"{availabe_rooms['name'][i]}, "
                    f"{availabe_rooms['price'][i]}, "
                    f"{availabe_rooms['available'][i]}\n"
                )

        with open("reservas.txt", "a") as file:
            file.write(f"{client}, {room}, {days}\n")

        break
    except ValueError:
        print("Invalid input. Try again.")
        time.sleep(1)
        continue
