def solve():
    # Helper function to read input
    read_input = lambda: map(int, input().split())

    # Read the number of attractions (N) and maximum attractions per day (K)
    num_attractions, max_per_day = read_input()

    # Read the scores for each attraction
    attraction_scores = list(read_input())

    # Prepare a list to store the maximum scores for each possible day configuration
    max_scores = [0] * min(2 * num_attractions, num_attractions + max_per_day)

    # Fill max_scores with the maximum scores achievable in one day
    for i, score in enumerate(attraction_scores):
        if i % max_per_day == 0:
            # If it's the start of a new day, use the score of the first attraction
            max_scores[i] = score
        else:
            # Otherwise, use the maximum of the current attraction score or the previous maximum
            max_scores[i] = max(score, max_scores[i - 1])

    # Process to find the maximum total score using multiple days
    # Iterate over the number of days needed, based on max_per_day
    for day_start in range((num_attractions - 1) // max_per_day):
        max_in_window = max_so_far = max_score_for_today = 0

        # Determine the range of attractions to consider for this day
        left_index = day_start * max_per_day
        middle_index = left_index + max_per_day
        right_index = middle_index + max_per_day

        # Loop backward through the attractions in the range for maximum calculations
        while middle_index > left_index:
            middle_index -= 1
            right_index -= 1

            # Get the precomputed max score for this subarray
            max_prev_day = max_scores[middle_index]
            current_attraction_score = attraction_scores[middle_index]

            # Update the maximum values
            if max_in_window < max_prev_day:
                max_in_window = max_prev_day
            if max_so_far < max_prev_day + max_score_for_today:
                max_so_far = max_prev_day + max_score_for_today
            if max_score_for_today < current_attraction_score:
                max_score_for_today = current_attraction_score

            # Update the maximum score for the next day configuration
            max_scores[right_index] = max(max_so_far, max_in_window + max_scores[right_index])

    # Output the maximum possible total score after visiting all attractions
    print(max_scores[num_attractions - 1])


# Call the function to solve the problem
solve()