package shopping;

import java.util.ArrayList;
import java.util.List;

public class Cart {
    private List<CartItem> items;
 
    // Constructor
    public Cart() {
        items = new ArrayList<>();
    }
 
    // Method to add product to cart
    // addProduct(p1, 2);
    public void addProduct(Product product, int quantity) {
        // Add logic to handle product addition to the cart
        // create product to be used in Cart
        Product newProduct = new Product(product.getName(), product.getPrice());

        // add newProduct to cart 
        items.add(new CartItem(newProduct, quantity));
    }
 
    // Method to calculate total cart amount
    public double calculateTotalAmount() {
        // Add logic to calculate total cart amount
        return 0.0; // Placeholder return statement
    }
 
    // Method to clear cart after payment
    public void clearCart() {
        items.clear();
    }
 
    // Getter method for products in the cart
    public List<CartItem> getItems() {
        return items;
    }
}

