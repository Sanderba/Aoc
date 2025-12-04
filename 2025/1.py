## PUzzle 1
import csv

with open('input.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    position = 50
    count = 0


    for row in csv_reader:
        rotation = row[0]
        direction = rotation[0]
        distance = int(rotation[1:])
        if direction == "L":
            position -= distance
        elif direction == "R":
            position += distance
        position %= 100
        if position == 0:
           count += 1
print(f"Antall ganger: {count}")


## Puzzle 2

import csv

with open('input.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    position = 50
    count = 0


    for row in csv_reader:
        rotation = row[0]
        direction = rotation[0]
        distance = int(rotation[1:])
        for i in range(distance):
            if direction == "L":
                position -= 1
                position %= 100
            elif direction == "R":
                position += 1
                position %= 100
            if position == 0:
                count += 1
print(f"Antall ganger: {count}")
