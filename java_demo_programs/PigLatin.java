package playground;

import java.util.Arrays;
import java.util.Scanner;

public class PigLatin {
	public static void main(String[] args) {
//		Scanner sc = new Scanner(System.in);
//		System.out.println("Enter a sentence that does not contain punctuation.");
//		String sentence = sc.nextLine();
//		String sentenceLowerCase = sentence.toLowerCase();
		String input = "the quick brown fox jumped over the lazy dog";
		System.out.println(Arrays.toString(tokenize(input)));
		
		System.out.println(detectPrefix("quick"));
		System.out.println(detectPrefix("one"));
		System.out.println(detectPrefix("brown"));
		
	}

	public static String[] tokenize(String sentenceLowerCase) {
		String[] arr1 = new String[1000];
		String word = "";
		int wordCount = 0;
		int j = 0;
		for (int i = 0; i < sentenceLowerCase.length(); i++) {
			if (sentenceLowerCase.charAt(i) != ' ') {
				word += sentenceLowerCase.charAt(i);
			} else {
				arr1[j] = word;
				wordCount += 1;
				j++;
				word = "";
			}
		}

		if (!word.isEmpty()) {
			wordCount++;
			arr1[j] = word;
		}

		String[] output = new String[wordCount];
		for (int i = 0; i < output.length; i++) {
			output[i] = arr1[i];
		}

		return output;
	}

	public static String detectPrefix(String input) {
		String prefix = "";
		for (int i = 0; i < input.length(); i++) {
			if (input.charAt(i) != 'a' && input.charAt(i) != 'e' && input.charAt(i) != 'i' && input.charAt(i) != 'o'
					&& input.charAt(i) != 'u') {
				prefix += input.charAt(i);
			}else {
				return prefix;
			}
		}
		
		return prefix;
	}

	public static void pigLatinfy(String prefix, String[] arr1, int prefixIndex) {
		for (int i = 0; i < arr1.length; i++) {
			if (prefix == "") {
				arr1[i] = arr1[i] + "way";
			} else {
				arr1[i] = arr1[i].substring(prefixIndex) + prefix + "ay";
			}
		}
		for (int i = 0; i < arr1.length; i++) {
			System.out.print(arr1[i] + " ");
		}
	}
}
