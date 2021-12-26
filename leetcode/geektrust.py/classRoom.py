class Room:

    # timeList = 15 mins intervals in 24 hrs => 1 hr = 4's - 15 min intervals equalsto 4*24hrs = 96
    def __init__(self, name, personCapacity):
        self.name = name
        self.personCapacity = personCapacity

    def __getitem__(self, timeList):
        return self.timeList
