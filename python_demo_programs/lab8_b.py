import math

def optimize_box(mass, mu):
    T = 30
    g = 9.8
    best_theta = None
    max_a = 0

    theta = 0
    while theta <= 90:
        theta_rad = math.radians(theta)
        T_x = T * math.cos(theta_rad)
        T_y = T * math.sin(theta_rad)

        net = T_x - (mu * (mass * g - T_y))
        a = net / mass
        if a > max_a:
            max_a = a
            best_theta = theta
            print(max_a, best_theta)
        theta += 0.01

    if best_theta is None:
        return None

    # Round results to match expected output
    return best_theta, round(max_a, 3)

# Test case
print(optimize_box(3, 0.2))  # Should print: (11.2873, 8.238)
# print(optimize_box(5, 0.4))  # Should print: (11.2873, 8.238)
