# Premise: given an array with 1,000,000 integers between 1 and 1,000,000, one integer is in the array twice.
#           Find the duplicate.
#
# Input:   nums, an integer array with 1,000,000 ints where each item is in range 1 and 1,000,000 inclusively
# Return:  int of a duplicate value
#          -1 if there is no duplicate int found
#          -2 if the input violated our constraint
#
# Analysis: Assume that the input Array has a fixed length of 1,000,000 as suggested in the premise. 
#       let A=[a_1, a_2...a_999,999], we'll loop over A once to cache each a_i to detect potential duplicate.
#       I used a *Set data structure as a caching mechanism. We could potentially cache upto a_999,999 which 
#       yield space complexity to be O(c). Similarly, the runtime complexity is O(c) because the input size is fixed.
#
#       *Footnote* If there is a constraint on memory or we just need to optimize for space, we could allocate
#           an array of bit, B=[b_0, b_1,..., b_999,999] where each b_i maps to an element between 1 and 1,000,000.
#           Therefore, one byte could represent 8 a_i's. Space complexity would still be O(c) but we can save 
#           by a constant factor of k with a lower bound of 8. Before: c * 1,000,000 -> Now: c/k * 1,000,000.

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
# Analysis: let C=[c_1, c_2...c_n], we'll loop over C once in order to cache all occurances of c_i. I used a map data structure 
#       as a caching mechanism. We need to cache upto c_n which yield the space complexity to be O(N). 
#       Similarly, the runtime complexity is O(N) because we need to loop for each c_i in C.

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
