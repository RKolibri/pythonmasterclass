data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

stop = 0

for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging how many were deleted
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # we have the index of the last item to keep
        # set 'start' to the position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1
        break
print(start)  # for debugging
del data[start:]
print(data)

# del data[0:2]
# print(data)
# del data[14:]
# print(data)
# min_valid = 100
# max_valid = 200
# for index, value in enumerate(data):
# if (value < min_valid) or (value > max_valid):  # this won't work
#        del data[index]