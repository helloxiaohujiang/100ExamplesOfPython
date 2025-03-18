# Find the Missing Number in a List

def find_missing_number(nums):
    """Find the missing number in a consecutive list"""
    n = len(nums) + 1
    expected_sum = n*(n+1)/2
    actual_sum = sum(nums)
    return expected_sum - actual_sum   
       
    
sample_list = [1,2,3,4,5,6,8,9]

missing_num = find_missing_number(sample_list)
print(missing_num)