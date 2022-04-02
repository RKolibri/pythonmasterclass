data = [4, 5, 104, 105, 110, 120, 130, 130, 150,  # raw data
        160, 170, 183, 185, 187, 188, 191, 350, 360]
data_empty = []
data_raw = [4, 5, 104, 105, 110, 120, 130, 130, 150,  # raw data
            160, 170, 183, 185, 187, 188, 191, 350, 360]

data_test1 = [104, 105, 110, 120, 130, 130, 150,  # testing if the first two small ones are missing
              160, 170, 183, 185, 187, 188, 191, 350, 360]

data_test2 = [4, 5, 104, 105, 110, 120, 130, 130, 150,  # testing if the last two big ones are missing
              160, 170, 183, 185, 187, 188, 191]

data_test3 = [104, 105, 110, 120, 130, 130, 150,
              # testing if the first two small ones + and last two big ones are missing
              160, 170, 183, 185, 187, 188, 191]
data_test4 = [1004, 1005, 1100, 1200, 1300, 1030, 1500,
              # testing if random bigger values are present gives empty list
              1600, 1070, 1083, 1850, 1087, 1808, 1910]

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
