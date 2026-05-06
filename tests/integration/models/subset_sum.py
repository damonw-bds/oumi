def is_subset_sum(arr, n, sum, memo):
    # Base Cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    # Check if the result is already in the memo
    if (n, sum) in memo:
        return memo[(n, sum)]

    # If the last element is greater than the sum, ignore it
    if arr[n-1] > sum:
        memo[(n, sum)] = is_subset_sum(arr, n-1, sum, memo)
        return memo[(n, sum)]

    # Check if the sum can be obtained by including or excluding the last element
    memo[(n, sum)] = is_subset_sum(arr, n-1, sum, memo) or is_subset_sum(arr, n-1, sum-arr[n-1], memo)
    return memo[(n, sum)]

def subset_sum(arr, sum):
    n = len(arr)
    memo = {}
    return is_subset_sum(arr, n, sum, memo)

# Example usage
arr = [3, 34, 4, 12, 5, 2]
sum = 9
if subset_sum(arr, sum):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")