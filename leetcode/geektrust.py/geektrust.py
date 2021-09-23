from classRoom import Room
from rules import checkOverlapDays, isTimeFormat, checkCapacity, checkBuffer, checkIntervalOfFifteen, bookRoom
import sys


if len(sys.argv) != 2:
    raise ValueError('Please provide input file to test the code.')


path = "/home/enemy/Desktop/Projects/pythonDSA/leetcode/geektrust.py/"
fileName = path + sys.argv[1]

# Creating our rooms object
cCave = Room("C-Cave", 3)
dTower = Room("D-Tower", 7)
gMansion = Room("G-Mansion", 20)

# check time format


# reads file line by line
with open(fileName) as file:
    for line in file:
        inputs = list(line.split())
        query_type = inputs[0]
        start_time = inputs[1]
        end_time = inputs[2]

        if isTimeFormat(start_time) == False or isTimeFormat(end_time) == False or checkOverlapDays(start_time, end_time) == False or checkIntervalOfFifteen(start_time, end_time) == False:
            print("INCORRECT_INPUT")

        elif query_type == "VACANCY":
            ans = ""
            if checkBuffer(cCave.timeList, start_time, end_time) == True:
                ans += cCave.name
            if checkBuffer(dTower.timeList, start_time, end_time) == True:
                ans += dTower.name
            if checkBuffer(gMansion, start_time, end_time) == True:
                ans += gMansion.name

            if ans == "":
                print("NO_VACANT_ROOM")
            else:
                print(ans)

        else:
            print("book")
            number_of_people = int(inputs[3])
            if not checkCapacity(number_of_people):
                print("NO_VACANT_ROOM")
                break
            if number_of_people <= cCave.personCapacity and checkBuffer(cCave.timeList, start_time, end_time) == True:
                bookRoom(cCave.timeList, start_time, end_time)
                cCave.personCapacity -= number_of_people
            elif number_of_people <= cCave.personCapacity and checkBuffer(cCave.timeList, start_time, end_time) == False:
                cCave.personCapacity -= number_of_people
            elif number_of_people <= dTower.personCapacity and checkBuffer(dTower.timeList, start_time, end_time) == True:
                bookRoom(dTower.timeList, start_time, end_time)
                dTower.personCapacity -= number_of_people
            elif number_of_people <= dTower.personCapacity and checkBuffer(dTower.timeList, start_time, end_time) == False:
                dTower.personCapacity -= number_of_people
            elif number_of_people <= gMansion.personCapacity and checkBuffer(gMansion.timeList, start_time, end_time) == True:
                bookRoom(gMansion.timeList, start_time, end_time)
                gMansion.personCapacity -= number_of_people
            elif number_of_people <= dTower.personCapacity and checkBuffer(gMansion.timeList, start_time, end_time) == False:
                gMansion.personCapacity -= number_of_people
