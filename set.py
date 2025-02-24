# setはアドレスを保存する

# 集合を作成
visited = set()

# 集合に追加
visited.add((0, 0)) # {(0, 0)}
visited.add((0, 1)) # {(0, 1), (0, 0)}

# 存在を確認
(0, 0) in visited # True