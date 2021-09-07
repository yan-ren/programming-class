public class Student {
    // instance variable
    private int studentID;
    public String name;
    private double[] grades;
    private int gradeIndex;

    // static variable
    static int ID = 1;

    // constructor: special function that is called when creating object
    public Student(int studentID, String name) {
        this.studentID = studentID;
        this.name = name;
        this.grades = new double[5];
        this.gradeIndex = 0;
    }

    // write a function that can be used to add grade to grades array
    public void addGrade(double grade) {
        if (gradeIndex == grades.length) {
            return;
        }

        grades[gradeIndex] = grade;
        gradeIndex += 1;
    }

    public int getStudentID() {
        return studentID;
    }

    public void setStudentID(int id) {
        studentID = id;
    }

    // write a function that can return the average grade of student
    public double getAverage() {
        double sum = 0;
        for (int i = 0; i < gradeIndex; i++) {
            sum = sum + grades[i];
        }
        return sum / gradeIndex;
    }

    // instance function/ non-static function
    public void printName() {
        System.out.println(name);
    }

    // static function, called through class name
    public static void printMessage() {
        System.out.println("hello");
    }
}
