# Merge Two Sorted Lists

def merge_sorted_list(sortedlst1, sortedlst2):
    """Merge two sorted lists without duplicates, keeping the order."""
    i, j = 0, 0
    merged_list = []
    
    while i < len(sortedlst1) and j < len(sortedlst2):
        if sortedlst1[i] < sortedlst2[j]:
            merged_list.append(sortedlst1[i])
            i += 1
        elif sortedlst1[i] > sortedlst2[j]:
            merged_list.append(sortedlst2[j])
            j += 1
        else:
            merged_list.append(sortedlst1[i])
            i += 1
            j += 1
            
    # merged_list.extend(sortedlst1[i:])
    # merged_list.extend(sortedlst2[j:])
        
    return merged_list
    

sample_list1 = [1,3,7]
sample_list2 = [2,3,4]

merged_list = merge_sorted_list(sample_list1,sample_list2)
merged_list.sort()
print(merged_list)