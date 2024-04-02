"""Counter Collection"""
from collections import Counter

# The Counter instantly counts elements for any hashable object
# Imagine we have the following data
opening_inventory = [
    'apples', 'oranges', 'bananas', 'grapes', 'pears', 'peaches', 'mangoes', 'watermelons',
    'strawberries', 'blueberries', 'pineapples', 'kiwis', 'apricots', 'plums', 'cherries',
    'lemons', 'limes', 'grapefruits', 'dragonfruits', 'pomegranates'
]

closing_inventory = [
    'apples', 'bananas', 'grapes', 'peaches', 'mangoes', 'strawberries',
    'blueberries', 'pineapples', 'apricots', 'plums', 'lemons', 'limes',
    'pomegranates'
]


def find_amount_sold(opening, closing, item):
    """Find out how many items were sold by using the opening inventory and the closing one"""
    opening_count = Counter(opening)
    closing_count = Counter(closing)

    # Substract the closing counted data from the opening one
    opening_count.subtract(closing_count)

    return opening_count[item]


apples_sold = find_amount_sold(opening_inventory, closing_inventory, 'apples')
print("Apples sold: ", apples_sold)
