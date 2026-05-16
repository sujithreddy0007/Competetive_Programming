from collections import deque

class Solution:
    def bfs(self, adj):
        V = len(adj)

        queue = deque()
        queue.append(0)

        ans = []
        vist = [0] * V
        vist[0] = 1

        while queue:
            start = queue.popleft()
            ans.append(start)

            for it in adj[start]:
                if vist[it] == 0:
                    vist[it] = 1
                    queue.append(it)

        return ans