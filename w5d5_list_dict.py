# Convert List to Dictionary (Using Zip)

def list_to_dict(list1, list2):
    """Convert list to dictionary"""
    return dict(zip(list1,list2))
    
sample_list1 = ['apple', 'orange', 'banana']
sample_list2 = [3,5,6]

result = list_to_dict(sample_list1,sample_list2)
print(result)