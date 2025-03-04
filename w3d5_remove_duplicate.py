# Remove Duplicates from a List

# Approach #1
# def remove_duplicate(lst):
#     """Remove duplicates from a list."""
#     clean_lst = []
    
#     try:
#         if not lst:
#             raise ValueError ("Empty list!")

#         for i in range(len(lst)):
#             if lst[i] not in clean_lst:
#                 clean_lst.append(lst[i])
#     except ValueError as e:
#         print(e)
#         exit()
            
#     return clean_lst

# if __name__ == "__main__":
#     sample_list = [1,1,3,3,5,6]
#     clean_list = remove_duplicate(sample_list)
#     print("Cleaned list: ", clean_list)


# Approach #2
def remove_duplicate(lst):
    """Remove duplicates from a list."""    
    if not isinstance(lst, list):
        raise ValueError ("Input must be a list.")
    
    return list(set(lst))

sample_list = [1,1,3,3,5,6]
clean_list = remove_duplicate(sample_list)
print("Clean list: ", clean_list)