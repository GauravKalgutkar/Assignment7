sample_dict = {1: 10, 3: 30, 2: 20}

sorted_dict_asc = dict(sorted(sample_dict.items(), key=lambda x: x[1]))

sorted_dict_desc = dict(sorted(sample_dict.items(), key=lambda x: x[1], reverse=True))

print("Ascending order:", sorted_dict_asc)
print("Descending order:", sorted_dict_desc)