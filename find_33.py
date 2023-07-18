'''Given a list of ints, return True if the array contains a 3 next to a 3 somewhere'''

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        
    return False

#Test
print(has_33([1,3,4,3]))
