import collections

# リストを用意
nums = [1,1,1,2,2,3]

# 頻度計算
c = collections.Counter(nums) # Counter({1: 3, 2: 2, 3: 1})

# 最も多いn要素を獲得
c.most_common(2) # [(1, 3), (2, 2)]