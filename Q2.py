# function for finding the maximum sum for sub array
def MaxSum(arr):
    max_sum=arr[0]
    for k in arr:
        if k>max_sum:
            max_sum=k
    return max_sum 

# function for sum of all elements of sub array
def SubArray(arr):
    max_sum_array=[]
    sum=0
    for i in range(1,len(arr)):
        for j in range(i-1,i+1):
            sum=sum+arr[j]
            max_sum_array.append(sum)
    return MaxSum(max_sum_array)

print(SubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))