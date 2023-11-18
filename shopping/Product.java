package shopping;

public class Product {
    private String name;
    private double price;
    // private int stock;
    private String category;

    // Constructor
    public Product(String name, double price) {
        this.name = name;
        this.price = price;
        // this.stock = stock;
        this.category = "";
    }

    // methods
    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    // public int getStock() {
    //     return stock;
    // }

    // public void setStock(int stock) {
    //     this.stock = stock;
    // }

    // public void decrementStock() {
    //     this.stock -= 1;
    // }

    public String getCategory() {
        return category;
    }
}
