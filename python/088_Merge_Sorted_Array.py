class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        # 直观思路显然是双指针i, j同时扫描A, B，选min(A[i], B[j])作为下一个元素插入。
        #但是只能利用A后面的空间来插入，这样就很不方便了。
        #反向思路，merge后的数组一共有m+n个数。
        #i, j从A, B尾部扫描，选max(A[i], B[j])插入从m+n起的尾部。
        #这样也可以防止插入到A原来数字的范围内时，overwrite掉A原来的数。

        
        
        p1, p2 = m - 1, n - 1
        pos = m + n - 1
        while p1 >= 0 and p2 >= 0:  # condition is 'and': both nums still have elements. 
            if nums1[p1] >= nums2[p2]:
                nums1[pos] = nums1[p1]
                p1 -= 1
            else:
                nums1[pos] = nums2[p2]
                p2 -= 1
            pos -= 1
            
        if p2 >= 0:
            nums1[: p2 + 1] = nums2[: p2 + 1]  # be careful with slicing here a[:n] = a[0 : n-1]


    # def merge(self, nums1, m, nums2, n):
    #     # using slicing
    #     i, j, k = m - 1, n - 1, m + n - 1
    #     while i >= 0 and j >= 0:
    #         if nums1[i] > nums2[j]:
    #             nums1[k] = nums1[i]
    #             i -= 1
    #         else:
    #             nums1[k] = nums2[j]
    #             j -= 1
    #         k -= 1
    #
    #     if j >= 0:
    #         nums1[:k + 1] = nums2[:j + 1]
