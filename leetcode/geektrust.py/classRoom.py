def addingBuffer(timeList):
    # 09:00 - 09:15, 13:15 - 13:45 and 18:45 - 19:00
    firstBuffer = 36  # 9*4
    timeList[firstBuffer] = False
    secondBufferFirstHalf = 53  # 13*4+1
    timeList[secondBufferFirstHalf] = False
    secondBufferSecondHalf = 54  # 13*4+2
    timeList[secondBufferSecondHalf] = False
    thirdBuffer = 18*4+3  # 18*4+3
    timeList[thirdBuffer] = False
    return timeList


class Room:

    # timeList = 15 mins intervals in 24 hrs => 1 hr = 4's - 15 min intervals equalsto 4*24hrs = 96
    def __init__(self, name, personCapacity, timeList=[True] * 96):
        self.name = name
        self.personCapacity = personCapacity
        self.timeList = addingBuffer(timeList)