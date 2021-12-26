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
def checkBuffer(timeList, start_time, end_time, number_of_people):
    startInterval = (int(start_time[:2])*4+1+int(start_time[3:])//15)
    endInterval = (int(end_time[:2])*4+1+int(end_time[3:])//15)
    #print(startInterval, endInterval)
    for timeInterval in range(startInterval, endInterval):

        if timeList[timeInterval][0] == False or timeList[timeInterval][1] < number_of_people:
            return False
    return True


# rule4 && rule5
def bookRoom(timeList, start_time, end_time, number_of_people):
    startInterval = (int(start_time[:2])*4+1+int(start_time[3:])//15)
    endInterval = (int(end_time[:2])*4+1+int(end_time[3:])//15)
    #print(startInterval, endInterval)
    for timeInterval in range(startInterval, endInterval):

        timeList[timeInterval][0] = False
        timeList[timeInterval][1] = number_of_people - \
            timeList[timeInterval][1]
