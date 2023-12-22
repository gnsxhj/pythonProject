# 28. 找出字符串中第一个匹配项的下标
class Solution:
    def strStr(self, haystack:str, needle:str) -> int:
        # return haystack.find(needle) # 用find内置函数

        # 用切片法来做
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

print(Solution().strStr("iloveyou", "love"))
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