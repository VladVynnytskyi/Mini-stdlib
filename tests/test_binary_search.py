from algorithms.searching.binary_search import binary_search
#this function returns the index of the given number using binary search

print(binary_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 22))

print(binary_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 1))

print(binary_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 55))

print(binary_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 2))
print(binary_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 7))
print(binary_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 73))

#--------------------------------------------------------------------------

arr = []
amount = int(input('How many numbers you want append? '))

for i in range(0, amount):
    arr.append(int(input('Your numbers: ')))
arr.sort()

print('Your sort array: \n', arr)

target = int(input("Enter the number you are looking for: "))

if binary_search(arr, target) == -1:
    print('Choose correct number')
else:
    print(binary_search(arr, target) + 1)