sample_dict = {'a': 10, 'b': 20, 'c': 30}
key_to_remove = 'b'

if key_to_remove in sample_dict:
    del sample_dict[key_to_remove]

print(sample_dict)