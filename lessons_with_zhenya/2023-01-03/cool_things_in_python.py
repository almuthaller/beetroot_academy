var_1, var_2 = 1, 2

assert var_1 == 1
assert var_2 == 2

var_1, var_2 = var_2, var_1

assert var_1 == 2
assert var_2 == 1
