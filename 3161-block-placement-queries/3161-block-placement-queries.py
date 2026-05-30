class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, val):
        idx += 1
        n = self.n + 1
        while idx < n:
            self.bit[idx] += val
            idx += idx & -idx

    def sum(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

    def kth(self, k):
        idx = 0
        bitmask = 1 << (self.n.bit_length())

        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bitmask >>= 1

        return idx


class SegTree:
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N <<= 1
        self.seg = [0] * (2 * self.N)

    def update(self, pos, val):
        p = pos + self.N
        self.seg[p] = val
        p >>= 1

        while p:
            self.seg[p] = max(self.seg[p * 2], self.seg[p * 2 + 1])
            p >>= 1

    def query(self, l, r):
        if l > r:
            return 0

        l += self.N
        r += self.N
        ans = 0

        while l <= r:
            if l & 1:
                ans = max(ans, self.seg[l])
                l += 1

            if not (r & 1):
                ans = max(ans, self.seg[r])
                r -= 1

            l >>= 1
            r >>= 1

        return ans


class Solution:
    def getResults(self, queries):
        MAXX = 50001

        final_obs = set()

        for q in queries:
            if q[0] == 1:
                final_obs.add(q[1])

        active = sorted(final_obs | {0, MAXX})

        prev = [-1] * (MAXX + 1)
        nxt = [-1] * (MAXX + 1)

        for i in range(len(active) - 1):
            a = active[i]
            b = active[i + 1]
            nxt[a] = b
            prev[b] = a

        bit = BIT(MAXX + 1)

        for x in active:
            bit.add(x, 1)

        seg = SegTree(MAXX + 2)

        for i in range(1, len(active)):
            seg.update(active[i], active[i] - active[i - 1])

        ans = []

        for q in reversed(queries):

            if q[0] == 2:
                x, sz = q[1], q[2]

                cnt = bit.sum(x)
                left = bit.kth(cnt)

                best = max(
                    seg.query(0, left),
                    x - left
                )

                ans.append(best >= sz)

            else:
                p = q[1]

                l = prev[p]
                r = nxt[p]

                seg.update(p, 0)
                seg.update(r, r - l)

                nxt[l] = r
                prev[r] = l

                bit.add(p, -1)

        return ans[::-1]