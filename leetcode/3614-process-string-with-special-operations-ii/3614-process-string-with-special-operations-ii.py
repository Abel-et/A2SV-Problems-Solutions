class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        current_length = 0

        # Step 1: Forward Pass to calculate the length at each step
        for ch in s:
            if ch == '*':
                if current_length > 0:
                    current_length -= 1
            elif ch == '#':
                current_length *= 2
            elif ch == '%':
                pass  # Reverse operation preserves the length
            else:
                current_length += 1
            lengths.append(current_length)

        # Out of bounds check
        if k < 0 or k >= current_length:
            return '.'

        # Step 2: Backward Pass to find the character at index k
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            prev_length = lengths[i - 1] if i > 0 else 0

            if ch == '*':
                # Characters removed at the end don't affect k's position
                continue
            elif ch == '#':
                # If k lies in the duplicated copy, map it back to the original half
                if k >= prev_length:
                    k -= prev_length
            elif ch == '%':
                # Invert the index to mirror the reversal string boundary
                k = prev_length - 1 - k
            else:
                # If k points directly to the newly appended character
                if k == prev_length:
                    return ch

        return '.'