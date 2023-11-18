package shopping;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ToyShopApp {
    public static void main(String[] args) {
        // Initialize the toy shop with some products
        List<ShopItem> shopItems = new ArrayList<>();
        ToyShop toyShop = new ToyShop(shopItems);

        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            // Display menu options
            System.out.println("Menu:");
            System.out.println("1. Add Product");
            System.out.println("2. Show Products");
            System.out.println("3. Buy Product");
            System.out.println("4. Show Cart");
            System.out.println("5. Payment");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            // Handle user choices
            switch (choice) {
                case 1:
                    // Add product logic
                    break;
                case 2:
                    // Show products logic
                    break;
                case 3:
                    // Buy product logic
                    // toyShop.buyProduct(productNumber, quantity);
                    break;
                case 4:
                    // Show cart logic
                    break;
                case 5:
                    // Payment logic
                    break;
                case 6:
                    System.out.println("Exiting Toy Shop. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        } while (choice != 6);

        scanner.close();
    }
}
