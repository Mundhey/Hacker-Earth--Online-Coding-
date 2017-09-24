N = input()

# Get the input
numArray = map(int, raw_input().split())

sum_integer = 0
# Write the logic to add these numbers here

for i in range(0,N):
    sum_integer=sum_integer+numArray[i]


# Print the sum
print sum_integer