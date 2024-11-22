def can_cover_all_houses(H, houses, hose_length, k, start_index):
    """
    Check if all houses can be covered with k hydrants for a given hose length.

    Parameters:
    - H: Total number of houses.
    - houses: Sorted list of house positions, duplicated to simulate circular arrangement.
    - hose_length: Current hose length being tested.
    - k: Number of available hydrants.
    - start_index: Starting index in the houses list to begin placing hydrants.

    Returns:
    - True if all houses can be covered with k hydrants, False otherwise.
    """
    hose_length *= 2  # The hose covers distance in both directions from the hydrant.
    placed = 1  # Start with one hydrant placed.
    start = houses[start_index]
    hose_range = start + hose_length  # Maximum range the first hydrant can cover.

    for h in houses[start_index:start_index + H]:
        if h > hose_range:
            # Need to place another hydrant as the current one can't cover this house.
            hose_range = h + hose_length
            placed += 1
            if placed > k:
                # More hydrants are needed than available.
                return False
    return True


def binary_search_for_hose_length(H, houses, K, start):
    """
    Finds the minimum hose length needed to cover all houses starting from a specific house.

    Parameters:
    - H: Total number of houses.
    - houses: Sorted list of house positions, duplicated to simulate circular arrangement.
    - K: Number of available hydrants.
    - start: Starting index in the houses list to begin placing hydrants.

    Returns:
    - The minimum hose length required to cover all houses with K hydrants.
    """
    best = C // 2
    left, right = 0, C // 2
    while left <= right:
        mid = (left + right) // 2
        if can_cover_all_houses(H, houses, mid, K, start):
            right = mid - 1
            best = min(best, mid)
        else:
            left = mid + 1
    return best


C = 1000000  # Circumference of the village.
H = int(input())  # Number of houses.
houses = [int(input()) for _ in range(H)]
houses.sort()
houses += [a + C for a in houses]  # Duplicate houses list with offset to handle circular village.
K = int(input())  # Number of hydrants available.

# Find the minimum hose length required, considering each house as a starting point.
final_hose_length = min(binary_search_for_hose_length(H, houses, K, i) for i in range(H))

print(final_hose_length)