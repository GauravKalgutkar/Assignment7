sample_dict = {'a': 50, 'b': 30, 'c': 80, 'd': 20}

sorted_dict = dict(sorted(sample_dict.items(), key=lambda x: x[1], reverse=True))
highest_values = dict(list(sorted_dict.items())[:3])
print(highest_values)