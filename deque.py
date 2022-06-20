# A little note on deque(pronounced deck). A deque is a linear abstract data structure that can be implemented in python using
# python built in data type called list.
# You can add items to the front of a deque or rare of the deck. You can also remove items from both ends.
# You can perform other operations like peek to see the item be removed from either end or checking if the deque is empty
# or checking for the lenght of the deck.
# These are basic methods that can be implemented in a deck
# We can use either the left end or right end of our list to serve as the front or back of our deque.
# We have chosen to use the right as the front of the deque. Just trying to be consistent with the other data structure files
#  A deque is a limiting ds because we can only access(remove) data from the rare or front
# Deque rear <<<<--------------->>>>> Deque front

class Deque:
    def __init__(self) -> None:
        '''we build our deque on a list'''
        self.items = []

    def add_front(self, item):
        ''' This adds the item to the right side of the list which serves as our deque front.
        Runtime here is constant time O(1) because its just adding to the end of a list'''
        self.items.append(item)

    def add_rear(self, item):
        '''This adds an item to the left end of the list which serves as our deque rear
        Runtime here is O(n) because inserting an element to the left end of a list would move each item in the list
        one step to the right. Number of operations to be performed depends on the number of items in the list  '''
        self.items.insert(0, item)

    def remove_front(self):
        '''This removes the last item of the list which is the right side and this side serves as our deque front
        Runtime for this operation is O(1) because we are just removing from the end'''
        if self.items:
            return (self.items.pop())
        else:
            return(None)

    def remove_rear(self):
        '''Removes items from the left end of the list which is our deque's rear
        Runtime is linear time O(n) because items would have to move one step to the left to fill in the gap'''
        if self.items:
            return (self.items.pop(0))
        else:
            return (None)

    def peek_front(self):
        '''Runtime here is constant time. We return the item at the right end of the list which serves as our front'''
        if self.items:
            return(self.items[-1])
        else:
            return(None)

    def peek_rear(self):
        '''Runtime here is constant time. We return the item at the left end of the list which serves as our rear'''
        if self.items:
            return(self.items[0])
        else:
            return(None)

    def is_empty(self):
        '''Checks to see if the queue is empty

        Runtime of this is constant time'''
        return self.items == []

    def size(self):
        '''This returns the length of the deque'''
        return(len(self.items))
