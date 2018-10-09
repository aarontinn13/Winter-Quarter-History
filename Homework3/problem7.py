def centered_average_with_iteration(nums):
    #sort list first
    nums = sorted(nums)
    if len(nums) > 2:
        #remove last element
        nums.remove(nums[-1])
        #remove first element
        nums.remove(nums[0])
        #create total
        total = 0.0
        #iterate through and add all remaining in the list
        for i in nums:
            total += i
        #take the total and divide by the length of list
        average = ((total) / (len(nums)))
        return float(average)
    else:
        return 'please enter at least three numbers in the list'

print(centered_average_with_iteration([1,2,3,4,5]))



def centered_average(nums):
    #sort list first
    nums = sorted(nums)
    if len(nums) > 2:
        #removing last element
        nums.remove(nums[-1])
        #removing first element
        nums.remove(nums[0])
        #taking sum of numbers and dividing by elements
        average = sum(nums) / len(nums)
        return float(average)
    else:
        return 'please enter at least three numbers in the list'


print(centered_average([3,4,5]))
