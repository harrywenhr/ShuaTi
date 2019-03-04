https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

preoder: root, left, right
inorder: left, root, right

[root, left1,left2,left3,right1,right2]
[left1,left2, left3, root, right1, right2]

when we get a node from preorder, we treat as a current root, we find that same value
in inorder travel (relative order), so the left part length of inorder travel equals the left part 
nodes in preorder travel, we recursively send the left part and right part


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #we hash the inorder values
        vmap = {}
        for i in range(len(inorder)):
            vmap[inorder[i]] = i

        def helper(preorder, inorder):
            #base case
            if not preorder or not inorder:
                return None
            currentRootValue = preorder[0]
            #find matching index, careful we need the relative rootIndex as the inorder
            #list is not the original one
            originalRootIndex = vmap[currentRootValue]
            relativeRootIndex = originalRootIndex - vmap[inorder[0]]

            currentRoot = TreeNode(currentRootValue)
            leftNode = helper(preorder[1:relativeRootIndex + 1], inorder[:relativeRootIndex])
            rightNode = helper(preorder[relativeRootIndex + 1:], inorder[relativeRootIndex + 1:])
            currentRoot.left = leftNode
            currentRoot.right = rightNode
            return currentRoot
        return helper(preorder, inorder)



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        vmap = {}
        for i in range(len(inorder)):
            vmap[inorder[i]] = i
        return self.helper(preorder, inorder, vmap)
    def helper(self, remainPreorder, remainInorder, vmap):
        if not remainPreorder or not remainInorder:
            return None
        currentNodeValue = remainPreorder[0]
        relativeNodeIndex = vmap[currentNodeValue] - vmap[remainInorder[0]]
        leftNode = self.helper(remainPreorder[1:relativeNodeIndex + 1], remainInorder[:relativeNodeIndex], vmap)
        rightNode = self.helper(remainPreorder[relativeNodeIndex + 1:], remainInorder[relativeNodeIndex + 1:], vmap)
        currentNode = TreeNode(currentNodeValue)
        
        currentNode.left = leftNode
        currentNode.right = rightNode
        return currentNode
        