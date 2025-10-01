from algorithms.searching.linear_search import linear_search
#this function returns the index of the given number using linear search

print(linear_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 22))

print(linear_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 1))

print(linear_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 55))

print(linear_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 2))
print(linear_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 7))
print(linear_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 73))

#--------------------------------------------------------------------------

arr = []
amount = int(input('How many numbers you want append? '))

for i in range(0, amount):
    arr.append(int(input('Your numbers: ')))

print('Your sort array: \n', arr)

target = int(input("Enter the number you are looking for: "))

if linear_search(arr, target) == -1:
    print('Choose correct number')
else:
    print(linear_search(arr, target) + 1)