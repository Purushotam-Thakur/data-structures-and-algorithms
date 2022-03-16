class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        track = {}

        for n in nums2:
            while stack and stack[-1] < n:
                track[stack.pop()] = n
            stack.append(n)
        for n in stack:
            track[n] = -1

        return [track[x] for x in nums1]
