# データアクセス　配列O(1)　連結リストO(n)
# データ挿入削除　配列O(n)　連結リストO(1)

import collections  # collections モジュールをインポート

# 連結リストをクラスとして定義
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 連結リスト作成
stack = collections.deque([5,4,3,2,1,0])
head = ListNode(stack.pop()) # ListNode(0) (val=0)
pos = head # 参照渡し
while stack:
    pos.next = ListNode(stack.pop())
    pos = pos.next

# 連結リストから値を取り出す
while head != None:
    print(head.val, end=" ") # 0 1 2 3 4 5
    head = head.next
