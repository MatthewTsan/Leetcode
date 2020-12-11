class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = (0, len(s) + 1)
        dictT = dict()
        for item in t:
            dictT[item] = dictT[item] + 1 if item in dictT else 1
        dictS = dict()

        # Too much time
        # def match(dictS, dictT):
        #     for item in t:
        #         if dictS.get(item, 0) < dictT.get(item, 0):
        #             return False
        #     return True

        i, j = -1, 0
        temPos = []
        flag = 0
        while (j < len(s)):
            if s[j] not in dictT:
                j += 1
                continue
            dictS[s[j]] = dictS[s[j]] + 1 if s[j] in dictS else 1
            if dictS[s[j]] == dictT[s[j]]:
                flag += 1
            temPos.append(j)

            i = temPos[0]
            while (dictS[s[i]] > dictT[s[i]] and len(temPos) > 1):
                dictS[s[i]] -= 1
                if dictS[s[i]] == dictT[s[i]] - 1:
                    flag -= 1
                del temPos[0]
                i = temPos[0]

            # if match(dictS, dictT):
            if flag == len(dictT):
                if result[1] - result[0] > j - i + 1:
                    result = (i, j + 1)
            j += 1
        return "" if result[1] == len(s) + 1 else s[result[0]:result[1]]