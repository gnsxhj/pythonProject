# # 1572. 矩阵对角线元素的和
# from typing import List


# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         n, res = len(mat), 0
#         for i in range(n):
#             res += mat[i][i]
#             mat[i][i] = 0
#             res += mat[i][n - i - 1]
#             print(mat[i][n - i - 1])

#         return res


# # class Solution:
# #     def diagonalSum(self, mat: List[List[int]]) -> int:
# #         ans = 0
# #         n = len(mat)
# #         for i, row in enumerate(mat):
# #             j = n - i - 1
# #             print(j, n, i)
# #             print(row[i], row[j])
# #
# #
# print(Solution().diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# # 1041. 困于环中的机器人
# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         # north = 0, east = 1, south = 2, west = 3
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         # Initial position is in the center
#         x = y = 0
#         # facing north
#         idx = 0
#
#         for i in instructions:
#             if i == "L":
#                 idx = (idx + 3) % 4
#             elif i == "R":
#                 idx = (idx + 1) % 4
#             else:
#                 x += directions[idx][0]
#                 y += directions[idx][1]
#
#         # after one cycle:
#         # robot returns into initial position
#         # or robot doesn't face north
#         return (x == 0 and y == 0) or idx != 0
#
#
# class Solution:
#     def isRobotBounded(self, s: str) -> bool:
#         x, y, d = 0, 0, 0
#         dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
#         for c in s:
#             if c == 'G':
#                 x += dirs[d][0]
#                 y += dirs[d][1]
#                 print(x, y)
#             elif c == 'L':
#                 d = (d + 1) % 4
#                 print(d)
#             else:
#                 d = ((d - 1) % 4 + 4) % 4
#                 print(d)
#         return (x == 0 and y == 0) or d != 0
#
#
# print(Solution().isRobotBounded('LGLGLGLG'))
# # 1275. 找出井字棋的获胜者
# from typing import List
#
#
# class Solution:
#     def tictactoe(self, moves: List[List[int]]) -> str:
#         length_moves = len(moves)
#         if length_moves % 2 == 1:
#             pos = 0
#         else:
#             pos = 1
#         tic = []
#         for i in range(pos, length_moves, 2):
#             tic.append(moves[i])
#         for n, ele in enumerate(tic):
#             choice = tic[n]
#             for subele in tic:
#                 if subele != choice:
#                     x = (subele[0] + choice[0]) / 2
#                     y = (subele[1] + choice[1]) / 2
#                     if [x, y] in tic:
#                         if pos:
#                             return "B"
#                         else:
#                             return "A"
#         if length_moves == 9:
#             return 'Draw'
#         return 'Pending'
#
#
# class Solution:
#     def tictactoe(self, moves: List[List[int]]) -> str:
#         playA = []
#         playB = []
#
#         for step in range(0, len(moves), 2):
#             playA.append(moves[step])
#         for step in range(1, len(moves), 2):
#             playB.append(moves[step])
#         for n, ele in enumerate(playA):
#             choice = playA[n]
#             for subele in playA:
#                 if subele != choice:
#                     x = (subele[0] + choice[0]) / 2
#                     y = (subele[1] + choice[1]) / 2
#                     if [x, y] in playA:
#                         return "A"
#         for n, ele in enumerate(playB):
#             choice = playB[n]
#             for subele in playB:
#                 if subele != choice:
#                     x = (subele[0] + choice[0]) / 2
#                     y = (subele[1] + choice[1]) / 2
#                     if [x, y] in playB:
#                         return "B"
#         if len(moves) == 9:
#             return "Draw"
#         else:
#             return "Pending"
#
#
# print(Solution().tictactoe([[0, 0], [2, 0]]))
# print(Solution().tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
# print(Solution().tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
# print(Solution().tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))
#
# # 896. 单调数列
# from typing import List
# class Solution:
#     def isMonotonic(self, nums: List[int]) -> bool:
#         n = sorted(nums, reverse=False)
#         m = sorted(nums, reverse=True)
#         if n != nums and m != nums:
#             return False
#         else:
#             return True
# print(Solution().isMonotonic([1, 2, 2, 3]))
#
# # 1822. 数组元素积的符号
# from typing import List
#
#
# class Solution:
#     def arraySign(self, nums: List[int]) -> int:
#         product = 1
#         for n in nums:
#             product *= n
#             if product == 0:
#                 return 0
#                 break
#         if product > 0:
#             return 1
#         elif product < 0:
#             return -1
#
#
# print(Solution().arraySign([-1, 0, 1, -1, 2, 3, 4]))
#
# # 66. 加一
# from typing import List
#
#
# class Solution1:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for i in range(len(digits) - 1, -1, -1):
#             if digits[i] != 9:
#                 digits[i] += 1
#                 return digits
#             else:
#                 digits[i] = 0
#                 if digits[0] == 0:
#                     digits.insert(0, 1)
#                     return digits
#
#
# class Solution2:  # 这个解法是错误的
#     def plusOne(self, digits: List[int]) -> List[int]:
#         n = len(digits)
#         while n > 0:
#             if digits[n - 1] == 9:
#                 digits[n - 1] = 0
#                 n -= 1
#             else:
#                 digits[n - 1] = digits[n - 1] + 1
#                 return digits
#         if n == 0:
#             return digits + [1]
#
#
# print(Solution2().plusOne([9, 9, 9, 9, 9]))
# 459. 重复的子字符串
# # 242. 有效的字母异位词
# from collections import Counter, defaultdict
#
#
# class Solution1:  # 直接初始化计数器
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         return Counter(s) == Counter(t)
#
#
# class Solution2:  # 利用Counter计数器基数字符
#     def isAnagram(self, s: str, t: str) -> bool:
#         c = Counter()
#         for i in s:
#             c[i] += 1
#         for j in t:
#             c[j] -= 1
#             if c[j] == 0:
#                 del c[j]
#         return True if len(c) == 0 else False
#
#
# class Solution4:  # 利用Counter计数器基数字符
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         dic = defaultdict(int)
#         for i in s:
#             dic[i] += 1
#         for j in t:
#             dic[j] -= 1
#         for val in dic.values():
#             if val != 0:
#                 return False
#         return True
#
#
# class Solution3:  # 利用列表作为哈希表
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         record = [0] * 26
#         for i in s:
#             record[ord(i) - ord('a')] += 1
#         for j in t:
#             record[ord(j) - ord('a')] -= 1
#         for number in record:
#             if number != 0:
#                 return False
#         return True
#
#
# print(Solution3().isAnagram('acts', 'cats'))
# # 283. 移动零
# class Solution1:
#     def moveZeroes(self, nums):
#         i = j = 0
#         for i in range(len(nums)):
#             # if nums[i] != 0: # 将所有的0移到末尾
#             if nums[i] == 0:  # 将所有的0移到开头
#                 nums[j], nums[i] = nums[i], nums[j]
#                 j += 1
#         print(nums)
# class Solution2:
#     def moveZeroes(self, nums):
#         n = len(nums)
#         p = 0
#         while p < n:
#             if nums[p] == 0:
#                 q = p + 1
#                 while q < n:
#                     if nums[q] != 0:
#                         nums[p], nums[q] = nums[q], nums[p]
#                         break
#                     q += 1
#             p += 1
#         print(nums)
# print(Solution2().moveZeroes([0, 4, 0, 3, 1]))
# # 28. 找出字符串中第一个匹配项的下标
# class Solution:
#     def strStr(self, haystack:str, needle:str) -> int:
#         # return haystack.find(needle) # 用find内置函数
#
#         # 用切片法来做
#         for i in range(0, len(haystack)-len(needle)+1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i
#         return -1
#
# print(Solution().strStr("iloveyou", "love"))
# # 389.找不同
# from collections import Counter
# class Solution:
#     def findTheDifference(self, s:str, t:str) -> str:
#
#         # return list(Counter(t)-Counter(s))[0] # 用Counter的方法来实现
#
#         # for i in t: # 用减差值的方式来实现
#         #     if t.count(i) - s.count(i) == 1:
#         #         return i
#
#         for k, v in Counter(t).items():
#             if not s.count(k) == v:
#                 return k
#
# print(Solution().findTheDifference("abcd", "abcde"))
#
# # Counter的用法：
# list = ["a", "b", "b", "c", "c", "c"]
# dic = Counter(list)
# print(dic)
# print(dict(dic))
# print(dic.items())
# print(dic.keys())
# print(dic.values())
# print(sorted(dic.items(), key=lambda s: (-s[1])))
# for i, v in dic.items():
#     if v == 1:
#         print(i)
# # 1480. 一维数组的动态和
# class solution:
#     def runningSum(self, nums):
#         dp = [0] * len(nums)
#         dp[0] = nums[0]
#         for i in range(1, len(nums)):
#             dp[i] = dp[i-1] + nums[i]
#         return dp
#
# test = solution()
# print(test.runningSum([1,3,4,5]))

