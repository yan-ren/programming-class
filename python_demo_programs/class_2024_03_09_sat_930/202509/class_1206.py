s = input().strip()

L = s.count('L')
M = s.count('M')
S = s.count('S')

# L: s[0, L]
L_zone = s[0:L]
M_zone = s[L:L+M]
S_zone = s[L+M:]

L_in_M = M_zone.count('L')
L_in_S = S_zone.count('L')

M_in_L = L_zone.count("M")
M_in_S = S_zone.count("M")

S_in_L = L_zone.count("S")
S_in_M = M_zone.count("S")

swaps = 0

direct_LM = min(L_in_M, M_in_L)
swaps += direct_LM
L_in_M -= direct_LM
M_in_L -= direct_LM

direct_LS = min(L_in_S, S_in_L)
swaps += direct_LS
L_in_S -= direct_LS
S_in_L -= direct_LS

direct_MS = min(M_in_S, S_in_M)
swaps += direct_MS
M_in_S -= direct_MS
S_in_M -= direct_MS

# remaining mistake for 3 cycle swap (requires 2 swaps)
remaining = L_in_M + L_in_S + M_in_L + M_in_S + S_in_L + S_in_M
swaps += remaining // 3 * 2
print(swaps)
