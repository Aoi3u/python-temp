import itertools

# リストを用意
list = ["0", "1", "2", "3"]

# リストから順列生成
for p in itertools.permutations(list, 2):
    print(p) # ('0', '1') ~ ('3', '2')

# リストから組み合わせ生成
for c in itertools.combinations(l, 2):
    print(c) # ('0', '1') ~ ('2', '3')