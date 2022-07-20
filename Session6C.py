# Use Bubble Sort to Sort Data
# https://visualgo.net/en/sorting

numbers = [7, 2, 4, 6, 1]
print("[NUMBERS BEFORE]", numbers)

# Pass By Reference
def sort_numbers(data):
    n = len(data)
    for idx1 in range(0, len(data)): # 0, 1, 2, 3, 4
        for idx2 in range(0, n-idx1-1):

            if data[idx2] > data[idx2+1]:
                data[idx2], data[idx2+1] = data[idx2+1], data[idx2]


sort_numbers(numbers)
print("[NUMBERS AFTER]", numbers)