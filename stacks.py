# A stack is a linear abstract data type
# We would be implementing a stack data structure
# To implement a ds,  we need to understand how the data structure works, the kind of operations we
# could perform on it and then create  a class for it limiting the operations to be performed based on the methods we
# include in the class
# Think of a stack ds like a stack of plates. You can only remove items at the top and remove from the top as well
# We can remove from the centre or bottom unless they will all break
# We should also be able to know the number of items in the stacks and also see the next item to be removed.
# We will be implementing our stack using the built in list ds. We will also be using the end of the list as our top
# The reason is that it gives us a constant time of o(1) to add or remove items from the end of a list
# Bottom of stack <<<--------------->>>>> Top of stack


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        ''' This method takes an item and adds to the top of the stack or right side of the list.
        and we have chosen the right side as the top
         Run time of this operation is O(1) or constant time because a
        appending to the end of a list is constant time'''
        self.items.append(item)

    def pop(self):
        ''' To remove item from the top of our stack. 
         Since we are implementing the stack based on a
         list and the list pop method removes item from the end and
        since we specified our end of the list as our top, then we dont need 
        to specify an index for the pop method
        Runtime is also constant time O(1)
        '''
        if self.items:
            return(self.items.pop())
        else:
            return(None)

    def peek(self):
        '''To see the next item in the list that is to be removed
        This method returns the last item in the list which is the top of the stacks.
        This method is done in constant time because indexing into a list is done in const time
        '''
        if self.items:
            return(self.items[-1])
        else:
            return(None)

    def size(self):
        '''To see the no of items in the stack. since we are using a list to build our stack, we can just call the length
        of the list to see the size.
        Runtime is constant time because finding the length of a list happens in constant time
        so this method runs in const time'''
        return(len(self.items))

    def is_empty(self):
        '''To know if the stack is empty'.
        Returns a boolean value to know of stack is empty.Testing for equality happens in const time'''

        return self.items == []
