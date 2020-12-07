from queue import Queue
from random import choices
from random import choice

# Determines pages faults based on the FIFO page replacement algorithm
def page_faults(pages, capacity):

    # Initialization variables to keep track of faults and pages in memory
    page_set = []
    page_faults = 0
    page_cache = Queue()

    # FIFO page replacement algorithm
    for page in pages:

        if (len(page_set) < capacity):

            if (page not in page_set):
                page_set.append(page)
                page_faults += 1
                page_cache.put(page)
        
        else:

            if (page not in page_set):

                page_value = page_cache.queue[0]
                page_cache.get()
                page_set.remove(page_value)
                
                page_set.append(page)
                page_cache.put(page)
                page_faults += 1
    
    return page_faults

# Drives the FIFO page replacement algorithm
if __name__ == '__main__':
    
    pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Lists that contain all of the pages that need to be loaded into memory
    pages_a = []
    pages_b = []
    pages_c = []

    # The weights for each page type
    pages_b_weights = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]
    pages_c_weights = [4, 16, 64, 128, 128, 128, 128, 64, 16, 4]

    # Generates required biased page requests
    for x in range(1000):
        pages_a.append(choice(pages))
        pages_b.append(choices(pages, weights=pages_b_weights))
        pages_c.append(choices(pages, weights=pages_c_weights))

    # The capacity of the frame list to hold pages
    capacity = 5

    # Runs the FIFO page replacement algorithm and prints the results for different metrics
    print('Page Faults (A): ' + str(page_faults(pages_a, capacity)))
    print('Page Faults (B): ' + str(page_faults(pages_b, capacity)))
    print('Page Faults (C): ' + str(page_faults(pages_c, capacity)))
