"""Al collection methods combined"""
# In this program we'll we checking overstocked items into groups to sell at once.
# We'll split items by price and then pick cheaper items and two more expensive items per bundle
# Then we are going to promote the bundles which have a value greater than 100 dollars
from collections import namedtuple, deque

overstock_items = [
    ['shirt_103985', 15.99],
    ['pants_906841', 19.99],
    ['pants_765321', 15.99],
    ['shoes_948059', 29.99],
    ['shoes_356864', 9.99],
    ['shirt_865327', 10.99],
    ['shorts_086853', 9.99],
    ['pants_267953', 21.99],
    ['dress_976264', 32.99],
    ['shoes_135786', 17.99],
    ['skirt_196543', 12.99],
    ['jacket_976535', 26.99],
    ['pants_086367', 30.99],
    ['dress_357896', 29.99],
    ['shoes_157895', 14.99]
]
# Send the expensive items to the front of the deque
split_prices = deque()
for item in overstock_items:
    if item[1] > 20:
        split_prices.appendleft(item)
    else:
        split_prices.append(item)

# We create a new namedtuple
ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

# We will look in the list if there are 5 elements left or more in the deque
# We wil then create the ClothesBundle with elements from the most expensive ones and the cheapest
# Then we wil sum them in order to see if the sum is bigger than 100, if it is,
# then we add it to the bundles.

bundles = []
while len(split_prices) >= 5:
    bundle_list = [
        split_prices.pop(), split_prices.pop(), split_prices.pop(),  # Cheapest
        split_prices.popleft(), split_prices.popleft()  # Most expensive
    ]

    calc_price = sum(b[1] for b in bundle_list)  # Claculate the price
    bundles.append(ClothesBundle(bundle_list, calc_price))  # Append the bundle


# Here we'll save the bundles that have a price bigger than 100 dolars
promoted_bundles = []
for bundle in bundles:
    if bundle.bundle_price > 100:
        promoted_bundles.append(bundle)


for bundle in promoted_bundles:  # Print the results
    print(bundle)
