from time import sleep
from random import randint
import threading

# A class that represents a process in an operating system
class process:
    # priority: the priority of a process
    # ctxs_time: the time it takes for a process to context swtich
    # burst_time: the time required by a process for CPU execution
    def __init__(self, priority, ctxs_time, burst_time):
        self.priority = priority
        self.ctxs_time = ctxs_time
        self.burst_time = burst_time
        self.burst_completion = 0
    
    def sleep_ctxs(self):
        sleep(self.ctxs_time)

    def sleep_burst(self):
        sleep(self.burst_time)

# A class that represents a set of process with different priorities and an average arrival rate
class priority:
    def __init__(self, processes, avg_arrival_rate):
        self.processes = processes
        self.avg_arrival_rate = avg_arrival_rate
        self.total_ctxs_time = 0
        self.total_burst_time = 0

        for process in self.processes:
            self.total_ctxs_time += process.ctxs_time
            self.total_burst_time += process.ctxs_time
    
    def process_ariv(self):
        sleep(self.avg_arrival_rate)
        return self.processes
    
def main():
    # Declared example process objects
    proc1 = process(10, 4, 2)
    proc2 = process(8, 4, 2)
    proc3 = process(6, 4, 2)
    proc4 = process(10, 4, 2)
    proc5 = process(8, 4, 2)
    proc6 = process(7, 4, 2)

    # Jobs that contain the process objects
    job1 = [proc1, proc2, proc3]
    job2 = [proc4, proc5, proc6]
    
    # Declares priority objects from jobs and sets the average wait time
    # The ready queue is where process go when at the ready state
    p1 = priority(job1, 3)
    p2 = priority(job2, 8)
    ready_queue = []

    # Populates the ready queue with processes from a priority object
    def populate_queue(priority):
        processes = priority.process_ariv()
        for process in processes:
            ready_queue.append(process)
    
    # Schedules a process to use the CPU
    def scheduler():
        sleep(min(p1.avg_arrival_rate, p2.avg_arrival_rate))

        previous_process = None
        current_process = None
        
        while ready_queue:
            for process in ready_queue:
               
               if (current_process is None):
                   current_process = process
               
               if (process.priority > current_process.priority):
                    previous_process = current_process
                    current_process = process
            
            if (previous_process is None):
                sleep(current_process.ctxs_time)
            else:
                sleep(max(current_process.ctxs_time, previous_process.ctxs_time))
            
            sleep(1)
            current_process.burst_completion += 1

            if (current_process.burst_completion >= current_process.burst_time):
                print(current_process.priority)
                ready_queue.remove(current_process)
                current_process = None

    # TODO: Fix faulty threading issues to get the program to operate correctly       
    t1 = threading.Thread(target=populate_queue(p1))
    t2 = threading.Thread(target=populate_queue(p2))
    t3 = threading.Thread(target=scheduler())

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()

        


            

            
