package archived;

/*
 * public, protected, default, private
 */
/*
 * static, non-static
 */
public class Person {
    private int id;
    public String gender;
    public String name;
    public static String nationality = "CN";

    // default constructor
    public Person() {

    }

    public Person(int id, String gender, String name) {
        this.id = id;
        this.gender = gender;
        this.name = name;
    }

    public int getId() {
        return this.id;
    }

    // non-static function
    // called through object
    public void setId(int id) {
        this.id = id;
    }

    // static function
    // called through class
    public static void print(String msg) {
        int tmp = 2;
        // non-static varialbe cannot be used in static function
        // System.out.println(this.id);

        System.out.println(msg);
    }

    public void say() {
        System.out.println("I am a person");
    }
}

/*
 * oop:
 * encaptuation intertance, abstraction, polymorphism
 * superclass and subclass
 */