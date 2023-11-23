# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        def dfs(root):
            if not root:
                return
        
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
            return
            
        dfs(root)
        print(res)
        sortedL = sorted(res)
        print(sortedL)
        return sortedL[k-1]
