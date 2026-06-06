def duplicateZeros(arr: list[int]) -> None:
    """Duplicate each zero in arr, shifting elements right, in place."""
    n = len(arr)

    # First pass: count how many elements survive (find the split point)
    zeros = 0
    i = 0
    while i + zeros < n:
        if arr[i] == 0:
            zeros += 1
        i += 1
    i -= 1  # back to last surviving element

    # Second pass: write from right to left
    j = n - 1
    # Edge case: if the last surviving element is a zero that only gets one copy
    if i + zeros == n and arr[i] == 0:
        arr[j] = 0
        j -= 1
        i -= 1

    while j >= 0:
        arr[j] = arr[i]
        j -= 1
        if arr[i] == 0:
            arr[j] = 0
            j -= 1
        i -= 1
