"""Creating personalized dictionaries"""
from collections import UserDict

# Suppose we have the following orders
orders = {
    'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
    'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
    'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
    'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}
}

# We now need a class that inherits the UserDict in order to change the dictionary behavior


class ProcessingDictionaries(UserDict):
    """Personalized dictionary"""

    def clean_order(self):
        """Delete order from orders if it is completed"""
        deleted_orders = []

        for key, val in self.data.items():
            if val['order_status'] == 'complete':
                deleted_orders.append(key)

        for item in deleted_orders:
            del self.data[item]


dictionary_processed = ProcessingDictionaries(orders)
dictionary_processed.clean_order()

# It will show all the elements that are not completed yet
print(dictionary_processed)
