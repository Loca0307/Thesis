// console.log("In-order Traversal:");
// inOrderTraversal(root); // Output: 4 2 5 1 6 3 7

// task 10
{
  class TreeNode {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }

  function calculateDepth(node) {
    // Base case: If the node is null, return 0
    if (node === null) {
      return 0;
    }

    // Recursive case: Calculate the depth of left and right subtrees
    const leftDepth = calculateDepth(node.left);
    const rightDepth = calculateDepth(node.right);

    // The depth of the current node is the maximum of leftDepth and rightDepth plus 1
    return Math.max(leftDepth, rightDepth) + 1;
  }

  // Test the function with a sample binary tree
  const root = new TreeNode(1);
  root.left = new TreeNode(2);
  root.right = new TreeNode(3);
  root.left.left = new TreeNode(4);
  root.left.right = new TreeNode(5);
  root.right.left = new TreeNode(6);
  root.right.right = new TreeNode(7);

//   console.log("Depth of the tree:", calculateDepth(root)); // Output: 3

  // Another test case with an unbalanced tree
  const unbalancedRoot = new TreeNode(1);
  unbalancedRoot.left = new TreeNode(2);
  unbalancedRoot.left.left = new TreeNode(3);

//   console.log("Depth of the unbalanced tree:", calculateDepth(unbalancedRoot)); // Output: 3
}