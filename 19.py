sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

unique_list = [list(t) for t in {tuple(lst) for lst in sample_list}]
print(unique_list)