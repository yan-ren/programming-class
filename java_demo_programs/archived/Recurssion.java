package archived;

public class Recurssion {
    public static void main(String[] args) {
        // System.out.println(factorial(4));
        // System.out.println(fib(5));

        int[] values = {1, 2, 3, 4, 5, 6, 7};
        System.out.println(binarySearchRecursive(values, 0, values.length - 1, 10));
    }

    // iterative approach
    public static int factorial(int n){
        int result = 1;
        while(n > 1) {
            result = result * n;
            n--;
        }

        return result;
    }

    // recurssive approach
    public static int factorialRecurrsive(int n) {
        // base case
        if(n == 1) {
            return 1;
        }
        // recurssive case
        return n * factorialRecurrsive(n-1);
    }

    // return nth fibonacci number
    public static int fib(int n) {
        int n1 = 1;
        int n2 = 1;
        int next = 1;

        if (n == 1 || n == 2){
            return 1;
        }

        for(int i = 1; i <= n - 2; i++){
            next = n1 + n2;
            n1 = n2;
            n2 = next;
        }

        return next;
    }

    // digits sum
    public static int digitsSum(int n) {
        // base case
        if(n < 10) {
            return n;
        }

        // % 10 gets the right most digits
        // / 10 remove the right most digits
        return n % 10 + digitsSum(n/10);
    }

    // recurssive print
    public static void recurssivePrint(int[] arr, int index) {
        if(index < 0){
            return;
        }
        // otherwise if index is not smaller than zero, we print the element on the index and decrease the index
        System.out.println(arr[index]);
        recurssivePrint(arr, index-1);
    }

    public static boolean binarySearchRecursive(int[] arr, int low, int high, int target) {
        // base case
        if(low > high){
            return false;
        }
        
        int mid = (low + high) / 2;
        // base case
        if(arr[mid] == target) {
            return true;
        }

        if(arr[mid] > target) {
            return binarySearchRecursive(arr, low, mid - 1, target);
        }else {
            return binarySearchRecursive(arr, mid + 1, high, target);
        }

    }

    public static String reverseStringRecursion(String string) {
        if (string == "") {
            return string;
        }

        //
        // if (string.length() == 1) {
        //     return string;
        // }

        return reverseStringRecursion(string.substring(1)) + string.charAt(0);
    }
}

/*
Given an array of integers called nums and an integer called target, 
there is only one pair of number in the array that sum is the target.
Find the  indices of the two numbers such that they add up to target

nums = [2, 7, 15, 11]

loop1
{2: 0, 7: 1, 15: 2, 11: 3}

2

target = 9

return [0, 1]
*/

/*
write a function that reverses a string using recursion

input: abc
output: cba
*/