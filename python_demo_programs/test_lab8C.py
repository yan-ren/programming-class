from lab8C import sumabs, revcomp

# Tests for sumabs
assert sumabs([1, -2, 3]) == 6
assert sumabs([-1, -2, -3]) == 6
assert sumabs([0, -5.5, 4.5]) == 10.0
assert sumabs([100]) == 100

# Tests for revcomp
assert revcomp("ac") == "gt"
assert revcomp("ttac") == "gtaa"
assert revcomp("acgt") == "acgt"
assert revcomp("cccgttacggatcc") == "ggatccgtaacggg"
assert revcomp("aCgT") == "acgt"
