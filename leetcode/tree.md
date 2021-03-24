# Tree

+[Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)

+[Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)

+[Invert Binary Tree](#invert-binary-tree)

+[Binary Search Tree Iterator](#binary-search-yree-iterator)

+[Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)

+[Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)

+[Validate Binary Search Tree](#validate-binary-search-tree)

+[Symmetric Tree](#symmetric-tree)

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/ 

```python
def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/ 

```python
def inorder(self, node, order):
        if node is None:
            return
        self.inorder(node.left, order)
        order.append(node.val)
        self.inorder(node.right, order)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        order = []
        self.inorder(root, order)
        return order
```

## Invert Binary Tree 

https://leetcode.com/problems/invert-binary-tree/ 

```python
def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        self.invertTree(root.left)
        self.invertTree(root.right)
       
        return root
```

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python
def __init__(self, root: TreeNode):
        self.index = -1
        self.arr = []
        self.helper(root)
        
    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.arr.append(root.val)
        self.helper(root.right)

    def next(self) -> int:
        self.index += 1
        return self.arr[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.arr)
```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/ 

```python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
        arr = []
        def helper(i, root):
            if root:
                if i >= len(arr):
                    arr.append([])
                arr[i].append(root.val)
                helper(i+1, root.left)
                helper(i+1, root.right)
        helper(0, root)
        return arr
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/ 

```python
def kthSmallest(self, root: TreeNode, k: int) -> int:
        A = []
        res = self.inord(root, A)
        return res[k-1]
    def inord(self, node, A):
        if node.left:
            self.inord(node.left, A)
        A.append(node.val)
        if node.right:
            self.inord(node.right, A)    
        return A
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
def isValidBST(self, root: TreeNode) -> bool:
        def recursion(node, mn = float('-inf'), mx = float('inf')):
            if not node:
                return True
            if node.val <= mn or node.val >= mx:
                return False
            return (recursion(node.right, node.val, mx) and recursion(node.left, mn, node.val))
        return recursion(root)
```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/ 

```python
def check(self, node, node2):
        if node == None and node2 == None:
            return 1
        if node != None and node2 != None:
            if node.val == node2.val:
                return(self.check(node.left, node2.right)*self.check(node.right, node2.left))
        return 0
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)
```
