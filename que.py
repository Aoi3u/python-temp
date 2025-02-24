import collections

# キューの作成
queue = collections.deque([])

# 追加
queue.append(1) # deque([1])
queue.append(2) # deque([1, 2])

# 取り出し
queue.popleft() # deque([2])

# BFS (幅優先探索)
# 入力サイズを確認する
# 簡単な例から考える
# 幅優先探索は、問題をグラフとして扱える場合に有効なアルゴリズムである
    #  ある場所からある場所へ行くための経路を探す場合
    #  ある場所からある場所へ行くための最短経路を探す場合
    #  キューをスタックに置き換えれば、DFS(深さ優先探索)になる

# 1. 行ける場所を探すための explore関数 を作成
# 2. 行ける場所を保存しておく queue を作成
# 3. 訪れた場所を記録