# N = int(input())
#
# scores = []
#
# for _ in range(N):
#     scores.append(int(input()))
#
# unique_score = list(set(scores))
# unique_score.sort(reverse=True)
# bronze_score = unique_score[2]
# number_of_bronze = scores.count(bronze_score)
#
# print(bronze_score, number_of_bronze)

N = int(input())

score_d = {}

for _ in range(N):
    score = int(input())
    # if score in score_d:
    #     score_d[score] += 1
    # else:
    #     score_d[score] = 1
    score_d[score] = score_d.get(score, 0) + 1

scores = list(score_d.keys())
scores.sort(reverse=True)
bronze_score = scores[2]

print(bronze_score, score_d[bronze_score])
