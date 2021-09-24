import time
class Queue:
    def __init__(self, priorityLevel, processState):
        """
            priorityLevel --> Level of priority in the queue.
            processState --> State of the process ie. "Ready" or "Blocked"
        """
        self._priorityLevel = priorityLevel
        self._processState = processState
        self._queue = []

    @property
    def priority(self):
        return self._priorityLevel

    @priority.setter
    def priority(self, priority):
        self._priority = priority

    # Returns length of the queue
    def queueProcesses(self):
        if len(self._queue) == 0:
            return "There are no processes in the queue"
        else:
            for x in self._queue:
                return x
              
    # adding to mlfq
    def addToQueue(self):
        if self._processState == "Ready":
            self._queue.append(self)
            self._queue.sort()

    def __str__(self):
        return "Priority level: %i \nProcess state: %s\n------------------------\n " % (self._priorityLevel, self._processState)

def q():
    q1 = Queue(0, "Ready")
    q2 = Queue(1, "Ready")
    q3 = Queue(2, "Blocked")
    q4 = Queue(3, "Ready")
    q5 = Queue(4, "Blocked")
    q6 = Queue(5, "Ready")
    q7 = Queue(6, "Ready")
    q8 = Queue(7, "Ready")

    global qs
    qs = [q1,q2,q3,q4,q5,q6,q7,q8]
