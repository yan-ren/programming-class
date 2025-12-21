# d = {'one': 1, 'two': 2, 'three': 3}
#
# for key, value in d.items():
#     print(key, value)

# d = {'class1': [30, 20, 40, 20], 'class2': [32, 40, 20], 'class3': [50, 29]}
#
# # create a new dictionary key->class name, value->average
# avg_dict = {}
#
# for key, value_list in d.items():
#     avg = sum(value_list) / len(value_list)
#     avg_dict[key] = avg
#
# print(avg_dict)
#
# best_class = 'class1'
#
# for key, value in avg_dict.items():
#     if value > avg_dict[best_class]:
#         best_class = key
#
# print(best_class)

# data = {'Tom': {'age': 20, 'home': 'Toronto'},
#         'Cherry': {'age': 21, 'home': 'montreal'},
#         'Bob': {'age': 19, 'home': 'toronto'}
#         }
#
# people = []
#
# for name, info in data.items():
#     if info['home'].lower() == 'toronto':
#         people.append(name)
#
# print(people)
