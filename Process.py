import time
class Process:
    def __init__(self, execDuration, ioOps, priorityLevel, quantum, processState, processNo):
        """
            execDuration -> length of time of an interrupt.
            ioOps -> presence of an I/O opeartion
            priorityLevel -> the level of priority of a process in the queue
            quantum -> time slice of a process
            processState -> state of the process at any given time
            processNo -> The processes identification number

        """
        self._execDuration = execDuration
        self._ioOps = ioOps
        self._priorityLevel = priorityLevel
        self._quantum = quantum
        self._processState = processState
        self._processNo = processNo
        self._blocked = []

    @property
    def execDuration(self):
        return self._execDuration

    @execDuration.setter
    def execDuration(self, execDuration):
        self._execDuration = execDuration

    @property
    def ioOps(self):
        return self._ioOps

    @ioOps.setter
    def ioOps(self, ioOps):
        self._ioOps = ioOps

    @property
    def priorityLevel(self):
        return self._priorityLevel

    @priorityLevel.setter
    def priorityLevel(self, priorityLevel):
        self._priorityLevel = priorityLevel

    @property
    def quantum(self):
        return self._quantum

    @property
    def processState(self):
        return self._processState

    @processState.setter
    def processState(self, processState):
        self._processState = processState

    @property
    def processNo(self):
        return self._processNo

    def __str__(self):
        return "Process: %i \nProcess state: %s \nPriority level: %i \nTime slice: %i \nI/O present: %s \nI/O duration: %i \n--------------------\n" % (self._processNo, self._processState, self._priorityLevel, self._quantum, self._ioOps, self._execDuration)

    # handling interrupts
    def blockedProcess(self):
        self._processState = "Blocked"
        self._quantum = 0
        self._blocked.append(self)
        print("Process ", self._processNo, " has been blocked for ", self._execDuration)
        time.sleep(self._execDuration)
        self._processState = "Ready"
        self._blocked.remove(self)
        self._ioOps = False
        if self._priorityLevel != 0:
            self._priorityLevel -= 1
        else:
            self._priorityLevel = 0
        print("Process ", self._processNo, " has been switched to Ready state.")
        print("New priority: %i" % self._priorityLevel)
        ready.append(self)

    # setting quantum, based on priority level
    def setTimeSlice(self):
        i = self._priorityLevel
        timeSlice = 2**i
        return timeSlice
