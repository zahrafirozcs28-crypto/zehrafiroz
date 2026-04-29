def min_swaps_to_make_identical(s1, s2):
    xy = 0
    yx = 0
    
    for c1, c2 in zip(s1, s2):
        if c1 == '1' and c2 == '0':
            xy += 1
        elif c1 == '0' and c2 == '1':
            yx += 1
            
    if (xy + yx) % 2 != 0:
        return -1
    
    return xy // 2 + yx // 2 + (xy % 2) * 2

s1_1, s2_1 = "1100", "1111"
print(min_swaps_to_make_identical(s1_1, s2_1))

s1_2, s2_2 = "00011", "11001"
print(min_swaps_to_make_identical(s1_2, s2_2))