# # 1672. 最富有客户的资产总量
# class solution:
#     def maxWealth(self, accounts):
#         # return max(sum(accounts[i]) for i in range(len(accounts)))
#         return max(map(sum, accounts))
#
# # return max(sum(accounts[i]) for i in range(len(accounts)))
# test = solution()
# print(test.maxWealth([[1, 2, 3, 5, 10], [2, 4, 6]]))

# # 412. FizzBuzz
# class solution:
#     def FizzBuzz(self, n):
#         # ans = []
#         # for i in range(1, n+1):
#         #     flag1, flag2 = i%3==0, i%5==0
#         #     if flag1 or flag2:
#         #         ans.append('Fizz'*flag1 + 'Buzz'*flag2)
#         #     else:
#         #         ans.append(f'{i}')
#         # return ans
#         return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
# test = solution()
# print(test.FizzBuzz(30))

# # 383.赎金信
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine:str)-> bool:
#         for i in ransomNote:
#             if i in magazine:
#                 # magazine = magazine.replace(i, "", 1) # 用replace把找到的字符串元素替换掉
#                 key = magazine.find(i)
#                 magazine = magazine[0:key] + magazine[key+1:]
#             else:
#                 return False
#         return True
# if __name__ == "__main__":
#     ransomNote = "abc"
#     magazine = "acatandaboy"
#     print(Solution().canConstruct(ransomNote, magazine))

