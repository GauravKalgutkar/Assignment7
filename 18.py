sample_list1 = [{}, {}, {}]
sample_list2 = [{1, 2}, {}, {}]

def check_empty_dicts(lst):
    return all(not d for d in lst)

print(check_empty_dicts(sample_list1))  # True
print(check_empty_dicts(sample_list2))  # False