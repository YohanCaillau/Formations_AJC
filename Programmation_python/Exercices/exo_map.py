#Question 1
nums = (1, 2, 3, 4, 5, 6, 7) 
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))

#Question 2
nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
nums3 = [7, 8, 9] 
print("\nOriginal list: ")
print(nums1)  
print(nums2)  
print(nums3)  
result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3) 
print("\nNew list after adding above three lists:")
print(list(result))

#Question 3
# List of strings
l = ['sat', 'bat', 'cat', 'mat']
  
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

#Question 4
nums = (1, 2, 3, 4, 5, 6, 7)
for i in range(len(nums)):
    print(i)
    result = map(lambda x: x**nums[i], nums)
    print(list(result))

value=[45,80,3]
indice=[2,3,4]
result=map(lambda x,y:x**y, value, indice)
print("\n",list(result))
