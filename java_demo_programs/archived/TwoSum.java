package archived;

public class TwoSum {
    public static void main(String[] args) {

    }

    /*
    Given an array of integers called nums and an integer called target, 
    there is only one pair of number in the array that sum is the target.
    Find the indices of the two numbers such that they add up to target
    */
    public static int[] twoSum(int[] candidates, int target){
        for(int i = 0; i < candidates.length; i++){
            for(int j = i+1; j < candidates.length; j++){
                if(candidates[i]+candidates[j] == target){
                    return new int[]{i, j};
                }
            }
        }

        return null;
    }
}
