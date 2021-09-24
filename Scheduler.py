import time 
class Scheduler:
    def __init__(self):
        global ready
        ready = []

    # add processes to the ready queue
    def addProcess(self):
        if self._processState == "Ready":
            ready.append(self)

    # simulate the scheduler
    def runScheduler(self):
        startProcess = time.time()
        pro1 = Process(1, False, 5, 9, "Ready", 0)
        Scheduler.addProcess(pro1)
        pro2 = Process(3, True, 4, 7, "Ready", 1)
        Scheduler.addProcess(pro2)
        pro3 = Process(0, False, 1, 3, "Ready", 2)
        Scheduler.addProcess(pro3)
        pro4 = Process(4, True, 2, 16, "Ready", 3)
        Scheduler.addProcess(pro4)
        pro5 = Process(4, False, 6, 65, "Ready", 4)
        Scheduler.addProcess(pro5)
        pro6 = Process(1, False, 0, 0, "Ready", 5)
        Scheduler.addProcess(pro6)

        # sorthing the ready queue in order of priority level
        sortedReady = []
        for i in ready:
            sortedReady.append(i._priorityLevel)
            sortedReady.sort()

        # algorithm
        for i in range(len(ready)+4):
            for i in ready:
                if i._priorityLevel == sortedReady[0]:
                    currentProcess = i
            clock = currentProcess.setTimeSlice()
            print("PROCESS %i IS RUNNING \n--> TIME SLICE: %i \n--> PRIORITY LEVEL: %s"  % (currentProcess._processNo, currentProcess._quantum, currentProcess._priorityLevel))
            # if there's an I/O operation.
            end = time.time()
            total = (end - startProcess)

            if currentProcess.ioOps == True:
                print("PROCESS %i IS IN BLOCKED QUEUE" % (currentProcess._processNo))
                currentProcess.blockedProcess()
            # if time slice is up
            elif clock - total > 1 and currentProcess._quantum !=0:
                # if process is not finished
                if currentProcess._quantum - clock >= 0:
                    currentProcess._priorityLevel += 1
                    currentProcess._quantum = currentProcess._quantum - clock
                    print("PROCESS %i NOT COMPLETED WITHIN TIMEFRAME. \nNEW PRIORITY: %i" % (currentProcess._processNo, currentProcess._priorityLevel))
                # if process is finished
                else:
                    print("PROCESS %i IS COMPLETE." % currentProcess._processNo)
                    ready.remove(currentProcess)
                    sortedReady.remove(sortedReady[0])
            # if process is finished.
            else:
                print("PROCESS ", currentProcess._processNo, " IS COMPLETE.")
                ready.remove(currentProcess)
                sortedReady.remove(sortedReady[0])
            # No processes = idle state.
            if len(sortedReady) == 0:
                print("NO PROCESSES IN QUEUE. CPU IS IN IDLE STATE.")

scheduler = Scheduler()
scheduler.runScheduler()
