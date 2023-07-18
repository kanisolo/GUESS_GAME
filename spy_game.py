"""Write a function that takes in a list of integers and returns True if it contains 007 in order"""

def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num in nums:
            if num == code[0]:
                code.pop(0)
    return len(code) == 1

#Test
print(spy_game([1,2,7,4,0,0,5]))