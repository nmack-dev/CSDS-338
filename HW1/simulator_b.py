# READ ME - IMPORTANT
# Each integer represents a second in time
# The priority rating is based on a scale from 1 -> 10, with 10 being the highest priority

# A class that represents a process in an operating system
class process:
    # priority: the priority of a process
    # ctxs_time: the time it takes for a process to context swtich
    # burst_time: the time required by a process for CPU execution
    # arrival_rate: the time taken by a process to arrive in the ready queue
    # burst_clock: measures the amount of time spent on a process in the CPU
    # total_arrival_time: measures the total time it takes for the a process to enter the ready queue
    # total_ctxs_time: measures the total time from context switches
    # total_time: measures the total time a process takes to execute
    def __init__(self, priority, ctxs_time, burst_time, arrival_rate):
        self.priority = priority
        self.ctxs_time = ctxs_time
        self.burst_time = burst_time
        self.arrival_rate = arrival_rate
        
        self.burst_clock = 0

        self.total_arrival_time = 0
        self.total_ctxs_time = 0
        self.total_time = 0
    
    # A function that calculates the total time a process takes
    def calc_tt(self):
        self.total_time += self.total_arrival_time + self.total_ctxs_time

# A class that represents a process scheduler
class scheduler:
    def __init__(self):
        # ready_queue: contains all of the processes/jobs to be scheduled
        # time_slice: the interval in which the process switchh algorithm occurs
        self.ready_queue = []
        self.time_slice = 1

        # total_ctxs_time: the sum of all context switching times for each process
        # total_arrival_time: the total time it takes for all process to arrive in the ready queue
        # arrival_iterate: a variable to ensure the correct process executes based on its arrival
        # total_time: the total time for all processes to execute
        # current_process: the current process on the CPU
        self.total_ctxs_time = 0
        self.total_arrival_time = 0
        self.arrival_iterate = 0
        self.total_time = 0
        self.current_process = None
    
    # Populates the ready_queue with a list of classes
    def populate_queue(self, processes):
        for process in processes:
            self.ready_queue.append(process)
            self.total_arrival_time += process.arrival_rate
            process.total_arrival_time = self.total_arrival_time
    
    # Schedules the processes and calculates simulated runtimes for each one.
    def schedule_processes(self):
        while self.ready_queue:

            process_switch = False

            # Selects the current process based on the other acceptable processes in the queue
            for process in self.ready_queue:
                if ((self.current_process is None) & (process.total_arrival_time <= self.arrival_iterate)):
                    self.current_process = process
                    process.total_ctxs_time += process.ctxs_time
                
                elif ((self.current_process is None) & (process.total_arrival_time > self.arrival_iterate)):
                    continue

                if ((process.priority > self.current_process.priority) & (process.total_arrival_time <= self.arrival_iterate)):
                    self.current_process.total_ctxs_time += self.current_process.ctxs_time
                    process.total_ctxs_time += process.ctxs_time
                    self.total_ctxs_time += self.current_process.ctxs_time + process.ctxs_time

                    process_switch = True
                    self.current_process = process 
            
            self.arrival_iterate += 1
            
            # Ups the burst count for the current process and ends it if need be
            if (self.current_process is not None):
                self.total_time += self.time_slice
                self.current_process.total_time += self.time_slice
                
                if (not process_switch):
                    self.current_process.burst_clock += self.time_slice

                if (self.current_process.burst_clock >= self.current_process.burst_time):
                    self.current_process.total_ctxs_time += self.current_process.ctxs_time
                    self.ready_queue.remove(self.current_process)
                    self.current_process = None
        
def main():
    # Test processes for the program to run
    p1 = process(8, 2, 3, 4)
    p2 = process(9, 2, 6, 1)
    p3 = process(6, 2, 9, 2)

    job = [p1, p2, p3]

    s1 = scheduler()
    s1.populate_queue(job)
    s1.schedule_processes()

    for i in range(len(job)):
        print("Process " + str(i + 1) + "\n")
        print("Priority: " + str(job[i].priority) + "\n")
        print("Burst Time: " + str(job[i].burst_time) + "\n")
        print("Total Arrival Time: " + str(job[i].total_arrival_time) + "\n")
        print("Total Context Switching Time: " + str(job[i].total_ctxs_time) + "\n")
        
        job[i].calc_tt()
        print("Total Time: " + str(job[i].total_time) + "\n")
        
if __name__ == "__main__":
    main()