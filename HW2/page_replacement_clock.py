from random import choices
from random import choice

# A class that represents a page with a used bit
class page_struct:
    def __init__(self, page_num):
        self.num = page_num
        self.used = 0

# Determines pages faults based on the clock page replacement algorithm
def page_faults(pages, capacity):

    # Initialization variables to keep track of faults and pages in memory
    page_set = []
    page_faults = 0
    page_ptr = 0

    # Clock page replacement algorithm
    for page in pages:
        page_in_set = False

        if (len(page_set) < capacity):

            if (page not in page_set):
                page_set.append(page)
                page.used = 1
                page_faults += 1
        
        else: 
            pg_values = []

            for pg in page_set:
                pg_values.append(pg.num)

            while not page_in_set: 
                if (page_ptr == capacity):
                    page_ptr = 0

                if (page.num not in pg_values):
                    if (page_set[page_ptr].used == 0):
                        page_set[page_ptr] = page
                        page_set[page_ptr].used = 1
                        page_ptr += 1
                        page_faults += 1
                        page_in_set = True
                    else: 
                        page_set[page_ptr].used = 0
                        page_ptr += 1
                else:
                    page_in_set = True
            
    return page_faults

# Drives the clock page replacement algorithm
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
    
    # A function to generate page_struct instances
    def gen_page_structs(pg_list):
        temp_list = []
        
        for page in pg_list:
            temp_list.append(page_struct(page))
        
        return temp_list
    
    # Modifies page lists to hold page structures
    pages_a = gen_page_structs(pages_a)
    pages_b = gen_page_structs(pages_b)
    pages_c = gen_page_structs(pages_c)

    # The capacity of the frame list to hold pages
    capacity = 5

    # Runs the clock page replacement algorithm and prints the results for different metrics
    print('Page Faults (A): ' + str(page_faults(pages_a, capacity)))
    print('Page Faults (B): ' + str(page_faults(pages_b, capacity)))
    print('Page Faults (C): ' + str(page_faults(pages_c, capacity)))