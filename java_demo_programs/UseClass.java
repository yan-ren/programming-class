public class UseClass {
    public static void main(String[] args) {
        // Student student1 = new Student();
        // student1.name = "jerry";
        // student1.studentID = 1;

        Student student1 = new Student(1, "jerry");
        System.out.println(student1.name);
        student1.printName();
        student1.getStudentID();

        Student.printMessage();

        // Student student2 = new Student();
        // student2.name = "tom";
        // student2.studentID = 2;

        //
        String text = new String("hello");

        // remove array duplicates
        // given an integer array, write a function that returns a new array with
        // duplicated value removed
        /*
         * {1, 2, 2, 3, 4, 5, 5}
         * 
         * {1, 2, 3, 4, 5}
         */

        /*
         * given two integer array, there is no duplicate in either array, combine two
         * arrays into one array by skipping duplicate values {1, 2, 3, 4, 5} {2, 6, 7}
         * 
         * {1, 2, 3, 4, 5, 6, 7}
         */
    }
}
