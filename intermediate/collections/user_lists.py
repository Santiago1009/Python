"""Personalized lists using UserList"""
from collections import UserList
from random import shuffle
# Imagine we have the following data
# It prints numbers from 1 to 50 adding only numbers every 3 spaces
data = [item for item in range(1, 50, 3)]
shuffle(data)


class SortedList(UserList):
    """Sorts automatically a list"""

    def append(self, item):
        self.data.append(item)
        self.data.sort()


sorted_list = SortedList(data)

# The number 3 will be sorted instantly after it is appended
sorted_list.append(3)
print(sorted_list)
