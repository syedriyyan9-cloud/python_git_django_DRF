grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_evens = [num for row in grid for num in row if num % 2 == 0]
print(flattened_evens)  # Output: [2, 4, 6, 8]


numbers = [1, 2, 3, 4, 5, 6]
result = [x * 2 if x > 3 else x for x in numbers if x % 2 == 0]
print(result)  # Output: [2, 4, 10, 12]

import timeit
loop = timeit.timeit('''result=[]\nfor i in range(1000): result.append(i**2)''', number=10000)
comp = timeit.timeit('[i**2 for i in range(1000)]', number=10000)
print(f"Loop: {loop:.4f}s, Comp: {comp:.4f}s")  # Comprehension is typically faster