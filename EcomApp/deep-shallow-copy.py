import copy

original = [1, 2, [3, 4]]
shallowCopy = copy.copy(original)
deepCopy = copy.deepcopy(original)

print('Results when only first element of original is modified')
original[0] = 10  # Modifiy only the first element of list2
#Results
print(original)  # Output: [10, 2, [3, 4]]
print(shallowCopy)  # Output: [1, 2, [3, 4]]
print(deepCopy)  # Output: [1, 2, [3, 4]]


print('Results when  nested list element of original is modified')
original[2][0] = 100  # Modifiy the nested list only in list2
#Results
print(original)  # Output: [10, 2, [100, 4]]
print(shallowCopy)  # Output: [1, 2, [100, 4]]
print(deepCopy)  # Output: [1, 2, [3, 4]]
