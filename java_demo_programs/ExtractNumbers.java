import javax.swing.tree.ExpandVetoException;

public class ExtractNumbers {
	
	public static void main (String[]args) {
		String test = "a is 123 345 hello 1a";
		// String[] tokens = tokenize(test);
		// String result = "";
		// for (int i = 0; i < tokens.length; i++) {
		// 	result = result + tokenize(tokens[i]) + " ";
		// }
		// System.out.println(result);
		String[] tokens = test.split(" ");
		int number;
		int[] result = new int[1000];
		int index = 0;
		for(int i = 0; i < tokens.length; i++){
			try{
				number = Integer.parseInt(tokens[i]);
			}catch(NumberFormatException e){
				continue;
			}
			result[index] = number;
			index+=1;
		}

		for(int i = 0; i < result.length; i++){
			System.out.println(result[i]);
		}
	
	}

	public static String[] tokenize(String arr) {
		String[] arr1 = new String[1000];
		String word = "";
		int wordCount = 0;
		int j = 0;
		for (int i = 0; i < arr.length(); i++) {
			if (arr.charAt(i) != ' ' && (arr.charAt(i) == '0' && arr.charAt(i) == '1' || arr.charAt(i) == '2' || arr.charAt(i) == '3' || arr.charAt(i) == '4' || arr.charAt(i) == '5' || arr.charAt(i) == '6' || arr.charAt(i) == '7' || arr.charAt(i) == '8' || arr.charAt(i) == '9')) {
				word += arr.charAt(i);
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
}