# # 1768.交替合并字符串
# import itertools as it
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         return "".join(sum(it.zip_longest(word1, word2, fillvalue=""), ()))
#
# # if __name__ == "__main__":
# #     word1 = "abc"
# #     word2 = "xyz"
# print(Solution().mergeAlternately("abc", "xyz"))
#
# # zip unzip zip_longest的用法
# fruits = ['apple', 'banana', 'melon', 'strawberry', 'orange']
# fruits_ch = ['苹果', '香蕉', '瓜', '草莓']
#
# for f in fruits:
#     print(f, end=', ')
# print('\n')
#
# for i in range(len(fruits)):
#     print(i, fruits[i], end=', ')
# print('\n')
#
# # 这种方法只有在长度相等的时候才能用，否则出错
# # for j in range(len(fruits)):
# # 判断最小长度为遍历范围
# min_len = min(len(fruits), len(fruits_ch))
# for j in range(min_len):
#     print(fruits[j], '--->', fruits_ch[j])
#
# # 用zip来聚合
# zipPair = zip(fruits, fruits_ch)
# print(zipPair)
# print(list(zipPair))
#
# fruits = ['apple', 'banana', 'melon', 'strawberry']
# prices = [10, 20, 30]
# print(list(it.zip_longest(fruits, prices, fillvalue="")))
