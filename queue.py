
# A queue is a linear abstract data type.
#  We are using list to implement our queue ds. We have chosen the left side as our back of the queue
# and the right side as the front of the queue.
# So you can only add items to a queue from the rare and remove from the front

# we chose the right side of our list to serve as the front of our list because removing an item from the end of the list
# is done at constant time
# Inserting an item to our queue(list) is done at linear time because we have to shift all items to the right
# We could decide to use the left side of the list as our front of the queue and the right side of the list as our rare of the queue. Either way. We would still
# have one operation to be O(n) while the other is O(1)
# Think of a print queue when implementing a queue. Items are printed as they come. So as they print, the are removed from the
# queue from the front of the queue
# Queue rear <<<<--------------->>>>> Queue front

class Queue:
    def __init__(self) -> None:
        '''we build our queue on a list'''
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

    def size(self):
        return(len(self.items))

    def peek(self):
        '''To see the next item that can be removed from the queue. So it returns the last item in the list.
        Runtime is constant time O(1)'''
        if self.items:
            return(self.items[-1])
        else:
            return (None)
