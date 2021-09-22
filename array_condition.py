def arr_condition(arr, n, p):

    max_value = float('-inf')

    for i, x in enumerate(arr):
        if x == p:
            return i
            break
        elif x < p:
            max_value = max(max_value, x)

    i = arr.index(max_value)
    return i+1


n = int(input("Enter the length of array: "))
arr = list(map(int, input("Enter the numbers : ").strip().split()))[:n]
p = int(input("Enter the number to search: "))
print(arr_condition(arr, n, p))
