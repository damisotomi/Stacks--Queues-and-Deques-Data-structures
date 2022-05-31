# PROBLEM STATEMENT
# TO CREAtE 3 CLASSES  THAT TOGETHER MODEL HOW A PRINTER COULD TAKE PRINT JOBS OUT OF A PRINT QUEUE

# Basicallly the way this works is that a job is first added to a print queue then the printer removes the job
# from the print queue to work on
# Step 1: create an instance of all three classes
# step 2 : add the job class instance to the PrintQueue using the enqueue method
# step3: call the get_job method in the printer class and pass the instance of the PrintQueue class as an argument to the function.
# This printQueue class instance would already have an item in it which we did in step 2
# step 4: call the print_job in the printer class and pass it the self.current_job attribute which is actually a job instance

class PrintQueue:
    '''Follows the queue data structure implemented in the queue.py file'''

    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item):
        '''Adds to the queue from the rare which is the left side of our list.
        This method is linear time O(n) because inserting into the zeroth index moves other elements one step to the right'''
        return (self.items.insert(0, item))

    def dequeue(self):
        '''Removes the last item of the list which is repr as the front of the queue
        This operation is done at constant time'''
        if self.items:
            return(self.items.pop())
        else:
            return (None)

    def is_empty(self):
        return (self.items == [])


class Job:
    '''Has pages attributes and each job can have 1-10 pages to be asigned randomly'''
    import random

    def __init__(self, page=random.randrange(1, 11)) -> None:
        self.page = page

    def print_page(self):
        '''Decrements pages'''
        if self.page >= 0:
            self.page -= 1

    def check_complete(self):
        '''Checks if all pages have been printed'''
        if self.page == 0:
            return('True')
        else:
            return('False')


class Printer:
    '''Makes use of the queues built in dequeue method to take the first job in the print queue off the queue'''

    def __init__(self) -> None:
        self.current_job = None

    def get_job(self, print_queue):
        ''' when calling this funtion you need to pass an instance of the PrintQueue class so it removes the item in the queue to work on for printing'''
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:  # Queue is empty
            return('No more jobs to print')

    def print_job(self, job):
        ''' when calling this funtion you need to pass the self.current_job above so the printer works on that job'''
        while job.page > 0:
            job.print_page()

        if job.check_complete():
            return('Printing complete')


# Try this codes in this order to run
job = Job()
print_q = PrintQueue()
printer = Printer()
print_q.enqueue(job)
print_q.items
printer.get_job(print_q)
print_q.items
printer.print_job(printer.current_job)
