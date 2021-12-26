from classRoom import Room
from rules import checkOverlapDays, isTimeFormat, checkCapacity, checkBuffer, checkIntervalOfFifteen, bookRoom
import sys


if len(sys.argv) != 2:
    raise ValueError('Please provide input file to test the code.')


path = "/home/enemy/Desktop/Projects/pythonDSA/leetcode/geektrust.py/"
fileName = path + sys.argv[1]


def addingBuffer(timeList, capacity):
    # 09:00 - 09:15, 13:15 - 13:45 and 18:45 - 19:00
    timeList = [[True, capacity] for i in range(95)]
    firstBuffer = 36  # 9*4
    timeList[firstBuffer] = [False, -1]
    secondBufferFirstHalf = 53  # 13*4+1-1
    timeList[secondBufferFirstHalf][0] = [False, -1]
    secondBufferSecondHalf = 54  # 13*4+2-1
    timeList[secondBufferSecondHalf][0] = [False, -1]
    thirdBuffer = 19*4-1
    timeList[thirdBuffer][0] = [False, -1]
    return timeList


False

# Creating our rooms object
cCave = Room("C-Cave", 3)
dTower = Room("D-Tower", 7)
gMansion = Room("G-Mansion", 20)
cCave.timeList = addingBuffer([], cCave.personCapacity)
dTower.timeList = addingBuffer([], dTower.personCapacity)
gMansion.timeList = addingBuffer([], gMansion.personCapacity)


# reads file line by line
with open(fileName, 'r') as file:
    lines = file.readlines()

    for line in lines:

        inputs = line.split()

        query_type = inputs[0]
        start_time = inputs[1]
        end_time = inputs[2]

        if isTimeFormat(start_time) == False or isTimeFormat(end_time) == False or checkOverlapDays(start_time, end_time) == False or checkIntervalOfFifteen(start_time, end_time) == False:
            print("INCORRECT_INPUT", line)

        elif query_type == "VACANCY":
            ans = []
            number_of_people = 0
            if checkBuffer(cCave.timeList, start_time, end_time, number_of_people) == True:
                ans.append(cCave.name)
            if checkBuffer(dTower.timeList, start_time, end_time, number_of_people) == True:

                ans.append(dTower.name)
            if checkBuffer(gMansion.timeList, start_time, end_time, number_of_people) == True:
                ans.append(gMansion.name)

            if ans == []:

                print("NO_VACANT_ROOM", line)
            else:
                print(" ".join(ans), line)

        else:
            number_of_people = int(inputs[3])
            if not checkCapacity(number_of_people):
                print("NO_VACANT_ROOM", line)
                break

            if checkBuffer(cCave.timeList, start_time, end_time, number_of_people) == True:
                bookRoom(cCave.timeList, start_time,
                         end_time, number_of_people)
                print(cCave.name, line)

            elif checkBuffer(dTower.timeList, start_time, end_time, number_of_people) == True:
                bookRoom(dTower.timeList, start_time,
                         end_time, number_of_people)
                print(dTower.name, line)

            elif checkBuffer(gMansion.timeList, start_time, end_time, number_of_people) == True:
                bookRoom(gMansion.timeList, start_time,
                         end_time, number_of_people)
                print(gMansion.name, line)

            else:
                print("NO_VACANT_ROOM", line)
