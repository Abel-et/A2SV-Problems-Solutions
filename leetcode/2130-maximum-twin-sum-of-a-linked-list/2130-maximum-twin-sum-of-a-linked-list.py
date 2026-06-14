# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        if not head:
            return 0
        current = head

        while current:
            nums.append(current.val)
            current = current.next

        left , right = 0  , len(nums)-1
        ans = 0
        while left < right:
            ans = max(ans , nums[left] + nums[right])
            left += 1
            right -=1
        return ans


