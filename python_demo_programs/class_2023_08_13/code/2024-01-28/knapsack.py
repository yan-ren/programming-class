'''
0-1 knapsack problem

Given a list of items, with value and weight, and give a max weight
'''
# A, B, C, D
values = [60, 50, 70, 30]
weights = [5, 3, 4, 2]
total_items = 4
max_weight = 5

# make a 2D list of size (number of items + 1 ) x (maxWeight+1)
cache = [[0 for x in range(max_weight + 1)] for x in range(len(values) + 1)]
def knapsack(values, weights, max_weight, total_items):
    '''
    base case: no items to use or max_weight is 0,
    '''
    if total_items == 0 or max_weight == 0:
        return 0

    if cache[total_items][max_weight] != 0:
        return cache[total_items][max_weight]
    '''
    for current item, need to check if have max_weight to use this item
    '''
    current_item_index = total_items - 1
    if weights[current_item_index] > max_weight:
        cache[total_items][max_weight] = knapsack(values, weights, max_weight, total_items - 1)
        return cache[total_items][max_weight]

    '''
    1. use the current item
        - gain the value
        - lose the max_weight, determine the subproblem by reducing the max_weight
    2. not use the current item
        - don't gain the value
        - determine the subproblem with the same max_weight
    '''
    with_item = values[current_item_index] + knapsack(values, weights, max_weight - weights[current_item_index], total_items - 1)
    without_item = knapsack(values, weights, max_weight, total_items - 1)

    cache[total_items][max_weight] = max(with_item, without_item)
    return cache[total_items][max_weight]

'''
bottom up
'''
cache = [[0 for x in range(max_weight + 1)] for x in range(len(values) + 1)]
def knapsack_bottom_up(values, weights, max_weight):
    for current_item_index in range(0, len(values) + 1):
        for current_max_weight in range(0, max_weight + 1):

            if current_item_index == 0 or current_max_weight == 0:
                cache[current_item_index][current_max_weight] = 0
            # current item cannot pick
            elif weights[current_item_index] > current_max_weight:
                cache[current_item_index][current_max_weight] = cache[current_item_index - 1][current_max_weight]
            else:
                with_item = values[current_item_index-1] + cache[current_item_index - 1][current_max_weight - weights[current_item_index-1]]
                without_itme = cache[current_item_index - 1][current_max_weight]
                cache[current_item_index][current_max_weight] = max(with_item, without_itme)

    return cache[len(values)][current_max_weight]