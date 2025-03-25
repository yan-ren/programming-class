package archived;

public class ExceptionExample {
    public static void main(String[] args){
        int numerator = 0;
        int denominator = 0;
        try {
            int[] array = new int[2];

            System.out.println(array[3]);
            System.out.println(numerator / denominator);
            System.out.println("Will this line be  printed?");
        } catch(ArithmeticException e){
            System.out.println("we are in catch block");
        } catch(ArrayIndexOutOfBoundsException e){
            System.out.println("array error");
        } catch(Exception e) {

        } finally {
            System.out.println("always run code in finally");
        }

        System.out.println("program finish!");
    }
}

// Given a string, each word in string is seperated by a space, extract all the numbers from the string into an array
// s = 'a is 123 345 hello 1a'
// result = [123, 345]