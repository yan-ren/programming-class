package datastructure;

import java.util.Collection;
import java.util.Collections;
import java.util.PriorityQueue;

public class Test {
    public static void main(String[] args) {
        // BST binarySearchTree = new BST();
        // binarySearchTree.insert(8);
        // binarySearchTree.insert(3);
        // binarySearchTree.insert(1);
        // binarySearchTree.insert(6);
        // binarySearchTree.insert(4);
        // binarySearchTree.insert(7);
        // binarySearchTree.insert(10);
        // binarySearchTree.insert(14);
        // binarySearchTree.insert(13);

        // // call inorder traversal
        // binarySearchTree.inorder();

        // PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        // queue.add(2);
        // queue.add(1);
        // queue.add(3);

        // System.out.println(queue.poll());
        // System.out.println(queue);

        PriorityQueue<Number> queue = new PriorityQueue<>();
        // queue.add(new Number(1, 2));

        Number n1 = new Number(2, 0);
        Number n2 = new Number(1, 1);
        queue.add(n2);
        queue.add(n1);

        System.out.println(queue.poll());
    }
}

class Number implements Comparable<Number> {
    public int value;
    public int priority;

    public Number(int value, int priority) {
        this.value = value;
        this.priority = priority;
    }

    @Override
    public int compareTo(Number anotherNumber) {
        if (this.priority == anotherNumber.priority) {
            return 0;
        }

        if (this.priority > anotherNumber.priority) {
            return 1;
        } else {
            return -1;
        }
    }

    public String toString() {
        return "[value: " + value + ", priority: " + priority + "]";
    }
}
