def quickselect(arr, k):
    n = len(arr)
    left, right = 0, n - 1
    arr.append(float('inf'))  # Sentinel value for simplicity
    while left <= right:
        p = arr[left]  # Pivot
        i, j = left + 1, right + 1

        while True:
            while i <= right and arr[i] < p:
                i += 1
            while arr[j] > p:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]

        # Swap pivot into its final position
        arr[left], arr[j] = arr[j], arr[left]
        if j > k - 1:
            right = j - 1
        elif j < k - 1:
            left = j + 1
        else:
            return arr[j]  # Return the k-th smallest element

# Example usage:
arr = [4, 1, 10, 8, 7, 12, 9, 2, 15]
#1,2,4,7,8,9,10,12,15
k = 1
result = quickselect(arr, k)
print(f"The {k}-th smallest element is: {result}")