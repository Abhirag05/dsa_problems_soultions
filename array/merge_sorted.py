def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid=(len(nums)//2)
    left=nums[:mid]
    right=nums[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)


def merge(nums1,nums2):
    res=[]
    i=0
    j=0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            res.append(nums1[i])
            i+=1
        else:
            res.append(nums2[j])
            j+=1
    res.extend(nums1[i:])
    res.extend(nums2[j:])
    return res

print(merge_sort([1,2,3,4,5,1,6,7,8,9,10,0]))


#approach:we used merge sort algorithm to sort the array. we divided the array into two halves and then we merged them in sorted order.

#time complexity: O(nlogn) where n is the number of elements in the array. we are dividing the array into two halves and then merging them in sorted order.

#space complexity: O(n) where n is the number of elements in the array. we are using extra space to store the merged array.