from collections import defaultdict

data = input().split()

N = int(data[0])
M = int(data[1])

pho_restaurants = set()
data = input().split()

for pho in data:
    pho_restaurants.add(pho)

# adjacency list for tree
tree = defaultdict(list)
for _ in range(N-1):
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    tree[a].append(b)
    tree[b].append(a)

# prune the tree to remove non-pho leaves

# find the longest path between two pho restaurant

# min_traversal_time = total_edges * 2 - longest_path