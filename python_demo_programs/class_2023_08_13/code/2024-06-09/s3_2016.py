from collections import defaultdict, deque

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
def prune_tree(tree, pho_restaurants):
    visited = [False] * N
    leaves = deque()
    for node in range(N):
        if len(tree[node]) == 1 and node not in pho_restaurants:
            leaves.append(node)

    while leaves:
        leaf = leaves.popleft()
        visited[leaf] = True
        for neighobor in tree[leaf]:
            if not visited[neighobor]:
                # remove useless leaf from the tree
                tree[neighobor].remove(leaf)
                # if the parent of the leaf is still useless, remove it as well
                if len(tree[neighobor]) == 1 and neighobor not in pho_restaurants:
                    leaves.append(neighobor)

def dfs(start):
    farthest_node = start
    max_depth = 0
    visited = set()
    stack = [(start, 0)] # in stack each tuple has two values, first value is node, second value is depth

    while stack:
        node, depth = stack.pop()
        visited.add(node)

        if depth > max_depth:
            max_depth = depth
            farthest_node = node

        for neighbor in tree[node]:
            if neighbor not in visited:
                stack.append((neighbor, depth+1))

    return farthest_node, max_depth


# find the longest path between two pho restaurant
# choose any pho restaurant as the starting point
start = pho_restaurants[0]

# find the farthest pho restaurant from the chosen starting point
farthest_pho, _ = dfs(start)

# farthest_pho is one side on the longest path
# find the longest path from the farthest pho restaurant
_, longest_path = dfs(farthest_pho)

total_edges = sum(len(neighbors) for neighbors in tree.values()) // 2

min_traversal_time = total_edges * 2 - longest_path