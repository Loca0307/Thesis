// I had to do these with the help of chatGPT. 

class Node {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

class BinarySearchTree {
  constructor(root = null) {
    this.root = root;
  }

  /** insert(val): insert a new node into the BST with value val.
   * Returns the tree. Uses iteration. */

  
  insert(val) {
    if(!this.root) {
      this.root = new Node(val);
      return this
  }
  
  let currentNode = this.root;
  while (true) {
    if(val < currentNode.val) {
      if(!currentNode.left) {
        currentNode.left = new Node(val);
        return this;
      }
      currentNode = currentNode.left;
    } else if (val > currentNode.val) {
      if (!currentNode.right) {
        currentNode.right = new Node(val);
        return this;
      }
      currentNode = currentNode.right;
    } else {

      return this
    }
  }

  }

  /** insertRecursively(val): insert a new node into the BST with value val.
   * Returns the tree. Uses recursion. */

  
  insertRecursively(val, currentNode = this.root) {
    if (!currentNode) {
      this.root = new Node(val);
      return this;
    }

    if (val < currentNode.val) {
      if (!currentNode.left) {
        currentNode.left = new Node(val);
      } else {
        this.insert(val, currentNode.left);
      }
    } else if (val > currentNode.val) {
      if (!currentNode.right) {
        currentNode.right = new Node(val);
      } else {
        this.insert(val, currentNode.right);
      }
    }
    // If val is equal to currentNode.val, handle as needed
    // Here, we'll avoid duplicates, but you can change this behavior if needed
    return this;
  }

  /** find(val): search the tree for a node with value val.
   * return the node, if found; else undefined. Uses iteration. */

  
  find(val) {
    let currentNode = this.root;

    if(!currentNode) {
      return null
    }
    while(currentNode) {
      if( currentNode.val === val ) {
        return currentNode
      } else if (val < currentNode.val) {
        currentNode = currentNode.left;
      } else {
        currentNode = currentNode.right
      }
    }
    return undefined;
  }

  /** findRecursively(val): search the tree for a node with value val.
   * return the node, if found; else undefined. Uses recursion. */

  findRecursively(val, currentNode = this.root) {
    if (!currentNode) {
        return undefined; 
    }

    if (val === currentNode.val) {
        return currentNode; 
    }

    if (val < currentNode.val) {
        return this.find(val, currentNode.left); 
    } else {
        return this.find(val, currentNode.right); 
    }
}


  /** dfsPreOrder(): Traverse the array using pre-order DFS.
   * Return an array of visited nodes. */

  dfsPreOrder() {
    if (!this.root) {
        return [];
    }

    const visited = [];
    const stack = [];
    let currentNode = this.root;

    while (currentNode || stack.length > 0) {
        if (currentNode) {
            visited.push(currentNode.val);
            

            if (currentNode.right) {
                stack.push(currentNode.right);
            }


            currentNode = currentNode.left;
        } else {

            currentNode = stack.pop();
        }
    }

    return visited;
}


  /** dfsInOrder(): Traverse the array using in-order DFS.
   * Return an array of visited nodes. */

  dfsInOrder() {
    if (!this.root) {
        return [];
    }

    const visited = [];
    const stack = [];
    let currentNode = this.root;

    while (currentNode || stack.length > 0) {
        if (currentNode) {

            stack.push(currentNode);
            currentNode = currentNode.left;
        } else {

            currentNode = stack.pop();
            visited.push(currentNode.val);
            currentNode = currentNode.right;
        }
    }

    return visited;
}


  /** dfsPostOrder(): Traverse the array using post-order DFS.
   * Return an array of visited nodes. */

  dfsPostOrder() {
    if (!this.root) {
        return [];
    }

    const visited = [];
    const stack1 = [];
    const stack2 = [];
    let currentNode = this.root;

    stack1.push(currentNode);

    while (stack1.length > 0) {
        currentNode = stack1.pop();
        stack2.push(currentNode);

        if (currentNode.left) {
            stack1.push(currentNode.left);
        }

        if (currentNode.right) {
            stack1.push(currentNode.right);
        }
    }

    while (stack2.length > 0) {
        visited.push(stack2.pop().val);
    }

    return visited;
}


  /** bfs(): Traverse the array using BFS.
   * Return an array of visited nodes. */

  bfs() {
    if (!this.root) {
        return [];
    }

    const visited = [];
    const queue = [];
    queue.push(this.root);

    while (queue.length > 0) {
        const currentNode = queue.shift(); // Dequeue
        visited.push(currentNode.val);

        if (currentNode.left) {
            queue.push(currentNode.left); // Enqueue left child
        }

        if (currentNode.right) {
            queue.push(currentNode.right); // Enqueue right child
        }
    }

    return visited;
}


  /** Further Study!
   * remove(val): Removes a node in the BST with the value val.
   * Returns the removed node. */

  remove(val) {

  }

  /** Further Study!
   * isBalanced(): Returns true if the BST is balanced, false otherwise. */

  isBalanced() {

  }

  /** Further Study!
   * findSecondHighest(): Find the second highest value in the BST, if it exists.
   * Otherwise return undefined. */

  findSecondHighest() {
    
  }
}

module.exports = BinarySearchTree;