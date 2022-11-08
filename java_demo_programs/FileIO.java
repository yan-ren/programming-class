import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.Scanner;

import javax.swing.tree.ExpandVetoException;

public class FileIO {
    public static void main(String[] args) {
        // try {
        // FileReader reader = new FileReader(
        // "/Users/yan.ren/github.com/yan.ren/programming-class/java_demo_programs/test.txt");
        // Scanner sc = new Scanner(reader);
        // while (sc.hasNext()) {
        // System.out.println(sc.nextLine());
        // }
        // } catch (Exception e) {
        // System.out.println(e);
        // }
        // try {
        // PrintWriter out = new PrintWriter("output.txt");
        // out.println("This is written by program");
        // out.close();
        // } catch (Exception e) {
        // e.printStackTrace();
        // }
        // try {
        // BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"));
        // PrintWriter out = new PrintWriter(bw);
        // out.println("first line");
        // out.println("second line");
        // out.close();
        // } catch (Exception e) {

        // }
        try {
            BufferedReader br = new BufferedReader(
                    new FileReader("/Users/yan.ren/github.com/yan.ren/programming-class/java_demo_programs/test.txt"));
            Scanner sc = new Scanner(br);
        } catch (Exception e) {

        }
    }

    public static void writeStudents(Student[] students, String fileName) {
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"));
            PrintWriter out = new PrintWriter(bw);
            for (int i = 0; i < students.length; i++) {
                out.println(students[i].name);
            }
            out.close();
        } catch (Exception e) {

        }

    }
}

/*
 * give two integer arrays, there is one number that is common between two
 * arrays find that common number
 * 
 * e.g. array1 = [1, 2, 3, 4] array2 = [0, 2, 5, 7]
 * 
 * output = 2
 */