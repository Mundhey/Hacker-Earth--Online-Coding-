N = input()

# Get the array
numArray1 = map(int, raw_input().split())
numArray2 = map(int, raw_input().split())

sumArray = []

# Write the logic here:

for i in range(0,N):
    sumArray.append(numArray1[i]+numArray2[i])

# Print the sumArray
for element in sumArray:
    print element,

print ""