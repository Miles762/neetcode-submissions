# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stackk = []

        while True:
            while root: #go as far as left as possiblr
                stackk.append(root)
                root = root.left
            
            ans_root = stackk.pop() 
            k-=1
            if k == 0:
                return ans_root.val
            
            root = ans_root.right   

        