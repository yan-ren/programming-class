package shopping;

public class ShopItem {
    private Product product;
    private int stock;

    public ShopItem(Product product, int stock){
        this.product = product;
        this.stock = stock;
    }

    public Product geProduct() {
        return product;
    }

    public int getStock() {
        return stock;
    }

    public void decreaseBy(int amount) {
        this.stock = this.stock - amount;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }
}
