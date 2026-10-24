package comp250;

/*

*/
public class Class1 {


    public static void main(String[] args) {
        int a = 0;
        int[] n = {1, 2, 3};

        String b = "hello";
        char c = 'c';

        // class -> object, object, object ...
        Book b1 = new Book("Book 1", "Author 1", 100, 123);
        Book b2 = new Book("Book 2");
        // Book b2 = new Book();
        b1.title = "Book 1";
        b1.author = "Author 1";

        b1.printTitle();
        // b2.title = "Book 2";
        // b2.author = "Author 2";

    }

    public static int calculate(int a, int b) {
        int c = a + b;
        return c;
    }
}


class Book {
    String title;
    String author;
    int page;
    int idName;

    public Book(String title) {
        this.title = title;
    }

    public Book(String title, String author, int page, int idName) {
        this.title = title;
        // title = bookTitle;
        this.author = author;
        this.page = page;
        this.idName = idName;
    }

    public void printTitle() {
        System.out.println(this.title);
    }
}
