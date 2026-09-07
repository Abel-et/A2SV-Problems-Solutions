class Solution:

  def distinctSubseqII(self, s: str) -> int:
    MOD = 10**9 + 7
    # Stores total subsequences ending in each character ('a' to 'z')
    last_added = [0] * 26
    dp = 0  # Total distinct non-empty subsequences

    for char in s:
      idx = ord(char) - ord("a")

      # Subsequences created by appending `char`
      new_added = (dp + 1 - last_added[idx]) % MOD

      # Update running totals
      dp = (dp + new_added) % MOD
      last_added[idx] = (last_added[idx] + new_added) % MOD

    return dp

    
        