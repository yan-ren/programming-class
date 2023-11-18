package shopping;

public class CartItem {
    private Product product;
    private int quantity;

    // complete...
    public CartItem(Product product, int quantity){
        this.product = product;
        this.quantity = quantity;
    }

    // getter/setter
    public Product geProduct() {
        return this.product;
    }

    public int getQuantity() {
        return this.quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
}
