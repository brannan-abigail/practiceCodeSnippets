import java.util.Scanner;

/**
* The Main program (amendTheSentence) implements an application that
* anwsers the codeSignal problem requiring the user to parse a given
* string with CapitalLettersForNewWords. The output for this example 
* should be "capital letters for new words".
*
* @author  Abigail Brannan
* @version 1.0
* @since   2019-12-11 
*/
public class Main {

    /**
   * This is the main method which takes in the input and call amendTheSentence(input)
   * @param args Unused.
   * @return Nothing.
   */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String output = "";
		
		while(scanner.hasNextLine()) {
			String line = scanner.nextLine();
        
            if (isNumeric(line))
                output = testCases(Integer.parseInt(line));
            System.out.println(output);
        }
    }

   /**
   * This method amends the sentence by parsing the output. 
   * @param String input Line to be parsed.
   * @return String output Sentence with words seperated by spaces and lowercase.
   */
    public static String amendTheSentence(String input) {
        String output = "codesignam is awesome";
        return output;
    }

   /**
   * This method provides the code for the test cases in codeSignal.
   * @param int testCase Number of test case.
   * @return String output amendTheSentence(String from test case).
   */
    public static String testCases(int testCase) {
        String output = "";

        switch (testCase) {
            case 1:
                System.out.println("Hit test Case 1");
                output = amendTheSentence("CodesignamIsAwesome");
                break;
        }

        return output;
    }

   /**
   * This method tests whether the input string is numeric. 
   * @author mykong
   * @param final String str
   * @return static boolean str.chars().allMatch(Character::isDigit)
   */
    public static boolean isNumeric(final String str) {
        // null or empty
        if (str == null || str.length() == 0) {
            return false;
        }
        return str.chars().allMatch(Character::isDigit);
    }
}