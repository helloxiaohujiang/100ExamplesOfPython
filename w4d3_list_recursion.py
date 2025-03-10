# Reverse a List Using Recursion

list_sample = ['a','b','c','d']

# approach#1 slicing
# def reverse_list(lst):
#     """Reverse a list using slicing"""
#     return lst[::-1]

# approach#2 recursion
def reverse_list(lst:list[any])-> list[any]:
    """Reverse a list using recursion"""
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

print(reverse_list(list_sample))