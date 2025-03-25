package class0303;

import javax.swing.*;
import java.awt.*;

// everything has to be in class
/*
This is multi line comments

keywords
 */
public class Class2 extends JPanel {
    private int x = 50, y = 50, size = 30;
    private int dx = 3, dy = 3;

    public Class2() {
        new Timer(10, e -> {
            x += dx;
            y += dy;
            if(x <= 0 || x >= getWidth() - size) {
                dx = -dx;
            }
            if(y <= 0 || y >= getHeight() - size) {
                dy = -dy;
            }
            repaint();
        }).start();
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.fillOval(x, y, size, size);
    }

    public static void main(String[] args) {
        /*
        System.out.println("Welcome to programming class");
        System.out.println("Today is a good day");
        System.out.println(1 + 2);
        System.out.println(1 - 2);
        System.out.println(1 * 2);
        System.out.println(3.0 / 2);

        int x = 2; // x is integer, number without decimal points
        double y = 2.0;
        */
        JFrame f = new JFrame();
        f.add(new Class2());
        f.setSize(500, 500);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}