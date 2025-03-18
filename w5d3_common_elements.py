# Find Common Elements Between Two Lists (Using Sets)

# approach #1
# def common_elements(list1, list2):
#     common_list = []
#     for ele in list1:
#         if ele in list2:
#             common_list.append(ele)
    
#     return common_list
    

# list1 = ['apple', 'banana', 'cherry']
# list2 = ['apple', 'grape', 'pear']

# result = common_elements(list1, list2)
# print(result)

# approach #2
def common_elements(list1, list2):
    """Find common elements in two lists"""    
    return list(set(list1) & set(list2))
    

list1 = ['apple', 'banana', 'cherry']
list2 = ['apple', 'grape', 'pear']

result = common_elements(list1, list2)
print(result)