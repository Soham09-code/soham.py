# 1. Find largest element in array
def largest_element(arr):
    return max(arr)

# 2. Find second largest element in array
def second_largest(arr):
    unique = list(set(arr))
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]

# 3. Move all zeros to end
def move_zeros(arr):
    non_zeros = [x for x in arr if x != 0]
    zeros = [0] * (len(arr) - len(non_zeros))
    return non_zeros + zeros

# 4. Rotate array by one (right)
def rotate_by_one(arr):
    if not arr:
        return arr
    return [arr[-1]] + arr[:-1]

# 5. Check if array is sorted (ascending)
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# 6. Reverse a string
def reverse_string(s):
    return s[::-1]

# 7. Check if string is palindrome
def is_palindrome(s):
    return s == s[::-1]

# 8. Count frequency of array elements
def frequency(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

