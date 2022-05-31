# PROBLEM STATEMENT
#  We want to define a function that checks if a string is a palindrome using the Deque data structure implemented in the
# deque.py file

# Return true if its a palindrome and returns false if it isnt

# SOLUTION
# We would put our data in a deque and limit the methods we can use on our data to the methods available for a deque.
# Thats the essence of solving this problem  using a deque ds

from deque import Deque


def palindrome_checker(string):

    my_data = Deque()

    for character in string:
        # Adds each character in the string to my Deque instance  using the add_front method becasue this method is a constant time opoeration
        my_data.add_front(character)

    while my_data.size() >= 2:  # check to see if we have less than two charactes left in the deque
        # assigns the front element in the deque to the front variable and reduces the deque length each time
        front = my_data.remove_front()
        # assigns the rear  element in the deque to the rear variable and reduces the deque length each time
        rear = my_data.remove_rear()
        if front != rear:  # compare front and rear items for a match
            return (False)
    return (True)


print(palindrome_checker('racecar'))
print(palindrome_checker('oranges'))
