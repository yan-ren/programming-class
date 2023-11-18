import java.util.HashMap;
import java.util.Map;

public class Test {
    public static void main(String[] args) {
        Map<String, Product> products = new HashMap<>();
        products.put("1", new Product());
        products.get("1");
    }
}

class Product {

}
/*
return keyword:
1. return value to where the function being called
2. terminate the function
*/