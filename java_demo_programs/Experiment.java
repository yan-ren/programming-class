import java.util.List;

public class Experiment {
    /** The mechanical arm used to process the solutions */
    private MechanicalArm arm;
    /** The list of solutions */
    private List<Solution> solutions;

    /**
     * Resets the experiment.
     * Postcondition:
     * - The mechanical arm has a current index of 0.
     * - It is facing right.
     */
    public void reset() {
        /* to be implemented in part (a) */
        if (arm.isFacingRight()) {
            arm.changeDirection();
        }

        while (arm.getCurrentIndex() != 0) {
            arm.moveForward(1);
        }

        // face to the right
        arm.changeDirection();
    }

    /**
     * Finds and returns the index of the most acidic solution.
     * 
     * @return index the location of the most acidic solution
     *         or -1 if there are no acidic solutions
     *         Postcondition:
     *         - The mechanical arm is facing right.
     *         - Its current index is at the most acidic solution, or at
     *         0 if there are no acidic solutions.
     */
    public int mostAcidic() {
        /* to be implemented in part (b) */
        // find min ph and its index
        int minPH = Integer.MAX_VALUE;
        int minIndex = -1;

        // for(int i = 0; i < solutions.size(); i++) {
        // if(solutions.get(i).getPH() < minPH) {
        // minPH = solutions.get(i).getPH();
        // minIndex = i;
        // }
        // }

        int count = 0;
        for (Solution s : solutions) {
            if (s.getPH() < minPH) {
                minPH = s.getPH();
                minIndex = count;
            }

            count++;
        }

        if (minPH < 7) {
            reset();
            arm.moveForward(minIndex);
            return minIndex;
        }

        return -1;
    }
}
