# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Reference https://leetcode.com/problems/binary-tree-paths/discuss/68507/8-lines-in-python48ms
        
        
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        treepaths = [str(root.val)+'->'+path for path in self.binaryTreePaths(root.left)]
        treepaths += [str(root.val)+'->'+path for path in self.binaryTreePaths(root.right)]
        
        '''
        root.val, root.left, root.right are exist
            self.binaryTreePaths(root.left[Here, 2->[None & 5]]) -> ['2->5']
                ### Currently, no return yet ###
                Since 2->[None & 5], root.val = 2, root.left = None, root.right = 5,
                Thus, again, self.binaryTreePaths(root.right[Here, 5->[None & None]]) -> [5]
                    Since root.val(=5) exist but root.left and root.right are not exist,
                        return [str(root.val(=5))]
                        ### Now finally get the first return [5] ###
                Since self.binaryTreePaths(root.right[Here, 5->[None & None]]) returns [5],
                In the process of self.binaryTreePaths(root.left[Here, 2->[None & 5]]),
                treepaths = [str(root.val)+'->'+path in [5]]
                Thus, it returns ['2->5']
            Now, we can clearly understand the process from the top node.
            treepaths = [str(root.val)+'->'+path for path in self.binaryTreePaths(root.left)]
                      = [    1        +'->'+path for path in           ['2->5']             ]
        '''
        
        return treepaths