# '''
# Write a function which takes a list of number as input, return the max and min value in the list
#
# e.g.
# if given [1, 2, 1, 5, 2]
# get 5, 1
# '''
# def find_max_min(numbers):
#     max, min = numbers[0], numbers[0]
#
#     for num in numbers:
#         if num > max:
#             max = num
#         if num < min:
#             min = num
#
#     return max, min
#
#
# print(find_max_min([1, 3, 2, 5, 1]))
# print(find_max_min([1, 112, 1, 20]))
#
# # exercise: write a function which takes a list of number, return the number of positive values
# def count_positive(numbers):
#     count = 0
#     for num in numbers:
#         if num > 0:
#             count += 1
#
#     return count
#
# print(count_positive([1, 2, -1, -3, 0]))
import random

import time

def game_start():
    emojis = ["🍎", "🍌", "🍇", "🍓", "🍉", "🍒", "🍍", "🥝", "🥭", "🍑"]
    game_list = random.sample(emojis, 5)
    return game_list


def main(original):
    print(original)
    time.sleep(3)
    print('\n'*100)


original = game_start()
main(original)