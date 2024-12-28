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
__version__ = "0.1"

import time

rooms_txt = {
    "code": [1, 2, 3, 4],
    "name": ["master suite", "family room", "single room", "simple room"],
    "price": [500, 200, 100, 50],
}
availabe_rooms = {"code": [], "name": [], "price": []}

try:
    with open("quartos.txt", "r") as file:
        for line in file:
            code, name, price = line.strip().split(", ")
            availabe_rooms["code"].append(int(code))
            availabe_rooms["name"].append(name)
            availabe_rooms["price"].append(int(price))
except FileNotFoundError:
    with open("quartos.txt", "w") as file:
        for i in range(len(rooms_txt["code"])):
            file.write(
                f"{rooms_txt['code'][i]}, {rooms_txt['name'][i]}, {rooms_txt['price'][i]}\n"
            )

while True:
    try:
        print("Available rooms:")
        for i in range(len(availabe_rooms["code"])):
            print(
                f"{availabe_rooms['code'][i]} - {availabe_rooms['name'][i]} - R${availabe_rooms['price'][i]}"
            )

        client = input("Enter your name: ")

        if not client or any(
            letter.isdigit() or letter.isnumeric() for letter in client
        ):
            raise ValueError

        room = int(input("Enter the room code you want to rent: "))
        days = int(input("Enter the number of days you want to rent: "))
    except ValueError:
        print("Invalid input. Try again.")
        time.sleep(1)
        continue
