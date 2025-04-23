import heapq

# 通常のリスト
heap = [4, 5, 8, 2]

# リストをヒープに変換
heapq.heapify(heap) # [2, 4, 5, 8]

# 最小の要素にアクセス
heap[0] # 2

# 最小の要素を取り出す
heapq.heappop(heap) # [4, 5, 8]

# 要素を追加
heapq.heappush(heap, 5) # [4, 5, 5, 8]

# ヒープキューの要素数
len(heap) # 4
