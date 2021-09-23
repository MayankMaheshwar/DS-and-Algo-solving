import time


# rule2
def checkIntervalOfFifteen(startTime, endTime):
    if (int(startTime[3:]) % 15 != 0 or int(endTime[3:]) % 15 != 0):
        return False
    else:
        return True


# rule7
def checkCapacity(people):
    if people < 2 or people > 20:
        return False
    else:
        return True


# rule8
def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False


# rule1
def checkOverlapDays(time1, time2):
    if int(time1[:2]) > int(time2[:2]):
        return False
    else:
        return True


# rule6
def checkBuffer(timeList, start_time, end_time):
    startInterval = (int(start_time[:2])//4+int(start_time[3:])//4)-1
    endInterval = (int(end_time[:2])//4+int(end_time[3:])//4)-1
    for timeInterval in range(startInterval, endInterval+1):
        if timeList(timeInterval) == False:
            return False
    return True


# rule4 && rule5
def bookRoom(timeList, start_time, end_time):
    startInterval = (int(start_time[:2])//4+int(start_time[3:]//4))-1
    endInterval = (int(end_time[:2])//4+int(end_time[3:]//4))-1
    for timeInterval in range(startInterval, endInterval+1):
        timeList[timeInterval] = False
