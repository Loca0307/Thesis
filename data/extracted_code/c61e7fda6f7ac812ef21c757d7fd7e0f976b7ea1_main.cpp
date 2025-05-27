#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:

    int leftDepth = 1, rightDepth = 1;
    int maxDepth(TreeNode* root) {
        if ( root != nullptr ){
            (root->left != nullptr ? leftDepth++ : leftDepth);
            (root->right != nullptr ? rightDepth++ : rightDepth);
            leftDepth = findMaxDepth(root->left);
            rightDepth = findMaxDepth(root->right);
            return 1 + (leftDepth >= rightDepth ? leftDepth : rightDepth);
        }
        return 0;
    }

    int findMaxDepth(TreeNode* root){
        if ( root == nullptr ){
            return 0;
        }
        return 1 + (std::max(findMaxDepth(root->left), findMaxDepth(root->right)));
    }
};

int main(){

    /*
    TreeNode* tree1 = new TreeNode(-8);
    tree1->left = new TreeNode(-6);
    tree1->left->left = new TreeNode(6);
    tree1->left->left->right = new TreeNode(5);
    tree1->right = new TreeNode(7);
    */
    
    // TreeNode* tree1 = new TreeNode(3);
    // tree1->left = new TreeNode(9);
    // tree1->right = new TreeNode(20);
    // tree1->right->left = new TreeNode(15);
    // tree1->right->right = new TreeNode(7);
    
    /*
    TreeNode* tree1 = new TreeNode(3);
    tree1->left = new TreeNode(4);
    tree1->left->left = new TreeNode(-7);
    tree1->left->left->left = new TreeNode(-7);
    tree1->left->right = new TreeNode(-6);
    tree1->left->right->left = new TreeNode(-5);
    tree1->left->right->left->left = new TreeNode(-4);
    tree1->right = new TreeNode(5);
    */

    TreeNode* tree1 = new TreeNode(0);
    tree1->left = new TreeNode(2);
    tree1->left->left = new TreeNode(1);
    tree1->left->left->left = new TreeNode(5);
    tree1->left->left->right = new TreeNode(1);
    tree1->right = new TreeNode(4);
    tree1->right->left = new TreeNode(3);
    tree1->right->left->right = new TreeNode(6);
    tree1->right->right = new TreeNode(-1);
    tree1->right->right->right = new TreeNode(8);

    Solution solution;
    int res = solution.maxDepth(tree1);
    std::cout << res << std::endl;
}