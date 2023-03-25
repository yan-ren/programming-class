import java.util.ArrayList;
import java.util.List;

/*
 * pure function: if the rutrned value depends only on the input parameter
 * 
 * higher order function: if a function can take another function as parameter or return a function
 * 
 * since java 8:
 * lambda function
 * functional interface
 * stream api
 * 
 * lambda function: we can create lambda function and pass it to another function as input parameter
 * 
 * (parameters) -> {statement};
 */
public class FunctionProgramming {
    public static void main(String[] args) {
        /*
         * () -> System.out.println("hello");
         * (parameter) -> System.out.println(parameter);
         * (x, y) -> x + y;
         * 
         * (x, y) -> {
         * System.out.prinltn(x);
         * System.out.println(y);
         * }
         */

        List<Book> books = new ArrayList<>();
        books.add(new Book("happy", 2020));
        books.add(new Book("sad", 2021));

        // print all books that have title begining with 'h'
        printAllBooksTathTitleBeginingWithh(books);
        // print all books that have year of publication > 2000

        // boolean test(Book book);
        printConditionally(books, book -> book.title.startsWith("h"));
        printConditionally(books, book -> book.year > 2000);

        //
        // map(fn, iterable)
    }

    public static void printAllBooksTathTitleBeginingWithh(List<Book> books) {
        for (Book book : books) {
            if (book.title.startsWith("h")) {
                System.out.println(book);
            }
        }
    }

    public static void printAllBooksThatHaveYearOfPublicationBiggerThan2000(List<Book> books) {
        for (Book book : books) {
            if (book.year > 2000) {
                System.out.println(book);
            }
        }
    }

    public static void printConditionally(List<Book> books, Condition condition) {
        for (Book book : books) {
            if (condition.test(book)) {
                System.out.println(book);
            }
        }
    }

    public int maxNumber(int a, int b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }
}

// for interface only has one function we call it functional interface
interface Condition {
    boolean test(Book book);
}

class Book {
    String title;
    int year;

    public Book(String title, int year) {
        this.title = title;
        this.year = year;
    }
}