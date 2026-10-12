
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        # Step 1: Count occurrences of each bit.
        bit_count = [0] * 31

        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    bit_count[bit] += 1

        # Step 2: Greedily construct k numbers.
        answer = 0

        for _ in range(k):
            x = 0

            for bit in range(31):
                if bit_count[bit] > 0:
                    x |= (1 << bit)
                    bit_count[bit] -= 1

            # Step 3: Add the square modulo MOD.
            answer = (answer + x * x) % MOD

        return answer
