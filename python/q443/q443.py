from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        ans = []
        cur = chars[0]
        time = 1
        for c in chars[1:]:
            if c == cur:
                time += 1
                continue
            # append the ans, with times
            ans.append(cur)
            if time > 1:
                strTime = str(time)
                for i in range(len(strTime)):
                    ans.append(strTime[i])
            # initial the para
            cur = c
            time = 1

        ans.append(cur)
        if time > 1:
            strTime = str(time)
            for i in range(len(strTime)):
                ans.append(strTime[i])

        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)