sample_dict = {'a': 2, 'b': 3, 'c': 4}

result = 1
for value in sample_dict.values():
    result *= value

print("Multiplication of values:", result)