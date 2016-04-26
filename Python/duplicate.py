# Premise: given an array with 1,000,000 integers between 1 and 1,000,000, one integer is in the array twice.
#           Find the duplicate.
#
# Input:   nums, an integer array with 1,000,000 ints where each item is in range 1 and 1,000,000 inclusively
# Return:  int of a duplicate value
#          -1 if there is no duplicate int found
#          -2 if the input violated our constraint
#
# Runtime Complexity: O(N)
# Space Complexity: O(N)

def findDuplicate(nums):
    if nums == None or len(nums) != 1000000:
        return -2

    cache = set()
    for num in nums:
        if not isinstance(num, int) or num < 1 or num > 1000000:
            return -2

        if num not in cache:
            cache.add(num)
        else:
            return num

    return -1

# negative unit tests
assert(findDuplicate(None) == -2)
assert(findDuplicate([]) == -2)
assert(findDuplicate(["str", 12]) == -2)

# positive unit tests
nums = []
for i in range(1, 1000001):
    nums.append(i)

assert(findDuplicate(nums) == -1)

nums[921222] = 18
assert(findDuplicate(nums) == 18)

nums[1] = 1
assert(findDuplicate(nums) == 1)



# Premise: Find the first non-repeating character in a string: ("DEFD" -> E)
#
# Input:   chars, a string to be examined
# Return:  char of the first none-repeating character in the input string
#          -1 if no none-repeating character found
#          -2 if the input violated our constraint
#
# Runtime Complexity: O(N)
# Space Complexity: O(N)
def findFirstNonRepeatingCharacter(chars):
    if chars == None or not isinstance(chars, str):
        return -2

    cache = {}
    for char in chars:
        if char not in cache:
            cache[char] = 1
        else:
            cache[char] += 1

    for char in chars:
        if cache[char] == 1:
            return char

    return -1

# negative unit tests
assert(findFirstNonRepeatingCharacter(None) == -2)
assert(findFirstNonRepeatingCharacter(12) == -2)
assert(findFirstNonRepeatingCharacter([1, 2, 3, 4, 5]) == -2)

# positive unit tests
assert(findFirstNonRepeatingCharacter("") == -1)
assert(findFirstNonRepeatingCharacter("AA") == -1)
assert(findFirstNonRepeatingCharacter("AABBCC") == -1)
assert(findFirstNonRepeatingCharacter("AABBC") == "C")
assert(findFirstNonRepeatingCharacter("ABC") == "A")
assert(findFirstNonRepeatingCharacter("DEFD") == "E")