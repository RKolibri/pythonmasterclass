even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
# IN PLACE SORTING
even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort(reverse=True)
print(even)
print(another_even)
sum(even)
print(sum(even))
