isConnected = [[]] # assume there is value inside

number_of_cities = len(isConnected)
provinces = 0
visited = set()

def dfs(city):
    visited.add(city)
    for neighbor, is_connected in enumerate(isConnected):
        if is_connected == 1 and neighbor not in visited:
            dfs(neighbor)


for city in range(number_of_cities):
    if city not in visited:
        dfs(city)
        provinces += 1
        