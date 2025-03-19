# Sort Dictionary by Values

sample_dict = {'apple': 5, 'orange': 3, 'banana': 7, 'cherry': 1, 'nectarine': 2}

# approach#1, can not handle scenario of key with multiple values
# def sort_dict_value(sample_dict):
#     """Sort dictionary by values"""
#     tem_dict = {}
#     sorted_dict = {}

#     for k, v in sample_dict.items():
#         tem_dict[v] = k 
    
#     tem_dict = dict(sorted(tem_dict.items()))

#     for v, k in tem_dict.items():
#         sorted_dict[k] = v
        
#     return sorted_dict

# result = sort_dict_value(sample_dict)
# print(result)


# approach#2
def sort_dict_value(sample_dict):
    """Sort dictionary by values"""
    return dict(sorted(sample_dict.items(), key=lambda x: x[1]))
 
result = sort_dict_value(sample_dict)
print(result)