public class Student extends Person {
    // data
    private int studentId;
    String name;
    double[] grades;
    int gradeIndex = 0;
    Course[] courses;

    public Student() {
    }

    public Student(int studentId) {
        super(studentId, "", "");
        this.studentId = studentId;
    }

    public Student(int studentId, String name) {
        super(studentId, "", name);
        this.studentId = studentId;
        this.name = name;
        grades = new double[5];
        courses = new Course[5];
    }

    // __init__
    // method overloading
    public void method1() {

    }

    public void method1(String s) {

    }

    // setter
    public void setStudentId(int studentId) {
        this.studentId = studentId;
    }

    // getter
    public int getStudentId() {
        return this.studentId;
    }

    public void addGrade(int grade) {
        if (gradeIndex == grades.length) {
            return;
        }

        grades[gradeIndex] = grade;
        gradeIndex += 1;
    }

    public void addCourse(Course course) {

    }

    public double computeAverageGrade() {
        double average = 0;
        for (int i = 0; i < gradeIndex; i++) {
            average += grades[i];
        }

        return average / gradeIndex;
    }

    // method overwriting
    public void say() {
        System.out.println("I am a student");
    }

    public void test() {
        say();
        super.say();
    }
}

/*
 * if superclass has constructor, subcalss has to call
 * the superclass's contructor in its own constructor
 * 
 */