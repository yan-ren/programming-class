package shopping;

import java.util.ArrayList;
import java.util.List;

public class ToyShop {
    private List<ShopItem> shopItems;
    private Cart cart;

    // Constructor
    public ToyShop(List<ShopItem> shopItems) {
        this.shopItems = shopItems;
        this.cart = new Cart();
    }

    // Method to add a product to the shop's inventory
    public void addProduct(Product product, int stock) {
        shopItems.add(new ShopItem(product, stock));
    }

    // Method to display list of available products
    public void showProducts() {
        // Add logic to display available products
    }

    // Method to handle product purchase
    /*
     * check if quantity is less than stock
     * then
     * add product in cart, decrease stock in shop
     * else
     * not enough stock
     */
    public void buyProduct(int productNumber, int quantity) {
        // Add logic to handle product purchase

        // invalid purchase
        if (shopItems.get(productNumber).getStock() < quantity ) {
            return;
        }

        cart.addProduct(shopItems.get(productNumber).geProduct(), quantity);
        shopItems.get(productNumber).decreaseBy(quantity);
    }

    // Method to display items in the cart
    public void showCart() {
        // Add logic to display items in the cart
    }

    // Method to process payment and clear the cart
    public void processPayment() {
        // Add logic to process payment and clear the cart
    }

    // Getter method for products in the shop
    public List<ShopItem> getProducts() {
        return shopItems;
    }
}
