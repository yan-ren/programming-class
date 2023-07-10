package datastructure;

import java.util.LinkedList;
import java.util.Queue;

import javax.naming.PartialResultException;

class Node {
    int data;
    Node left;
    Node right;

    public Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

public class BST {

    Node root;

    // public void insert(int data) {
    //     root = recursiveInsert(root, data);
    // }

    public Node recursiveInsert(Node node, int data) {
        // base case
        if (node == null) {
            node = new Node(data);
            return node;
        }

        // recursive case
        if (data < node.data) {
            node.left = recursiveInsert(node.left, data);
        } else {
            node.right = recursiveInsert(node.right, data);
        }

        return node;
    }

    // non recursive insert
    public void insert(int data) {
        if (root == null) {
            root = new Node(data);
            return;
        }

        Node newNode = new Node(data);
        Node current = root;
        Node parent = null;

        while(true) {
            parent = current;
            if (data < current.data) {
                current = current.left;
                if (current == null) {
                    parent.left = newNode;
                    return;
                }
            } else if (data > current.data) {
                current = current.right;
                if (current == null) {
                    parent.right = newNode;
                    return;
                }
            }
        }
    }

    public void inorder() {
        inorderTraveral(root);
    }

    private void inorderTraveral(Node node) {
        // base case
        if (node == null) {
            return;
        }

        // visit the left subtree
        inorderTraveral(node.left);
        // visit the node
        System.out.println(node.data);
        // visit the right subtree
        inorderTraveral(node.right);
    }

    public void preorder() {
        preorderTraveral(root);
    }

    private void preorderTraveral(Node node) {
        // base case
        if (node == null) {
            return;
        }

        // visit the node
        System.out.println(node.data);
        // // visit the left subtree
        // inorderTraveral(node.left);
        // // visit the right subtree
        // inorderTraveral(node.right);
        /*
         * for each child of node
         *      preorderTraveral(child)
         */
    }

    // private void breadthFirstTraversal(Node node) {
    //     Queue<Node> queue = new LinkedList<>();
    //     queue.add();
    //     queue.remove();
    // }

    // non-recursive node deletion
    public void delete(int target) {
        Node current = this.root;
        Node parent = null;

        // find the node needs to be deleted
        while (current != null && current.data != target) {
            parent = current;
            if(target < current.data) {
                current = current.left;
            } else {
                current = current.right;
            }
        }

        // if target does not exist
        if (current == null) {
            return;
        }

        // case 1: node has only one child
        if (current.left == null) {
            // edge case, when remove the root
            if (parent == null) {
                this.root = current.right;
            } else if( current == parent.left) {
                parent.left = current.right;
            } else {
                parent.right = current.right;
            }
        } else if (current.right == null) {
            // edge case
            if (parent == null) {
                this.root = current.left;
            } else if (current == parent.left) {
                parent.left = current.left;
            } else {
                parent.right = current.left;
            }
        }
        // case2: when current node has two children. strategy: find the min on right subtree and move min value to current
        else {
            Node minRight = findMin(current.right);
            current.data = minRight.data;
            delete(minRight.data);
        }

    }

    // find the minimum value from the node
    public Node findMin(Node node) {
        while(node.left != null) {
            node = node.left;
        }

        return node;
    }

}