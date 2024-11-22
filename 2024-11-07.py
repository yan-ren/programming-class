import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('abalone.csv')

# function to calculate the statistics for a given sex
# def calculate_stats(sex):
#     data = df[df['sex'] == sex]
#     count = len(data)
#     length_mean = data['length_mm'].mean()
#     height_mean = data['height_mm'].mean()
#     weight_mean = data['whole_weight_gm'].mean()
#     rings_mean = data['rings'].mean()
#     return count, length_mean, height_mean, weight_mean, rings_mean
#
#
# male_stats = calculate_stats('M')
# female_stats = calculate_stats('F')
# infant_stats = calculate_stats('I')
#
# with open('report.txt', 'w') as file:
#     # header
#     file.write(f"{'sex':3} {'count':5} {'length':6} {'height':6} {'weight':6} {'rings':5}\n")
#
#     # write each line
#     file.write(f"{'M':3} {male_stats[0]:5} {male_stats[1]:6.1f} {male_stats[2]:6.1f} {male_stats[3]:6.1f} {male_stats[4]:5.1f}\n")
#     file.write(f"{'F':3} {female_stats[0]:5} {female_stats[1]:6.1f} {female_stats[2]:6.1f} {female_stats[3]:6.1f} {female_stats[4]:5.1f}\n")
#     file.write(f"{'I':3} {infant_stats[0]:5} {infant_stats[1]:6.1f} {infant_stats[2]:6.1f} {infant_stats[3]:6.1f} {infant_stats[4]:5.1f}\n")

'''
sex count length height weight rings
M    1528  112.3   30.3  198.3  10.7
F    1307  115.8   31.6  209.3  11.1
I    1342   85.5   21.6   86.3   7.9
'''

df = pd.read_csv('abalone.csv')

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle('Relationship between shell size and growth rings')

axes[0, 0].scatter(df['length_mm'], df['rings'], s=2, color='red')
axes[0, 0].set_xlabel('length_mm')
axes[0, 0].set_ylabel('Number of growth rings')

axes[0, 1].scatter(df['diameter_mm'], df['rings'], s=2, color='green')
axes[0, 1].set_xlabel('diameter_mm')
axes[0, 1].set_ylabel('Number of growth rings')

axes[1, 0].scatter(df['height_mm'], df['rings'], s=2, color='blue')
axes[1, 0].set_xlabel('height_mm')
axes[1, 0].set_ylabel('Number of growth rings')

axes[1, 1].scatter(df['shell_weight_gm'], df['rings'], s=2, color='violet')
axes[1, 1].set_xlabel('shell_weight_gm')
axes[1, 1].set_ylabel('Number of growth rings')

plt.show()

