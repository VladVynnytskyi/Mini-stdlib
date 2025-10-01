from algorithms.searching.jump_search import jump_search
#this function returns the index of the given number using jump search

print(jump_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 22))

print(jump_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 1))

print(jump_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 55))

print(jump_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 2))
print(jump_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 7))
print(jump_search([1,2,3,4,5,6,7,8,9,11,22,33,44,55], 73))

#--------------------------------------------------------------------------

arr = []
amount = int(input('How many numbers you want append? '))

for i in range(0, amount):
    arr.append(int(input('Your numbers: ')))
arr.sort()

print('Your sort array: \n', arr)

target = int(input("Enter the number you are looking for: "))

index = jump_search(arr, target)
if index == -1:
    print('Choose correct number')
else:
    print(index + 1)