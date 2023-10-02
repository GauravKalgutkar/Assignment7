dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

common_keys = set(dict1.keys()) & set(dict2.keys())

for key in common_keys:
    print(f"{key}: {dict1[key]} is present in both x and y")