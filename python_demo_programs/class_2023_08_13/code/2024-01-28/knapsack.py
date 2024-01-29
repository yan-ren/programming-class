values = [60, 50, 70, 30]
weights = [5, 3, 4, 2]
total_items = 4
def knapsack(values, weights, max_weight, total_items):
    '''
    base case: no items to use or max_weight is 0,
    '''
    if total_items == 0 or max_weight == 0:
        return 0

    '''
    for current item, need to check if have max_weight to use this item
    '''
    current_item_index = total_items - 1
    if weights[current_item_index] > max_weight:
        return knapsack(values, weights, max_weight, total_items - 1)

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

    return max(with_item, without_item)