

public class PigLatin {
	public static void main(String[] args) {
//		Scanner sc = new Scanner(System.in);
//		System.out.println("Enter a sentence that does not contain punctuation.");
//		String sentence = sc.nextLine();
//		String sentenceLowerCase = sentence.toLowerCase();
		// String input = "the quick brown fox jumped over the lazy dog";
		// System.out.println(Arrays.toString(tokenize(input)));
		
		// System.out.println(detectPrefix("quick"));
		// System.out.println(detectPrefix("one"));
		// System.out.println(detectPrefix("brown"));
		
		// System.out.println(pigLatinfy("pig"));
		// System.out.println(pigLatinfy("this"));

		String test = "the quick brown fox jumped over the lazy dog";
		String[] tokens = tokenize(test);
		String result = "";
		for(int i = 0; i < tokens.length; i++){
			result = result + pigLatinfy(tokens[i]) + " ";
		}

		System.out.println(result);
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

	public static String pigLatinfy(String input){
		String result = "";
		if(input.charAt(0) == 'a' || input.charAt(0) == 'e' || input.charAt(0) == 'i' || input.charAt(0) == 'o' || input.charAt(0) == 'u'){
			result = input + "w";
		}else {  
			String prefix = detectPrefix(input);
			if(prefix.length() != 0){
			 	result = input.substring(prefix.length());
				result += prefix;
			}
		}

		return result + "ay";
	}
}
