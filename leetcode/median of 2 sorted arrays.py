'''
Find the median of 2 sorted arrays of different length
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        first = nums1[:]
        second = nums2[:]

        while m > 2 and n > 2:
            med1 = find_median(first)
            med2 = find_median(second)
            if med1 == med2:
                return med1
            if med1 > med2:
                first = first[:(m + m% 2) / 2]
                second = second[(n - n % 2) / 2:]
            else:
                first = first[(m - m % 2) / 2:]
                second = second[:(n + n % 2) / 2]
            m = len(first)
            n = len(second)

        if m > 2 or n > 2:
            if m > 2:
                med2 = find_median(second)
                while m > 2:
                    med1 = find_median(first)
                    if med1 > med2:
                        first = first[:(m + m % 2) / 2]
                    else:
                        first = first[(m - m % 2) / 2:]
                    m = len(first)
            else:
                med1 = find_median(first)
                while n > 2:
                    med2 = find_median(second)
                    if med1 > med2:
                        second = second[(n - n % 2) / 2:]
                    else:
                        second = second[:(n + n % 2) / 2]
                    n = len(second)

        except I

        final_med = (max(first[0], second[0]) + min(first[1], second[1])) / 2
        return final_med

    def find_median(nums):
        res = 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return sum(nums) / 2

        if len(nums) % 2 == 0:
            num1 = len(nums) / 2
            num2 = num1 - 1
            res = (nums[num1] + nums[num2]) / 2
        else:
            res = nums[(len(nums) - 1) / 2]

        return res

sol1 = Solution()
arr1 = [1,3]
arr2 = [2]

print sol1.findMedianSortedArrays(arr1,arr2)