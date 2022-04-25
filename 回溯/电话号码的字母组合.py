# 17.
# 电话号码的字母组合
# 给定一个仅包含数字2 - 9的字符串，返回所有它能表示的字母组合。答案可以按任意顺序
# 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意

# 不对应任何字母。
#
#
#
#
#
# 示例
# 1：
#
# 输入：digits = "23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# 示例
# 2：
#
# 输入：digits = ""
# 输出：[]
# 示例
# 3：
#
# 输入：digits = "2"
# 输出：["a", "b", "c"]
# 这道题的关键点在于如何回溯，可以查看图片。
class Solution:
    def letterCombinations(self, digits: str):
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)
        res = []
        path = []
        print(n)

        def dfs(p, r, index):
            if index == n:
                res.append("".join(p))
                return
            for i in phoneMap[digits[index]]:
                dfs(p + [i], r, index + 1)

        print(res)
        dfs(path, res, 0)
        return res


s = Solution()
s.letterCombinations(digits="23")
