from typing import List

from nose.tools import assert_equal


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        min_time = time[0]
        max_time = min_time * totalTrips
        ans = 0
        print(min_time,max_time)

        while (min_time <=max_time):
            mid = (max_time + min_time) // 2
            trip = 0
            for t in time:
                if t <= mid:
                    trip += mid // t
            if trip < totalTrips:
                min_time = mid + 1
            else:
                ans = mid
                max_time = mid-1
        return ans


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([2],1), 2)
        assert_equal(sol([1,2,3],5), 3)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.minimumTime)
